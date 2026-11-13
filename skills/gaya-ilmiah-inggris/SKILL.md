---
name: gaya-ilmiah-inggris
description: "English academic writing patterns from a SINTA 1 corpus (IJIMS, Studia Islamika): scope openings, mapped gap claims, calibrated findings, and English academic AI tells. Load with gaya-ilmiah."
---

> Load with gaya-ilmiah. The full stack also needs antislop and antislop-copywriting: `npx skills add miqdadbadjuber/anti-slop` if they are missing.
# gaya-ilmiah-inggris

> Gaya Ilmiah Inggris: patterns for English scholarly writing from a SINTA 1
> corpus (IJIMS, Studia Islamika, and Al-Jami'ah, 2023-2026).

> Load with `gaya-ilmiah` (the core). This skill holds English patterns
> only; the core holds the mechanism and hard rules (G-01 to G-08) plus the
> antislop rules cited by number. Corpus: ~/workspace/corpus-jurnal-sinta1/en/,
> inventory: ~/workspace/skill-gaya-ilmiah/pola-gaya-korpus.md.

## Corpus measurements (the target rhythm)

- Mean sentence length 24.3 words, median 22.3. Long sentences above 35
  words are common (19.0 percent) but short sentences still occur
  (13.2 percent below 10 words). The rhythm is mixed, never uniformly
  mid-length.
- "However" is the dominant concession transition (51 occurrences across
  seven articles) and always carries a real objection.

## Positive patterns (write this way)

### E1, Open with scope, not with an era
- "This article examines the role of religion in contemporary social
  movements in Indonesia using the framework of relative deprivation
  theory." (Kuswana et al., 2024)
- "This study examines the role of ideas and politics within Muslim
  organizations, political parties, and the state in Indonesia."
  (Munhanif & Ihsan, 2023)

### E2, Show the gap through a specific objection
- "However, there's been little exploration into the historical evolution
  of their ideologies and political preferences in religious politics."
  (Munhanif & Ihsan, 2023)
- "However, their manifestations and impacts vary depending on the specific
  context of each movement." (Kuswana et al., 2024)
The gap is demonstrated against named prior work, never declared in the
abstract phrase "there is a gap in the literature" without that map (G-03).

### E3, Calibrate findings inside the sentence
- "The findings show that, while relative deprivation plays a significant
  role in motivating participation in religious social movements,
  contextual factors such as political opportunity structures and
  organizational resources also play an important role."
  (Kuswana et al., 2024)
The "while X, Y also" shape keeps the claim proportionate to field data.

### E4, State the contribution in measured terms
- "Theoretically speaking, the article aims to contribute to developing a
  more authentic and strategic citizenship perspective so that the
  recognition of minority groups in a Muslim-majority country can
  transpire harmoniously, not confrontationally." (Qodir & Hefner, 2024)
Name what the contribution changes, for whom, in what debate.

### E5, Methods stated briefly and explicitly
- "This article uses qualitative analytical methods by emphasizing field
  findings with interviews and literature reviews of articles that match
  the research theme." (Qodir & Hefner, 2024)
Passive methods sentences ("Data were collected through interviews") are
equally standard and are not to be forced into active voice.

### E6, Citations tied to the claim
The corpus journals use numbered footnotes (IJIMS, Studia Islamika) and
name-year references inside argument sentences, e.g. "(Blood 1974, 34)".
Either system is acceptable; mixing both inside one manuscript is not.
Every claim's number stands in the same sentence or footnote as its
source (G-01, G-03).

### E7, Draw the conclusion with "therefore" after the evidence
- "Bourdieu defines cultural capital as a resource that is accumulated
  or transmitted through social interaction, including education.
  Therefore, this article aims to reveal the curriculum developed by
  Salafi educational institutions, and then review the compatibility of
  the curriculum with the national ideology of Indonesia."
  (Basya et al., 2026)
- "Therefore, the 'digital' here does not imply abandoning the physical
  world; rather, online spaces help participants find like-minded
  audiences that can lead to local community formation (Herding 2013)."
  (Herdiansah, 2026)
"Therefore" (35 occurrences across six of the seven articles, in three
journals) always follows evidence, a definition, or a finding just
stated, and draws one specific inference from it. It never opens a
paragraph with a platitude and never stands in for missing evidence.

## Anti-patterns (AI tells in English academic prose)

### Era Opener
- **The pattern:** "In recent years, X has gained significant attention",
  "In today's rapidly evolving world", "X plays a crucial role in".
- **Why:** interchangeable warm-up; the corpus opens with E1 instead.
- **Fix:** state the scope and the framework in the first sentence.
- **Rule:** R-36, R-16. "Significant" only with a test or a number (G-05).

### Unmapped Gap Claim
- **The pattern:** "This study aims to fill the gap" with no named
  literature the gap is measured against.
- **Why:** a gap is a claim about other work; without the map it is
  fabricated specificity (R-36, G-03).
- **Fix:** E2. Name the work, state what it does not do, then position
  this study.
- **Not a ban:** a gap claim with named prior studies and a specific
  missing element is legitimate and is what E2 models.

### Uncalibrated Findings
- **The pattern:** "The results prove that X is the most important
  factor", absolute and one-directional.
- **Why:** field research in the corpus calibrates inside the sentence;
  "prove" overstates what one study's design can carry.
- **Fix:** E3. Replace "prove" with the verb the design supports (show,
  suggest, indicate) and add the real counterweight when one exists.
- **Rule:** R-36, C-5 of antislop.

### Empty Academic Vocabulary
- **The pattern:** delve, pivotal, crucial, landscape (abstract),
  tapestry, shed light on, a growing body of literature, with no data
  attached.
- **Why:** the scholarly dialect of the buzzword list in R-16; absent
  from the corpus.
- **Fix:** name the action, the count, or the specific studies.
- **Rule:** R-16, R-36.

## What NOT to flag in English academic text

- Long sentences that carry data, a concession, or a citation chain.
  Corpus mean is 24.3 words; length alone is not a tell.
- "However" used with a genuine objection (E2). It is the corpus's main
  concession marker.
- Established disciplinary terms, even multisyllabic ones. Precision is
  not buzzword use; an empty term is one that survives unchanged when the
  topic changes.
- Footnote-heavy passages in the corpus journals' house styles (E6).
