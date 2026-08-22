# Substack Essays

Essays imported from Substack. Unlike `reference/journal-entries/` (raw
private source material this book gets built from), these are already
published, finished pieces — they may get pulled into chapters directly,
referenced, or stand alongside the chapters as-is.

## Naming

`{substack-post-id}.{slug}.md` — e.g. `189806602.why-i-write-this.md`.

The raw upload came as HTML exports with no publish-date metadata attached
(no `<time>` tag, nothing in the filename but Substack's internal post ID
and URL slug), so files are **not** dated `YYYY-MM-DD-title.md` the way the
original plan called for. The post ID is a reasonable proxy for chronological
order — Substack assigns it sequentially — so sorting filenames roughly
sorts by publish order, just without real dates attached.

If you have the real publish dates (from Substack's own export/analytics, or
just memory), renaming these to `YYYY-MM-DD-title.md` would be a welcome
follow-up — nothing here depends on the current naming.

## Titles

Each file's `# ` heading is the essay title, recovered from the post's own
first heading when it had one, otherwise guessed from the URL slug (title-
cased, hyphens to spaces). The slug is Substack's own, occasionally
auto-generated or truncated — a few titles are visibly rough because of
this (e.g. one file's slug was just `b02`; its real title, `Refunding
$1,100 Hurt, and Here's Why`, was recovered from a heading inside the post).
Where the guess looks off, fixing the `#` line by hand is fine — nothing
depends on the filename matching the title exactly.

## Conversion notes

Converted from Substack's raw HTML export: paragraphs, bold/italic, links,
lists, blockquotes, and inline images preserved; embedded "Subscribe" widget
forms/buttons/icons stripped as non-content.

Three posts came through with **no body content** in the original upload
(the export was just an empty paragraph) — they're kept as stub files with
a note instead of being silently dropped, so the gap stays visible:

- `166865425.everyone-should-build-something-even.md`
- `174587269.parenting-not-policy-is-the-real.md`
- `205090112.470.md`

These need re-exporting from Substack and re-pasting in if that content
still matters.
