# Publishing plan — Amazon KDP

Target: a 200–300 page paperback, self-published through KDP.

## Trim size and the page math

**Trim: 6" × 9"** — the default for serious nonfiction, and what a reader
expects this book to look like on a shelf next to other health-policy and
medicine titles. KDP stocks it, it's the cheapest per-page tier for its size,
and it holds more words per page than 5.5" × 8.5", which matters because the
alternative would push the word count higher for the same spine.

Interior spec used for all estimates below:

| Setting | Value |
| --- | --- |
| Trim | 6" × 9" |
| Body font | 11pt serif (Garamond, Minion, or EB Garamond) |
| Leading | ~1.25 |
| Margins | 0.75" outside/top/bottom, gutter per KDP for page count |
| Words per page | **~310** (planning figure) |

That yields:

| Word count | Approx. pages | Verdict |
| ---: | ---: | --- |
| 59,500 | ~192 | Below target — the original plan |
| 70,000 | ~226 | Acceptable, thin end |
| **76,500** | **~247** | **Target — middle of range** |
| 90,000 | ~290 | Top of range |

Add front and back matter (below) for roughly **+18 pages**, landing the book
near **265 pages**. That sits comfortably inside 200–300 with room to lose or
gain a chapter without blowing the target.

**Sensitivity:** words-per-page is the soft number here. At 280 wpp the book
runs ~273pp of body text; at 340 wpp, ~225pp. Both stay in range, which is
why 76,500 is the right target rather than something closer to either edge.
Re-measure against a real typeset proof before trusting any of this — set one
chapter in the actual template and count.

## Front and back matter

Front (~6 pages):
- Half title, title page, copyright
- Epigraph — the Asaf ud-Daulah build-and-destroy parable (see `outline.md`)
- Contents
- Author's note on vantage point: written during medical training, from one
  chair, deliberately. Fixes the narration-timepoint question in the reader's
  mind before Chapter 1 rather than leaving it ambiguous.

Back (~12 pages):
- Notes, by chapter. Not academic footnotes — sourced claims with citations,
  which is what keeps the book from reading as a blog compilation (see
  `writing-plan.md` §8, risk 4).
- Acknowledgments
- About the author

No index. Indexing is expensive, slow, and rarely worth it for a
narrative-argument book at this length.

## KDP specifics to settle before upload

- **ISBN.** KDP offers a free one, but it lists Amazon as publisher and can't
  be used elsewhere. Buying an ISBN (Bowker, US) keeps the book portable to
  other retailers and lists the author as publisher. Recommended if there's
  any intention of wider distribution.
- **Categories.** Two at upload, expandable to ten by request. Likely:
  Medical > Health Care Delivery; Business & Money > Industries > Healthcare;
  Political Science > Public Policy > Social Policy.
- **Keywords.** Seven slots. Draft them from the book's actual argument
  (scarcity mindset, medical training, physician entrepreneur, healthcare
  incentives, overdiagnosis, health technology adoption) rather than guessing
  at volume.
- **Cover.** Needs a real designer. The spine width depends on final page
  count and paper type — do not commission until the manuscript is locked.
- **Paper.** Cream stock for a text-heavy book; white reads clinical and is
  better suited to books with figures.
- **Price.** Set after page count is final — KDP's printing cost scales with
  it, and royalty math depends on the 70% vs 35% band.

## Manuscript conventions for KDP

These are decisions that are cheap now and expensive to retrofit:

- One chapter per file, already the repo convention. Compile at the end.
- Chapter titles only — no "Chapter One" labels above them.
- Scene breaks marked with a centered typographic break, not a blank line
  (blank lines vanish across page breaks).
- No em-dash reformatting at typeset time. The author uses them heavily and
  deliberately; see `writing-plan.md` §7.
- Straight quotes in the source files; let the typesetting pass curl them
  once, globally.
- Every sourced claim carries its citation in the draft, inline in brackets,
  and gets moved to the Notes section during the compile pass. Chasing
  citations after the fact is how books lose months.

## Sequence

1. Draft all chapters (see `writing-plan.md` §2 for order)
2. Full revision pass — throughline, anecdote collisions, bridges
3. Compile to one manuscript; move inline citations to Notes
4. Copyedit
5. Typeset one chapter, measure real words-per-page, confirm the page target
6. Typeset the whole; commission cover against final spine width
7. Proof copy from KDP, read on paper, fix
8. Publish
