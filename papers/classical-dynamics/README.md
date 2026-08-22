# Paper II — Classical dynamics / Dinamica classica

- `it/main.tex`: Italian source
- `en/main.tex`: English source

Both versions share section/equation labels, citations, candidate states, and downstream gate. Scientific edits must update both.

## Build status

**NOT COMPILED LOCALLY**: local environment lacks TeX. GitHub Actions compiles both languages and uploads PDFs. No PDF is claimed passing until CI is green.

Expected command in each language directory:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Scientific status

A/B remain `INCOMPLETE`; C is `NON_IDENTIFIABLE` and `ALTERNATIVE_HYPOTHESIS`; `κ₀>0` remains `UNPROVEN`; `NO_GO_NOT_ESTABLISHED`. Paper III remains scientifically deferred.
