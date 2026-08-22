# Books

Every book I write lives here as a folder. Chapters are markdown files. Drafts
have a commit history, revisions have diffs, and a finished book is just a
directory that stopped changing.

## Layout

```
Books/
├── _template/                  # copy this to start a new book
├── providence/                 # autobiography, built from journal entries
│   ├── README.md               # title, logline, status, word count
│   ├── outline.md              # structure, beats, what each chapter does
│   ├── 01-chapter-title.md
│   ├── 02-chapter-title.md
│   ├── ...
│   └── reference/              # research, interviews, sources, images
├── policy-patient/              # nonfiction, health policy + patient harm
└── not-yet-captured/            # physician-in-training's case against medicine's scarcity mindset
```
```

## Conventions

- **One folder per book**, named in `kebab-case` after the working title. The
  working title can change without renaming the folder — the folder is an ID,
  the title lives in `README.md`.
- **One file per chapter**, prefixed with a zero-padded number so they sort in
  reading order: `01-`, `02-`, … `10-`. Front matter chapters get `00-`.
- **Renumbering is a rename**, not a rewrite. Use `git mv` so history follows
  the chapter.
- **Write chapters as normal prose** — flowing paragraphs, the way a book
  actually reads. Don't break sentences onto separate lines; that makes for
  tidy diffs and unreadable drafts, and the draft is the thing that matters.
  Planning files (outlines, notes, this README) can use whatever structure
  helps.
- **Reference material** — research notes, source PDFs, transcripts, cover
  art — goes in `reference/` so the top level of a book folder is only the
  book itself.
- **Nothing outside a book folder** except this README and `_template/`.

## Starting a new book

```sh
cp -r _template the-new-book
cd the-new-book
# fill in README.md, sketch outline.md, rename 01-chapter-title.md
```

## Status vocabulary

Each book's `README.md` carries a status. In order:

| Status | Meaning |
| --- | --- |
| `outlining` | Structure exists, prose doesn't |
| `drafting` | Writing forward, not looking back |
| `revising` | Full draft exists, now it gets good |
| `final` | Done. Only typo fixes from here |
| `published` | Out in the world — see the book's README for where |
| `shelved` | Set down deliberately, not abandoned |
