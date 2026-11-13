---
name: gaya-ilmiah
description: "Gaya Ilmiah: core filter for academic writing in Indonesian and English from a SINTA 1 journal corpus. Load always for scholarly writing; load with the language sub-skill."
---

> Companion skills: the rules cited as R-xx live in antislop and antislop-copywriting, which are not in this repository. If they are not installed yet, install them first: `npx skills add miqdadbadjuber/anti-slop`. The SINTA 1 corpus behind these patterns is the author's local corpus and is not distributed; the patterns apply without it.
# gaya-ilmiah

> Gaya Ilmiah: Rules for AI Agents Writing Academic Prose. The core filter
> for scholarly writing in Indonesian and English, built on a verified
> corpus of SINTA 1 journal articles.

> Part of a system: this core plus `gaya-ilmiah-indonesia` and
> `gaya-ilmiah-inggris`. Load the core always for academic writing tasks,
> then the sub-skill matching the language of the text. This system stands
> on `antislop` and `antislop-copywriting`; where they apply, cite their
> rule numbers (R-02, R-16, R-17, R-36, R-38) and never renumber them.
> Corpus and pattern inventory live in ~/workspace/skill-gaya-ilmiah/
> (pola-gaya-korpus.md, pola-statistik.json) with sources in
> ~/workspace/corpus-jurnal-sinta1/.

## What this is

A filter, not a beautifier. It stops academic prose that reads as
AI-generated while keeping the register, terminology, and conventions of
real published scholarship. It does not supply arguments, data, or
citations. Those come from the user or from verified sources only.

## Core principle

Published academic writing is specific in three places at once: the claim
names its object, the number names its instrument and threshold, and the
citation names its location. AI academic prose is vague in all three at
once. Every rule below protects one of those three specificities.

## Hard rules (G-series, absolute unless a sub-skill states an exception)

- **G-01, No fabricated citations.** A citation may be written only when
  its document is real and accessible: active DOI, publisher or official
  repository page opening the document, or the file in the user's hands.
  Never cite from model memory or from another paper's reference list
  without opening the source. Incomplete citation details are marked
  [sitasi belum terverifikasi], never completed by guessing.
  (Extends R-17, R-36, R-38.)
- **G-02, No fabricated facts.** A rewrite adds no fact, name, number,
  date, instrument, or result that is not in the user's material or a
  verified source. If a sentence needs real detail to work, ask for it or
  write the plain version without it. (R-36, R-38.)
- **G-03, Claim-to-evidence mapping.** Before delivery, every substantive
  claim in every paragraph must point to one of: a verified source (G-01),
  the user's own data named in the task, or an explicit label as the
  author's argument. A claim that points to none of these is deleted or
  returned to the user as a question.
- **G-04, No em dash.** The em dash character is forbidden in authored
  text (R-02). Replace with a period, comma, colon, or parentheses.
- **G-05, Numbers carry instrument and threshold.** In results writing,
  a number never stands alone: it is written with the instrument or
  analysis that produced it and the threshold or comparator that gives
  it meaning. Numbers missing those are returned for completion, not
  smoothed over. (Extends R-17.)
  Clarification from field test 1: a qualitative category stated in the
  user's own material ("sangat valid", "sangat efektif") without its score
  is preserved exactly as the source's claim. Never convert it into an
  invented score, and never delete it silently; flag the missing score in
  the delivery note instead.
- **G-06, Bilingual abstract consistency.** Indonesian and English
  abstracts are checked as one pair: same aim, same method, identical
  numbers, equally strong conclusion. Neither version adds a claim the
  other lacks.
- **G-07, Do not over-sterilize.** Formal register, technical terms, and
  the conventions named in the sub-skills (methods passives, nominalized
  procedures, footnote citations) are legitimate scholarly style. Removing
  them is as much a defect as leaving AI patterns in. (Extends R-37.)
- **G-08, Corpus frames may be borrowed, corpus sentences may not.**
  Sentence frames, transitions, and number-attachment habits from the
  corpus inventory may be matched. Whole corpus sentences enter user text
  only as cited quotations.

## Corpus calibration (use before drafting)

1. Identify the language and the section being written (abstract, method,
   results, discussion, conclusion).
2. Pull the matching patterns from the inventory
   (~/workspace/skill-gaya-ilmiah/pola-gaya-korpus.md): customary openings,
   transitions with their real frequencies, method and result phrasing,
   citation habits. Match the frame, fill it only with the user's material.
3. If the inventory has no pattern for that section, say so. Do not invent
   a pattern and call it corpus-based.
4. A user-supplied writing sample outranks the corpus for voice; the
   corpus outranks generic academic habit. Order: user sample, corpus,
   default rules.

## Draft, Audit, Final (mandatory loop)

1. **Draft** applying the core and the language sub-skill.
2. **Audit** by answering two questions in writing, briefly: "What makes
   this obviously AI-generated?" and "Does any sentence state a fact,
   number, or citation that is not in the user's material or a verified
   source?"
3. **Final** revising against both answers, then running the Delivery
   Gate below.

## Delivery notes (where disclosures live)

Anything the audit removed, could not verify, or needs from the user is
reported in a short note that accompanies the text, never as a sentence
inside the manuscript itself. A manuscript sentence like "the source names
no prior studies, so no gap is claimed here" is a delivery note that
leaked into the text; move it out. The manuscript carries only manuscript
content; the note carries the accounting.

## Delivery Gate (every line must be true)

- [ ] No citation written without G-01 verification; unverified ones carry the honest marker
- [ ] Every substantive claim maps to a source, user data, or an author-argument label (G-03)
- [ ] No number stands without instrument and threshold (G-05)
- [ ] Bilingual abstracts match in aim, method, numbers, conclusion (G-06)
- [ ] No em dash in the output (G-04)
- [ ] No era opener, no unmapped gap claim, no generic optimistic conclusion (sub-skill patterns)
- [ ] Methods passives and legitimate formal terms preserved, not flattened (G-07)
- [ ] Sentence lengths vary: short statements of fact alongside longer data or concession sentences, per corpus distributions
- [ ] Read aloud: the text sounds like the corpus read aloud, not like a model summarizing scholarship
