# Penulisan Ilmiah

Paket skill penulisan karya ilmiah berbahasa Indonesia untuk agent AI: gaya akademik terverifikasi sumber, format dokumen mengikuti acuan resmi lembaga, dan sitasi Zotero yang tidak diketik manual.

## Isi paket

Empat skill karya asli dalam repo ini:

| Skill | Isi |
| --- | --- |
| `gaya-ilmiah` | Inti gaya akademik dari korpus jurnal SINTA 1: klaim wajib berbasis sumber yang dibaca penuh, gerbang klaim-bukti, catatan penyampaian. |
| `gaya-ilmiah-indonesia` | Pola penulisan akademik bahasa Indonesia: pembuka, suara metode, bingkai hasil, transisi, dan ciri tulisan AI yang harus dihindari. |
| `gaya-ilmiah-inggris` | Pola penulisan akademik bahasa Inggris dari korpus SINTA 1. |
| `sistematika-karya-ilmiah` | Format karya tulis: acuan resmi lembaga sebagai sumber utama, halaman A4, Times New Roman, heading dan judul bab, jorok 0,63 cm, tabel identitas dan tanda tangan, daftar isi otomatis, sitasi Zotero, verifikasi render, dan kebiasaan kirim. |

Satu berkas perekat:

- `SOUL.md` — persona penulis akademik beserta daftar tumpukan skill yang wajib dimuat. Pemasangannya mengikuti `INSTRUKSI-INSTALL.md`: agent wajib menjelaskan dulu, mencadangkan SOUL.md asli user, dan meminta persetujuan eksplisit sebelum menimpa.

Satu alat:

- `tools/zotero-refresh.py` — penyegar field sitasi Zotero di dalam DOCX dari data library terkini, dipakai saat audit sitasi (lihat skill sistematika).

## Ketergantungan: antislop

Tumpukan ini bekerja di atas enam skill **antislop** karya Miqdad Badjuber, yang tidak dibundel di repo ini. Pasang dari sumber resminya:

```bash
npx skills add miqdadbadjuber/anti-slop
```

## Cara pasang paket ini

Urutan pasang penting: antislop dulu, baru paket ini, supaya rujukan aturan antar-skill langsung tersambung.

```bash
npx skills add miqdadbadjuber/anti-slop
npx skills add demile02/writing-tools
```

Lalu minta agent membaca `INSTRUKSI-INSTALL.md` untuk pemasangan SOUL.md yang aman (cadangan dulu, persetujuan user, baru timpa).

Urutan muat tumpukan saat menulis: antislop inti, antislop copywriting, gaya-ilmiah, gaya-ilmiah-indonesia atau gaya-ilmiah-inggris sesuai bahasa teks, sistematika-karya-ilmiah; sub-skill antislop bidang lain (ui, human, layoutmobile, code) dimuat saat bidangnya dikerjakan.

## Lisensi

MIT. Antislop adalah karya terpisah dengan lisensi dan repositori sendiri.
