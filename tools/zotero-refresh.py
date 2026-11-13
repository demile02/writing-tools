#!/usr/bin/env python3
"""zotero-refresh.py — perbarui field sitasi Zotero di dalam DOCX dari data library TERKINI.

Cara kerja:
1. Pindai word/document.xml dan word/footnotes.xml untuk field ADDIN ZOTERO_ITEM / ZOTERO_BIBL.
2. Untuk setiap item yang disitir, ambil data CSL + teks terformat (footnote & daftar rujukan)
   dari mesin sitasi Zotero sendiri (local API, include=citation/bib, gaya dokumen).
3. Tulis ulang hasil field (teks tampak) dan itemData tertanam, supaya dokumen selalu
   mengikuti metadata library. Berkas asli disimpan sebagai .bak.

Pakai: python3 zotero-refresh.py <dokumen.docx> [--style turabian-fullnote-bibliography]
"""
import argparse, html, json, re, shutil, sys, urllib.request, zipfile
from copy import deepcopy
from lxml import etree

API = "http://127.0.0.1:23119/api/users/0"
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}

def api(url):
    req = urllib.request.Request(url, headers={"Zotero-API-Version": "3"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8")

def api_json(url):
    return json.loads(api(url))

def segments_from_html(fragment):
    """Ubah HTML citeproc menjadi daftar (teks, italic)."""
    frag = re.sub(r"<span[^>]*>.*?</span>", "", fragment, flags=re.S)
    parts = re.split(r"(</?i>)", frag)
    segs, italic = [], False
    for p in parts:
        if p == "<i>":
            italic = True
        elif p == "</i>":
            italic = False
        else:
            t = html.unescape(re.sub(r"<[^>]+>", "", p))
            if t:
                segs.append((t, italic))
    return segs

def plain(segs):
    return "".join(t for t, _ in segs)

def make_run(text, italic, base_rpr):
    r = etree.SubElement(etree.Element("x"), "{%s}r" % W)  # placeholder, diganti di bawah
    return r

def build_run(text, italic, base_rpr):
    r = etree.Element("{%s}r" % W)
    if base_rpr is not None:
        rpr = deepcopy(base_rpr)
        # buang penanda italic lama, atur sesuai segmen
        for tag in ("i", "iCs"):
            for el in rpr.findall("{%s}%s" % (W, tag)):
                rpr.remove(el)
        if italic:
            rpr.append(etree.Element("{%s}i" % W))
        r.append(rpr)
    t = etree.SubElement(r, "{%s}t" % W)
    t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    t.text = text
    return r

def field_spans(par):
    """Kembalikan (runs, idx_begin, idx_sep, idx_end) untuk field Zotero dalam satu paragraf."""
    runs = par.findall("w:r", NS)
    begin = sep = end = None
    for i, r in enumerate(runs):
        fc = r.find("w:fldChar", NS)
        it = r.find("w:instrText", NS)
        if fc is not None:
            t = fc.get("{%s}fldCharType" % W)
            if t == "begin": begin = i
            elif t == "separate": sep = i
            elif t == "end": end = i
        if it is not None and "instr" not in dir():
            pass
    return runs, begin, sep, end

def get_instr(par):
    for r in par.findall("w:r", NS):
        it = r.find("w:instrText", NS)
        if it is not None:
            return it
    return None

def replace_result(par, segs):
    """Ganti run hasil (antara separate dan end) dengan segmen baru."""
    runs = par.findall("w:r", NS)
    sep = end = None
    for i, r in enumerate(runs):
        fc = r.find("w:fldChar", NS)
        if fc is not None:
            t = fc.get("{%s}fldCharType" % W)
            if t == "separate": sep = i
            elif t == "end": end = i
    if sep is None or end is None:
        return False
    base_rpr = None
    if end - sep > 1:
        base_rpr = runs[sep + 1].find("w:rPr", NS)
    for r in runs[sep + 1:end]:
        par.remove(r)
    end_run = runs[end]
    for text, italic in segs:
        end_run.addprevious(build_run(text, italic, base_rpr))
    return True

def process_part(root, style, cache):
    """Perbarui semua field sitasi dalam satu part XML. Kembalikan set key yang disitir."""
    cited = []
    for par in root.iter("{%s}p" % W):
        instr = get_instr(par)
        if instr is None or "ZOTERO_ITEM" not in (instr.text or ""):
            continue
        m = re.search(r"CSL_CITATION\s*(\{.*\})\s*$", instr.text.strip(), re.S)
        if not m:
            continue
        cit = json.loads(m.group(1))
        new_items = []
        note_segs = None
        for ci in cit["citationItems"]:
            uri = ci["uris"][0]
            key = uri.rstrip("/").split("/")[-1]
            cited.append(key)
            if key not in cache:
                csl_list = api_json(f"{API}/items?itemKey={key}&format=csljson")
                styled = api_json(f"{API}/items/{key}?include=citation,bib&style={style}")
                cit_html = styled.get("citation", "")
                mm = re.search(r"<li>(.*?)</li>", cit_html, re.S)
                cache[key] = {
                    "csl": csl_list[0],
                    "note_segs": segments_from_html(mm.group(1) if mm else ""),
                }
            c = cache[key]
            nci = dict(ci)
            nci["uris"] = [c["csl"]["id"]]
            nci["itemData"] = {k: v for k, v in c["csl"].items() if k != "id"}
            nci["itemData"]["id"] = ci.get("id", 1)
            new_items.append(nci)
            note_segs = c["note_segs"]
        cit["citationItems"] = new_items
        if note_segs:
            cit.setdefault("properties", {})["formattedCitation"] = plain(note_segs)
            replace_result(par, note_segs)
        instr.text = " ADDIN ZOTERO_ITEM CSL_CITATION " + json.dumps(cit, ensure_ascii=False) + " "
    return cited

def refresh_bib(root, style, keys):
    for par in root.iter("{%s}p" % W):
        instr = get_instr(par)
        if instr is None or "ZOTERO_BIBL" not in (instr.text or ""):
            continue
        styled = api(f"{API}/items?itemKey={','.join(keys)}&include=bib&style={style}")
        data = json.loads(styled)
        blocks = data if isinstance(data, list) else [data]
        entries = []
        for b in blocks:
            entries += re.findall(r'<div class="csl-entry">(.*?)</div>', b.get("bib", ""), re.S)
        entries.sort(key=lambda e: plain(segments_from_html(e)).lower())
        if not entries:
            return
        segs = segments_from_html(entries[0])
        replace_result(par, segs)
        # entri tambahan: sisipkan paragraf kloning sesudahnya (teks polos terformat sama)
        anchor = par
        for extra in entries[1:]:
            np = deepcopy(par)
            # bersihkan field dari kloningan; sisakan paragraf teks biasa
            for r in np.findall("w:r", NS):
                np.remove(r)
            base = None
            for text, italic in segments_from_html(extra):
                np.append(build_run(text, italic, base))
            anchor.addnext(np)
            anchor = np

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("docx")
    ap.add_argument("--style", default="turabian-fullnote-bibliography")
    args = ap.parse_args()

    shutil.copyfile(args.docx, args.docx + ".bak")
    zin = zipfile.ZipFile(args.docx)
    parts = {n: zin.read(n) for n in zin.namelist()}
    infos = zin.infolist()
    zin.close()

    cache = {}
    cited_all = []
    roots = {}
    for name in ("word/footnotes.xml", "word/document.xml"):
        if name not in parts:
            continue
        root = etree.fromstring(parts[name])
        roots[name] = root
        cited_all += process_part(root, args.style, cache)
    keys = list(dict.fromkeys(cited_all))
    if not keys:
        print("Tidak ada field sitasi Zotero ditemukan.")
        return
    if "word/document.xml" in roots:
        refresh_bib(roots["word/document.xml"], args.style, keys)
    for name, root in roots.items():
        parts[name] = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True)

    with zipfile.ZipFile(args.docx, "w", zipfile.ZIP_DEFLATED) as zout:
        for info in infos:
            zout.writestr(info, parts[info.filename])
    print(f"Refresh selesai: {args.docx} | item disitir: {keys} | gaya: {args.style}")

if __name__ == "__main__":
    main()
