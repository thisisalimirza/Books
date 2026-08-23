# Not Yet Captured

**Working subtitle:** A Physician-in-Training's Case Against Medicine's Scarcity Mindset
**Status:** production build — awaiting author scenes
**Started:** 2026-08-22
**Target length:** ~76,500 words / 17 chapters → ~250pp at 6"×9" (see `publishing.md`)

*(Title and subtitle are both provisional — the folder name is an ID, not a
commitment. See `writing-plan.md` §9 for title alternatives under
consideration.)*

## Logline

Every physician eventually stops noticing what's strange about medicine,
because almost everyone enters it knowing nothing else — the culture becomes
the water they swim in before they can compare it to anything. This book is
written from the narrow window before that happens: a medical student who
built and ran businesses first, still able to see the profession's assumptions
as *choices* — usually defended as patient safety, often actually serving
institutional incentives, inertia, or professional status — rather than as
facts about how medicine has to work.

## Why this vantage point, specifically

People who write books critiquing medicine are usually either lifelong
outsiders — journalists, patients, policy analysts — who never see how
incentives actually operate inside a hospital, or lifelong insiders trained
for a decade to experience the current structure as simply how good medicine
is practiced. Both write real books. Neither can write this one.

The angle here is the overlap: enough time inside training to know the
mechanisms (documentation and billing, how attendings are evaluated, what
"clinical judgment" actually selects for), plus enough time before it running
a business to notice when an argument defended as patient safety is an
incentive problem, a liability shield, or a status game wearing a lab coat.

That window closes — and the book knows it. Chapter 3 documents it closing in
real time: arriving with a founder's certainty that nobody is watching, and
discovering that in medicine everybody is, that he now "represented an
institution, a profession." The premise carries its own deadline.

## Working thesis

Medicine has internalized **scarcity as a virtue** — in testing, in data, in
access, in what patients are told about their own bodies — for reasons often
legitimate when established and mostly not now.

> Medicine treats **abundance of data** and **abundance of action** as the
> same category of risk. They are not. Information is cheap to gather, store,
> and analyze; intervention still carries real cost and risk. Collapsing the
> two into one "more is more dangerous" reflex is where the damage happens —
> and it is a trained reflex, not a law of nature.

Each chapter is a named instance of that pattern, argued from a concrete case.
The book ends where diagnosis becomes prescription: what he thinks should
change, and why.

**On vantage point:** this is narrated from the author's chair throughout — a
physician-builder in training. It is not a book of patient testimony. What is
patient-side is the *yardstick*: the test applied to every proposed change is
whether it would alter what medicine is actually like to be on the receiving
end of, rather than whether it moves a system metric. That's the standard the
argument is judged by, not a change of narrator.

## Structure

| Part | Chapters | Does |
| --- | --- | --- |
| One — The Vantage Point | 1–4 | Who's speaking, what they see, what they've gotten wrong, why they're speaking at all |
| Two — The Diagnosis | 5–10 | Misaligned incentives → scarcity as virtue → the steelman → the limits of reductionism → two reasoning tools |
| Three — Institutional Lag | 11–13 | The pattern tested against specific fights, including one where medicine is right |
| Four — Whom Medicine Serves | 14–17 | Disruption, money, motive, and what he thinks should actually change |

See `outline.md` for full chapter specs and `writing-plan.md` for drafting
order, the anecdote ledger, research gaps, and the definition of done.

## Relationship to the other books in this repo

- **Policy Patient** is the systems-and-index book — abstracted across many
  policies, aimed at a predictive tool. This book is one physician's specific,
  first-person case, grounded in training as lived rather than policy as
  studied. They rhyme (both are about incentive structures producing patient
  harm that looks accidental and isn't) without duplicating: this book can
  feed concrete human case material *to* Policy Patient's abstraction.
- **Providence** is the full-life autobiography. This book draws on the same
  Substack archive (`providence/substack-essays/`) but is scoped tightly to
  the medicine-and-building argument. 16 of ~51 essays are used here; that
  ratio is the discipline, not an oversight.

## Source material

Seed essays live in `providence/substack-essays/` and are **not duplicated
here** — `outline.md` maps each chapter to its source. A chapter is a
rewritten, expanded, book-length treatment of its seed, not a copy-paste;
`writing-plan.md` §4 covers how that expansion works. Chapter 17 has no seed
at all and carries the book's ending.

`reference/` holds material specific to this book: sources for the diagnosis
chapters, technology-adoption research, and any optional patient material
gathered later (`writing-plan.md` §6.1 — enrichment, not a requirement).

## Production build

`python3 build.py` compiles everything into `manuscript/`. It converts inline
bracketed citations into numbered endnotes, generates the Notes section
grouped by chapter, strips editorial draft notes into `production-notes.md`,
assembles front and back matter, and writes a single-file manuscript.

Working chapter files keep their draft notes. The build is regenerated from
scratch each run, so never edit inside `manuscript/` — edit the chapter file
and rebuild.

**Current build:** 19 chapters, 25 endnotes, 33,339 words, ~108 pages at
6"×9". One scene placeholder remains in the text. The build fails loudly on
any bracketed citation it could not convert, so nothing reaches a typesetter
as a bare source note.

## What is finished

- Author's note and epilogue, both complete
- All 17 chapters as continuous prose
- Front matter: half title, title page, copyright with a medical-advice
  disclaimer and de-identification statement, epigraph, contents
- Back matter: Notes by chapter, acknowledgments stub, about the author
- Citations converted to endnotes; every note either cites a real source or
  says plainly that it could not be verified
- Cross-chapter duplication resolved, verbatim and conceptual
- Mechanically clean: no double spaces, no trailing whitespace, straight
  apostrophes

## What is not finished

1. **The scenes.** See `scenes-needed.md` — nine of them, only the author can
   write them. This is the length gap and the quality gap simultaneously.
2. **Acknowledgments.** Stub only.
3. **ISBN, imprint, cover.** Cover cannot be commissioned until the final
   page count is known, which depends on the scenes.
4. **Four time-sensitive citations** flagged in-text as unverified for this
   edition: radiologist workforce projections, FDA autonomous-clearance
   status, psychiatry compensation and employment figures, and the Bervell
   anecdote. Each says so in the note rather than implying confidence.
5. **A full human read.** Nobody has read this end to end, including the
   author. It should happen after the scenes go in.
6. **Copyedit** by someone who is not the author or me.
