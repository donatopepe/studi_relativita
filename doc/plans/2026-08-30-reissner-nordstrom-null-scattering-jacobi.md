# Reissner–Nordström null-scattering Jacobi implementation plan

> Execution is direct in the current session because the user explicitly forbids subagents. Use the isolated worktree `/.worktrees/reissner-nordstrom-null-scattering` and preserve TDD evidence.

## Task 1 — Freeze scientific and source contracts

**Files**
- Modify: `references/library.bib`
- Modify: `references/verification-log.md`
- Create: `tests/test_reissner_nordstrom_null_scattering_sources.py`

1. Add failing tests requiring dedicated verified source headings and narrow scope disclaimers.
2. Run `python3 -m unittest tests.test_reissner_nordstrom_null_scattering_sources` and retain RED output.
3. Add canonical metadata for Eiroa–Romero–Torres (2002), DOI `10.1103/PhysRevD.66.024010`, arXiv `gr-qc/0203049`; document exact supported equations and exclusions.
4. Re-run to GREEN and commit.

## Task 2 — Define counterexample-first numerical contract

**Files**
- Create: `tests/test_reissner_nordstrom_null_scattering_jacobi.py`

Add tests before production code for domain validation, path branches, direct optical matrix symmetry, nonzero Ricci trace at charge, Schwarzschild limit, sign collision, orientation similarity, zero window, symplectic/reversal/composition, graph guard, dilation and rank-null direction. Run focused test and retain import/file failure as RED. Commit tests.

## Task 3 — Implement minimal direct-curvature phase map

**Files**
- Create: `studies/spacetime/reissner_nordstrom_null_scattering_jacobi.py`
- Create: `studies/spacetime/reissner-nordstrom-null-scattering-jacobi-results.json`

Implement RN metric and analytic Christoffels (or a deterministic metric-derivative Riemann implementation), regularized path, declared screen, direct Riemann projection, RK4 full map, controls and deterministic serialization. Reuse generic matrix helpers only where their conventions are explicit. Preserve raw matrices and separate trace/trace-free diagnostics. Run focused suite until GREEN. Generate and deterministically compare JSON. Commit.

## Task 4 — Add bilingual authoritative audit

**Files**
- Create: `audit/reissner-nordstrom-null-scattering-jacobi-report-en.md`
- Create: `audit/reissner-nordstrom-null-scattering-jacobi-report-it.md`
- Create: `theory/spacetime/reissner-nordstrom-null-scattering-jacobi.md`
- Create: `tests/test_reissner_nordstrom_null_scattering_reports.py`
- Modify: `docs/roadmap.md`

Write tests requiring semantic EN/IT alignment for equations, labels, status/gate, numerical baseline, limitations and source scope. Run RED, write reports/theory/roadmap, run GREEN. State charge-shape result and absolute-scale blindness without converting RN charge into `ell0`. Commit.

## Task 5 — Verify and ship conservatively

1. Run focused RN suites.
2. Run cross-control Schwarzschild/Jacobi suites.
3. Run `python3 -m unittest discover -s tests`.
4. Run artifact render/check, `tools/extract_docx.py --check`, `tools/inventory_source.py --check`, and `git diff --check`.
5. Perform direct bilingual/source/numerical closure review and record `DIRECT_REVIEW_NO_SUBAGENT`; do not call it independent review.
6. Push branch, open PR and wait for `tests` and `latex` jobs.
7. Auto-merge only if changes remain conservative and all checks are green. Otherwise leave PR open.
8. After merge, verify post-merge CI, write a new timestamped Hermes Inbox note, update main, remove worktree/branches, and retain durable loop `16588751` because no structural dead end is declared.
