# Paper II Comparative Classical Dynamics Implementation Plan

> Spec: `doc/specs/2026-08-21-paper-ii-classical-dynamics.md`

## Goal

Produce a bilingual, reproducible comparative/no-go analysis of a hard pointwise curvature constraint, a barrier curvature action, and a separately labeled coarse-grained alternative. Do not claim viability beyond tested scope.

## Task 1 — Verify classical-dynamics literature

Create canonical BibTeX entries and verification-log sections for Arreaga–Capovilla–Guven, Capovilla–Guven–Rojas, and Nesterenko et al. Add tests for required citation keys and support/limit statements. Commit after full suite.

## Task 2 — Define candidate schemas and decision matrix

Test-first create candidate documents and `theory/classical-dynamics/decision-matrix.csv`. Schema must record domain, action, analysis level, differential order, constraints, standard limit, observable, evidence, state, and blocking issue. All unevaluated cells remain `INCOMPLETE`.

## Task 3 — Hard-constraint variational audit

Document proper-time/reparametrization conventions, KKT sign convention, feasibility, active/inactive branches, nonsmooth boundary, initial-data implications, and conditional equivalence tension. Add deterministic algebra/schema checks; do not infer a full Dirac classification without derivation.

## Task 4 — Barrier candidate audit

Choose one explicit dimensionally consistent representative and declare coupling dimensions. Derive asymptotic behavior and derivative order at variational level. Add symbolic checks for barrier divergence, dimensions, and `κ₀→0` under each declared scaling. Treat stability as unresolved unless constrained Hamiltonian analysis proves it.

## Task 5 — Separate coarse-grained alternative

Define averaging window, scalar observable, covariance/operational questions, and non-equivalence to pointwise UMCH. Ensure tests and paper label it `ALTERNATIVE_HYPOTHESIS`.

## Task 6 — Comparative audit reports

Create bilingual reports and dimensional-analysis artifact. Populate decision matrix only from Tasks 3–5 evidence. Use `NO_GO_CONDITIONAL`, `INCOMPLETE`, or other specified states precisely.

## Task 7 — Bilingual Paper II draft

Create aligned Italian/English LaTeX with matching labels, citations, candidate states, limitations, stop rules, and AI disclosure. Extend CI to compile Paper II. Never promote `UNPROVEN` or `INCOMPLETE` to result.

## Task 8 — Verification and PR

Run full unit suite, all existing generator checks, new deterministic checks, `git diff --check`, and CI. Update roadmap/overviews only with verified outcomes. Update Hermes. Remove this ephemeral plan, push branch, verify SHA, open PR for human scientific review. Do not auto-merge.

## Canonical local verification

```bash
python3 -m unittest discover -s tests -v
python3 tools/extract_docx.py --check
python3 tools/inventory_source.py --check
python3 studies/free-fall-identifiability/analysis.py --check
git diff --check
```
