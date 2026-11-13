---
name: gaya-ilmiah-indonesia
description: "Indonesian academic writing patterns from a SINTA 1 corpus (JPEP UNY): openings, methods voice, results frames, transitions, and Indonesian AI tells. Load with gaya-ilmiah."
---
# gaya-ilmiah-indonesia

> Gaya Ilmiah Indonesia: pola penulisan karya tulis ilmiah berbahasa
> Indonesia dari korpus jurnal SINTA 1 (5 artikel: JPEP UNY, Jurnal
> Ilmiah Psikologi Terapan UMM, dan Jurnal Entomologi Indonesia,
> 2017-2026).

> Load with `gaya-ilmiah` (the core). This skill holds Indonesian patterns
> only; the core holds the mechanism and hard rules (G-01 to G-08) plus the
> antislop rules cited by number. Corpus: ~/workspace/corpus-jurnal-sinta1/id/,
> inventory: ~/workspace/skill-gaya-ilmiah/pola-gaya-korpus.md.

## Corpus measurements (the target rhythm)

- Mean sentence length 18.5 words, median 15.8. Long sentences above 35
  words are rare (8.8 percent). Vary length on purpose: short factual
  sentences next to longer analytical ones.
- Era openers ("di era", "tidak dapat dipungkiri") occur zero times in the
  corpus. Conclusions phrases occur only where a real result is concluded.

## Positive patterns (write this way)

### P1, Open on the object and aim
Abstracts and introductions start with the object or the aim, no warm-up.
- "Tujuan penelitian ini adalah mengeksplorasi faktor-faktor yang
  mempengaruhi kearifan konselor menurut perspektif calon konselor etnis
  Jawa." (Herdi dkk., 2017)
- "Penelitian ini bertujuan untuk mengembangkan instrumen asesmen diri guru
  pada aktivitas pengembangan keprofesian berkelanjutan yang handal."
  (Kasmayadi dkk., 2018)

### P2, Methods in procedural nominal and passive voice
- "Pengumpulan data menggunakan angket yaitu Skala Anteseden Kearifan
  Konselor yang berbentuk skala lima jenjang." (Herdi dkk., 2017)
- "Sampel penelitian berjumlah 270 calon konselor etnis Jawa semester enam
  dari 11 Program Studi Bimbingan dan Konseling di Indonesia." (Herdi dkk.)
- "Validitas dan reabilitas instrumen telah diuji sehingga instrumen dapat
  digunakan dengan valid dan reliabel." (Nugroho, 2018)
This passive is the convention. Never rewrite methods procedures into
active first person to satisfy a generic active-voice rule.

### P3, Results with fixed frame, changing content
Frame: result subject + "menunjukkan bahwa" + finding with its number and
threshold (G-05).
- "Hasil penelitian menunjukkan terdapat enam faktor yang mempengaruhi
  kearifan konselor menurut perspektif calon konselor etnis Jawa."
- "Hasil analisis faktor dengan program SPSS 17.0 menunjukkan bahwa nilai
  KMO sebesar 0,921 (KMO>0,50)." (Kasmayadi dkk., 2018)

### P4, Transitions the corpus actually uses
By combined frequency: berdasarkan, menunjukkan bahwa, selain itu, dengan
demikian, menurut (attached to a named claim), oleh karena itu, sesuai
dengan. Prefer these over generic filler transitions. A transition must
carry a real logical relation; delete transitions that only pad.

### P5, Conclusions tied to a named result
- "Berdasarkan hasil perhitungan reliabilitas konstrak, dapat disimpulkan
  bahwa reliabilitas konstrak model asesmen diri aktivitas pengembangan
  keprofesian berkelanjutan guru adalah baik (CR > 0,70)."
  (Kasmayadi dkk., 2018)
"dapat disimpulkan bahwa" at most once per subsection, always attached to
the result it concludes.

### P6, Cite with menurut attached to one claim, with location
Name, year, and page stand next to the claim they support, followed by the
author's own assessment in the next sentence. One source per claim is the
corpus habit, not three definitions in a row.

## Anti-patterns (AI tells in Indonesian academic prose)

### Pembuka Era dan Pembuka Keharusan
- **The pattern:** "Di era globalisasi ini", "Di zaman yang serba digital
  ini", "Tidak dapat dipungkiri bahwa", "Pendidikan merupakan hal yang
  sangat penting bagi".
- **Why:** fits any topic, says nothing, absent from the corpus entirely.
- **Fix:** open with P1.
- **Rule:** R-36, G-03.
- **Not a ban:** a specific historical setting used as data ("pada masa
  Orde Baru") may open a paragraph; that is a fact, not warm-up.

### Pengisi Simpulan Berulang
- **The pattern:** "Berdasarkan uraian di atas, dapat disimpulkan bahwa"
  or "Hal ini menunjukkan bahwa" closing most paragraphs.
- **Why:** ritual closing replacing an actual logical link.
- **Fix:** P5, once per subsection and tied to a named result.
- **Rule:** R-36, G-05.

### Tumpukan Definisi Para Ahli
- **The pattern:** "Menurut X ... Menurut Y ... Menurut Z ..." with no
  position from the writer.
- **Why:** compiling is not synthesizing. The corpus attaches "menurut" to
  a single claim with its location (P6).
- **Fix:** keep the definition the study actually uses, say why it was
  chosen, derive its indicators. Others get at most one distinguishing
  sentence.
- **Rule:** R-36, C-5 of antislop, G-01 for the location details.

### Hedging Bertumpuk versi Indonesia
- **The pattern:** "dapat dikatakan bahwa kiranya" and similar stacks.
- **Why:** one qualifier does the work; stacking reads as evasion.
- **Fix:** keep the single qualifier that matches the evidence strength.
- **Rule:** R-36.

## What NOT to flag in Indonesian academic text

- Methods passives and nominalizations (P2). They are the convention.
- Formal connectives used once with a real relation (P4).
- Long noun phrases naming instruments, programs, or regulations in full.
  Indonesian scholarship names institutions completely; that is precision,
  not padding.
- Repetition of the study's key term. Repeat the clearest term rather than
  cycling synonyms, matching antislop-copywriting on synonym cycling.
