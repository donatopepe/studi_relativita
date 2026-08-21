# UMCH Initial Repository and Audit Implementation Plan

> **Spec:** `doc/specs/2026-08-21-universal-minimum-curvature-hypothesis.md`

**Goal:** Deliver the initial UMCH repository foundation, loss-aware source extraction, complete claim/equation inventory, verified starter bibliography, foundational audit framework, bilingual Paper I skeleton, and one reproducible experimental-bound study or documented no-bound result.

**Architecture:** Treat the immutable DOCX as source evidence. Deterministic Python tooling extracts and inventories it into stable-ID artifacts. Human-reviewed Markdown/CSV records feed bilingual LaTeX papers. Automated tests validate provenance, schemas, bilingual alignment, references, and reproducibility. Work advances in small commits and pushes to `origin/paper-scientifico` after each verified milestone.

**Tooling:** Python 3 standard library first; `pytest` only if available or added with pinned development requirements; Markdown, CSV, BibTeX, LaTeX; GitHub Actions for checks that do not require unavailable local binaries.

## Operating rules

- Work only in `/home/public/studi_relativita/.worktrees/paper-scientifico` on branch `paper-scientifico`.
- Read approved spec before each milestone.
- Never fabricate references, calculations, experimental bounds, or review outcomes.
- Preserve original text separately from normalized and translated text.
- Mark incomplete scientific work `UNREVIEWED` or `UNPROVEN`.
- Run scoped tests before each commit and full available suite before each push.
- Update `/home/public/HermesVault/Memory/UMCH - Ipotesi Curvatura Minima Universale.md` after every verified milestone.
- Push only committed, verified work to `origin/paper-scientifico`; never force-push.
- Stop and record blocker when credentials, source verification, or scientific judgment is unavailable.

## Task 1: Repository policy and public entry points

**Create:**
- `.gitignore`
- `README.md`
- `README.en.md`
- `LICENSE`
- `CITATION.cff`
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `docs/ai-assistance.md`

**Checks:**
1. Add a script/test that verifies required files, author metadata, CC BY 4.0 notice, reciprocal language links, hypothesis status, and explicit falsifiability warning.
2. Run check and observe failure before files exist.
3. Create concise equivalent Italian/English entry points and policy files.
4. Run check; expect success.
5. Commit: `docs: establish UMCH public project foundation`.

## Task 2: Preserve source and record provenance

**Move:**
- `Dimostrazione e Prove Relatività Einstein.docx` → `archive/original/Dimostrazione e Prove Relatività Einstein.docx`

**Create:**
- `archive/provenance.md`
- `archive/original/SHA256SUMS`
- `tests/test_provenance.py`

**Checks:**
1. Test requires one source file, valid SHA-256, matching checksum, source commit, extraction caveat, and AI-origin caveat.
2. Run failing test.
3. Move with `git mv`; compute checksum; document provenance without changing bytes.
4. Run test and compare blob/checksum.
5. Commit: `archive: preserve original source with provenance`.

## Task 3: Build deterministic DOCX extraction

**Create:**
- `tools/extract_docx.py`
- `archive/extracted/document-it.md`
- `archive/extracted/extraction-manifest.json`
- `tests/test_extract_docx.py`

**Checks:**
1. Fixtures or source-based tests require ordered paragraph IDs `UMCH-SRC-P0001...`, heading levels, exact text runs, hyperlinks where recoverable, empty equation-bearing paragraphs, source checksum, tool version, counts, and deterministic output.
2. Run failing tests.
3. Implement standard-library ZIP/XML extraction without semantic corrections.
4. Generate extracted Markdown and manifest.
5. Re-run extraction and assert zero diff; run tests.
6. Commit: `feat: add deterministic source extraction`.

## Task 4: Inventory claims and equations

**Create:**
- `tools/inventory_source.py`
- `audit/claims.csv`
- `audit/equations/equations.csv`
- `audit/inventory-summary.json`
- `audit/README.md`
- `tests/test_audit_schema.py`
- `tests/test_inventory.py`

**Checks:**
1. Define exact CSV schemas from spec, stable IDs, controlled claim types/statuses, source paragraph links, and nonempty decision fields only after review.
2. Tests initially fail for absent artifacts.
3. Implement conservative inventory: uncertain classifications stay `UNREVIEWED`; formula candidates are captured, not declared valid.
4. Generate complete source inventory and summary counts.
5. Validate all source paragraphs are represented or explicitly excluded with reason; rerun deterministically.
6. Commit: `feat: inventory source claims and equations`.

## Task 5: Establish theory vocabulary and contradiction tracking

**Create:**
- `theory/definitions.md`
- `theory/assumptions.md`
- `theory/notation.md`
- `theory/limiting-cases.md`
- `theory/open-problems.md`
- `audit/contradiction-log.md`
- `docs/glossary-it.md`
- `docs/glossary-en.md`
- `tests/test_theory_docs.py`

**Checks:**
1. Test requires distinct definitions for spacetime curvature, geodesic curvature, proper acceleration, timelike/null curves, field observables, and vacuum observables; it also requires unit declarations and `κ₀→0` cases.
2. Run failing test.
3. Write conservative definitions grounded in standard geometry; label proposed extensions as conjectures.
4. Ensure bilingual glossary keys align.
5. Run tests.
6. Commit: `docs: define UMCH vocabulary and assumptions`.

## Task 6: Verify starter bibliography

**Create:**
- `references/library.bib`
- `references/verification-log.md`
- `tests/test_bibliography.py`

**Procedure and checks:**
1. Test validates unique citation keys, required metadata, DOI/arXiv syntax, and a verification-log entry per citation.
2. Add only primary sources or authoritative reviews whose metadata and claim relevance were checked against publisher, DOI, arXiv, or institutional pages.
3. Record access date, canonical URL, exact supported topic, and verification status. Do not infer a source from the DOCX wording.
4. Run tests.
5. Commit: `research: add verified foundational bibliography`.

## Task 7: Audit foundational geometric claims

**Create:**
- `audit/audit-report-it.md`
- `audit/audit-report-en.md`
- `audit/dimensional-analysis/foundations.md`
- `tests/test_foundation_audit.py`

**Modify:**
- `audit/claims.csv`
- `audit/equations/equations.csv`
- `audit/contradiction-log.md`

**Checks:**
1. Select all load-bearing claims about `κ`, `κ₀`, Frenet–Serret frames, geodesics, proper acceleration, covariance, and momentum norm.
2. For each, record premises, derivation/source, dimensions, standard-theory comparison, status, and rationale.
3. Independently derive the timelike candidate definition and expose its consequence for geodesic motion.
4. Keep any unresolved claim `UNPROVEN`; record contradictions explicitly.
5. Test requires no selected foundational claim remains `UNREVIEWED`, bilingual reports reference identical claim IDs, and status values are valid.
6. Commit: `research: audit foundational geometric claims`.

## Task 8: Draft bilingual Paper I

**Create:**
- `papers/foundation/it/main.tex`
- `papers/foundation/en/main.tex`
- shared LaTeX support files only where duplication is mechanical
- `papers/foundation/README.md`
- `tests/test_paper_alignment.py`

**Checks:**
1. Tests require matching labeled sections/equations/claims/citations across languages and prohibit promotion of `UNPROVEN`/`UNREVIEWED` claims as results.
2. Run failing test.
3. Draft title, abstract, definitions, hypothesis, standard-theory tension, limiting cases, falsification criteria, results limited to audited material, limitations, AI disclosure, and bibliography.
4. Run structural tests. Compile PDFs when a TeX engine is available; otherwise CI must compile and local status must say `NOT COMPILED`.
5. Commit: `paper: draft bilingual UMCH foundations manuscript`.

## Task 9: Implement first experimental-bound study

**Create:**
- `studies/<selected-observable>/README.md`
- `studies/<selected-observable>/analysis.py`
- `studies/<selected-observable>/inputs.*`
- `studies/<selected-observable>/results.json`
- `studies/<selected-observable>/report-it.md`
- `studies/<selected-observable>/report-en.md`
- `tests/test_first_bound.py`

**Decision gate:** Select observable only after Paper I establishes which measured quantity is related to `κ₀`. Prefer transparent published free-fall/proper-acceleration data over a more sensitive but model-dependent dataset.

**Checks:**
1. Write tests for units, deterministic result, source metadata, uncertainty handling, and a known synthetic case.
2. Run failing tests.
3. Implement smallest defensible inference.
4. If no valid mapping from observable to `κ₀` exists, publish a reproducible no-bound result explaining missing assumption instead of inventing a bound.
5. Run tests and regenerate results from clean inputs.
6. Commit: `research: evaluate first experimental constraint`.

## Task 10: CI, roadmap, and milestone verification

**Create:**
- `.github/workflows/verify.yml`
- `docs/overview-it.md`
- `docs/overview-en.md`
- `docs/roadmap.md`
- `docs/falsification.md`
- development dependency/config files only if needed

**Checks:**
1. CI runs all Python tests, deterministic artifact checks, Markdown/link checks, bibliography checks, bilingual alignment, and LaTeX build where configured.
2. Run complete local suite and `git diff --check`.
3. Verify README links, citation metadata, license, generated artifacts, and clean Git status.
4. Update Hermes/Obsidian note with milestone status, key findings, blockers, branch, and latest commit.
5. Push `paper-scientifico` to GitHub and verify remote SHA equals local SHA.
6. Commit any final doc-only status update: `docs: record initial milestone status`.

## Full verification commands

Exact commands may be refined when Task 1 establishes tooling. Baseline:

```bash
cd /home/public/studi_relativita/.worktrees/paper-scientifico
python3 -m unittest discover -s tests -v
python3 tools/extract_docx.py --check
python3 tools/inventory_source.py --check
git diff --check
git status --short --branch
```

If `pytest` is intentionally added and pinned, use:

```bash
python3 -m pytest -q
```

PDF compilation is required in CI before claiming PDFs pass, even when local TeX is unavailable.

## Loop completion condition

Recurring work loop stops itself when all Task 1–10 acceptance criteria pass, branch is pushed, remote SHA matches local SHA, Hermes note is current, and no unresolved implementation blocker remains. Scientific `UNPROVEN` or `CONTRADICTED` results do not block completion when correctly documented.
