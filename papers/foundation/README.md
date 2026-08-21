# Paper I — Foundations / Fondamenti

Parallel sources:

- `it/main.tex`: Italian version
- `en/main.tex`: English version

Both versions share section/equation labels, audited claim IDs, and citation keys. Scientific changes must update both files in one commit.

## Build status

**NOT COMPILED LOCALLY**: current environment has no `pdflatex` or `latexmk`. Structural alignment is tested by `tests/test_paper_alignment.py`. CI must compile both versions before any PDF is described as passing.

Expected commands from each language directory:

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

Bibliography path is relative to repository `references/library.bib`. Generated PDFs and auxiliary files are not committed by default.

## Scientific status

Draft promotes only audited kinematic identities and explicitly retains `κ₀>0` as `UNPROVEN`. It does not define null, field, or vacuum sectors, derive dynamics, or claim an experimental bound.
