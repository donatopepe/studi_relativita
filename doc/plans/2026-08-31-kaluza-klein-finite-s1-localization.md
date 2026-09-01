# Finite `S1` source–probe localization implementation plan

> Direct MVP execution. User forbids subagents. Recon and closure review are direct and labeled `DIRECT_RECON_NO_SUBAGENT` / `DIRECT_REVIEW_NO_SUBAGENT`; neither is independent review.

**Objective:** Determine whether wrapped-Gaussian source/probe widths are separately identifiable from existing point and radial-shell tidal matrices.

**Metric:** all ten preregistered controls pass (`10/10`) before accepting result.

**MVP:** extend existing scalar compact-circle module with wrapped-Gaussian coefficients and one radial-shell path. No general profile framework, oriented-box rerun, tensor/radion/localization dynamics, detector, or data.

**Worktree:** `/home/public/studi_relativita/.worktrees/kaluza-klein-next-control`

## Task 1 — Freeze source contract test-first

**Files**
- Modify: `doc/specs/2026-08-31-kaluza-klein-finite-s1-localization.md`
- Create: `tests/test_kaluza_klein_finite_s1_sources.py`
- Modify: `references/library.bib`
- Modify: `references/verification-log.md`

1. Write failing source tests requiring `NISTDLMF` metadata, DOI `10.18434/M3167`, release `1.2.7`, DLMF equations `(1.8.14)` and `(20.2.3)`, and strict exclusions.
2. Preserve RED.
3. Add verified bibliography/log entry using DLMF citation guidance and inspected equation permalinks.
4. Run GREEN and commit.

## Task 2 — Define ten controls RED

**Files**
- Create: `tests/test_kaluza_klein_finite_s1_localization.py`

Write one test per preregistered control:

1. wrapped-profile normalization;
2. direct-quadrature Fourier coefficient conformance;
3. localized limit;
4. broad finite-width and exact-uniform distinction;
5. periodicity;
6. orientation-sign collision/conjugation;
7. source–probe exchange;
8. equal-combined-width collision;
9. joint dilation and shell zero-width;
10. local rank/null directions and global collision labels.

Require raw complex coefficients, combined overlaps, static weights, point matrix, shell matrix, convergence certificate, classifications, physical gate, and all negative statuses. Run missing-API RED and commit tests.

## Task 3 — Implement smallest wrapped-Gaussian extension

**Files**
- Modify: `studies/spacetime/kaluza_klein_linearized_tidal.py`
- Modify only if compatibility demands isolation: create `studies/spacetime/kaluza_klein_finite_s1_localization.py`

Prefer direct extension. Implement:

- normalized wrapped-Gaussian image sum for independent quadrature/reference;
- analytic source/probe complex coefficients;
- exact localized/uniform preparation records;
- combined complex overlap and static real weights;
- mode-sum potential derivatives and raw point Hessian;
- radial-shell average using existing convention;
- mode convergence;
- ten controls, scale/rank diagnostics and statuses.

Do not alter old `build_result()` output except through backward-compatible helpers. Run focused GREEN and commit.

## Task 4 — Deterministic artifact and bilingual authority

**Files**
- Create: `studies/spacetime/kaluza-klein-finite-s1-localization-results.json`
- Create: `audit/kaluza-klein-finite-s1-localization-report-en.md`
- Create: `audit/kaluza-klein-finite-s1-localization-report-it.md`
- Create: `theory/spacetime/kaluza-klein-finite-s1-localization.md`
- Create: `tests/test_kaluza_klein_finite_s1_reports.py`
- Modify: `docs/roadmap.md`
- Modify only as required by schema: unified claims/assumptions/equations and their completeness tests.

1. Write report/authority tests RED.
2. Generate `.8g` stable artifact, canonicalizing only `abs(value)<1e-7`.
3. Record exactly ten controls and `10/10` metric.
4. Keep EN/IT tokens, equations and numeric values aligned.
5. Preserve previous KK result and `F_0`; classify this increment as model-level negative identifiability result.
6. Run GREEN and commit.

## Task 5 — Direct review and full verification

1. Record `DIRECT_REVIEW_NO_SUBAGENT`.
2. Mechanically compare reports to JSON and verify source scopes.
3. Re-attack all ten controls, especially direct quadrature independence, conjugation versus static collision, equal-`u` collision, shell limit and rank nulls.
4. Run:

```bash
python3 -m py_compile <touched Python files>
python3 -m unittest discover -s tests -p 'test_kaluza_klein_finite_s1*.py' -v
python3 -m unittest discover -s tests -v
python3 studies/spacetime/kaluza_klein_finite_s1_localization.py --check
python3 studies/spacetime/kaluza_klein_linearized_tidal.py --check
python3 tools/extract_docx.py --check
python3 tools/inventory_source.py --check
python3 studies/free-fall-identifiability/analysis.py --check
git diff --check
git status --short
```

GitHub `latex` job is authoritative if local LaTeX is unavailable.

## Task 6 — Conservative PR and finish

1. Push exact clean SHA and open PR with source scope, `10/10`, full-suite evidence and no-evidence guardrails.
2. Require exact-SHA `tests` and `latex` success.
3. Write Hermes Inbox note.
4. Auto-merge only if diff remains conservative/unambiguous, every local/CI check is green, and no source/gauge ambiguity emerged.
5. Verify post-merge main CI, update main, clean worktree/branch, and cancel loop.
6. If any ambiguity emerges, leave PR open, cancel loop and request human review.
