#!/usr/bin/env python3
"""Compile the manuscript for production.

Takes the working chapter files and produces a press-ready build:

  - inline bracketed citations become numbered endnote markers
  - a Notes section is generated, grouped by chapter
  - draft footers are stripped from chapter text and preserved separately
  - front and back matter are assembled
  - everything is concatenated into one manuscript file

Working files are left intact. Everything written goes to manuscript/.
Run from the book directory: python3 build.py
"""

import re
import glob
import os
import shutil

BOOK = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BOOK, "manuscript")

# Bracketed spans that are citations rather than prose. A citation bracket
# starts with a capital and runs long; scene markers and editorial asides are
# handled separately so they never silently become endnotes.
CITE = re.compile(r'\[((?:Cite: )?[A-Z][^\]]{20,})\]', re.S)

CHAPTER_TITLES = {}


def split_body(text):
    """Return (body, draft_note). Draft notes are editorial, not book text."""
    if "\n*[Draft" in text:
        i = text.index("\n*[Draft")
        return text[:i].rstrip(), text[i:].strip()
    return text.rstrip(), ""


def process_chapter(path, counter_start):
    raw = open(path).read()
    body, draft_note = split_body(raw)

    title_match = re.match(r'#\s+(.+)', body)
    title = title_match.group(1).strip() if title_match else os.path.basename(path)

    notes = []
    n = counter_start

    def repl(m):
        nonlocal n
        content = m.group(1).strip()
        # Scene placeholders are not citations; leave them for the human pass.
        if content.upper().startswith("SCENE NEEDED"):
            return m.group(0)
        content = re.sub(r'^Cite:\s*', '', content)
        n += 1
        notes.append((n, content))
        return f'[^{n}]'

    body = CITE.sub(repl, body)
    return title, body, notes, draft_note, n


def scene_placeholder(body):
    """Render any remaining SCENE NEEDED marker as a clean production block."""
    def repl(m):
        return ("\n> **[ SCENE TO BE ADDED ]**\n>\n> "
                + m.group(1).replace("\n", " ").strip()
                + "\n")
    return re.sub(r'\[SCENE NEEDED —?\s*([^\]]+)\]', repl, body, flags=re.S)


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)

    files = sorted(glob.glob(os.path.join(BOOK, "[0-9][0-9]-*.md")))
    counter = 0
    all_notes = []          # (chapter_title, [(n, text), ...])
    draft_notes = []        # (filename, note)
    compiled = []

    for path in files:
        title, body, notes, dnote, counter = process_chapter(path, counter)
        body = scene_placeholder(body)
        base = os.path.basename(path)
        with open(os.path.join(OUT, base), "w") as f:
            f.write(body + "\n")
        compiled.append((base, title, body))
        if notes:
            all_notes.append((title, notes))
        if dnote:
            draft_notes.append((base, dnote))

    # --- Notes section -----------------------------------------------------
    lines = ["# Notes", "",
             "Sources are given by chapter. Where a claim could not be verified "
             "against a primary source, the note says so rather than implying "
             "a confidence the evidence does not support.", ""]
    for title, notes in all_notes:
        lines.append(f"## {title}")
        lines.append("")
        for n, text in notes:
            lines.append(f"[^{n}]: {text}")
            lines.append("")
    with open(os.path.join(OUT, "90-notes.md"), "w") as f:
        f.write("\n".join(lines).rstrip() + "\n")

    # --- Preserved draft notes (not part of the book) ----------------------
    dn = ["# Draft notes (not for publication)", "",
          "Per-chapter editorial notes stripped from the manuscript during "
          "the production build. Kept so the reasoning behind each chapter "
          "isn't lost.", ""]
    for base, note in draft_notes:
        dn.append(f"## {base}")
        dn.append("")
        dn.append(note)
        dn.append("")
    with open(os.path.join(BOOK, "production-notes.md"), "w") as f:
        f.write("\n".join(dn).rstrip() + "\n")

    # --- Single-file manuscript -------------------------------------------
    front = []
    for name in ("00a-half-title.md", "00b-title-page.md", "00c-copyright.md",
                 "00d-epigraph.md", "00e-contents.md"):
        p = os.path.join(BOOK, "frontmatter", name)
        if os.path.exists(p):
            front.append(open(p).read().rstrip())

    back = []
    back.append(open(os.path.join(OUT, "90-notes.md")).read().rstrip())
    for name in ("91-acknowledgments.md", "92-about-the-author.md"):
        p = os.path.join(BOOK, "backmatter", name)
        if os.path.exists(p):
            back.append(open(p).read().rstrip())

    parts = front + [b for _, _, b in compiled] + back
    manuscript = "\n\n\\newpage\n\n".join(parts)
    with open(os.path.join(OUT, "not-yet-captured-manuscript.md"), "w") as f:
        f.write(manuscript + "\n")

    # --- Validation --------------------------------------------------------
    # Anything still in square brackets that isn't a footnote marker, a link,
    # or the scene block is a citation the converter missed. Fail loudly:
    # a bare [Cite: PMC1234567] shipping to a typesetter is how notes get lost.
    leftover = []
    for base, _, body in compiled:
        for m in re.finditer(r'\[(?!\^)([^\]]*)\]', body):
            frag = m.group(1)
            if frag.startswith("[ SCENE") or frag.startswith(" SCENE"):
                continue
            if body[m.end():m.end() + 1] == "(":   # markdown link
                continue
            leftover.append((base, frag[:70]))

    # --- Report ------------------------------------------------------------
    words = sum(len(b.split()) for _, _, b in compiled)
    scenes = sum(b.count("[ SCENE TO BE ADDED ]") for _, _, b in compiled)
    print(f"chapters compiled : {len(compiled)}")
    print(f"endnotes generated: {counter}")
    print(f"body word count   : {words:,}")
    print(f"est. pages @310wpp: {round(words/310)}")
    print(f"scene placeholders: {scenes}")
    print(f"draft notes moved : {len(draft_notes)}")
    print(f"output            : manuscript/")
    if leftover:
        print(f"\nUNCONVERTED BRACKETS ({len(leftover)}) — these will not become notes:")
        for base, frag in leftover:
            print(f"  {base}: [{frag}]")


if __name__ == "__main__":
    main()
