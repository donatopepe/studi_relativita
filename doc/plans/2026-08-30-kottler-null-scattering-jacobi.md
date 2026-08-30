# Kottler null-scattering Jacobi implementation plan

> Direct execution in current session. User forbids subagents. Use isolated worktree `/.worktrees/kottler-null-scattering`; preserve RED/GREEN evidence and classify review as `DIRECT_REVIEW_NO_SUBAGENT`.

## Task 1 — Freeze source and scientific contracts

**Files**
- Modify: `doc/specs/2026-08-30-kottler-null-scattering-jacobi.md`
- Modify: `references/library.bib`
- Modify: `references/verification-log.md`
- Create: `tests/test_kottler_null_scattering_sources.py`

1. Record bounded implementation authorization from repeated autonomous-loop instruction.
2. Add failing source tests requiring Rindler–Ishak metadata, equations `(1)`, `(2)`, `(7)`, and strict exclusions.
3. Run focused source test and preserve RED.
4. Add canonical bibliography and narrow verification-log entry.
5. Re-run GREEN and commit.

## Task 2 — Define counterexample-first numerical contract

**Files**
- Create: `tests/test_kottler_null_scattering_jacobi.py`

Write tests before production code for static-patch domain, turning path, screen/Riemann conformance, nonzero spacetime Ricci with vanishing null Ricci optical trace, `alpha=0` Schwarzschild limit, pure-de-Sitter analytic null-focusing control, zero window, orientation reversal, full-map symplectic/reversal/composition checks, effective-Schwarzschild normalization cancellation, joint dilation, exact scale-null rank representative, and fixed-dimensional-`Lambda` imported-standard classification. Run focused test and preserve missing-file RED. Commit tests.

## Task 3 — Implement direct-curvature full phase map

**Files**
- Create: `studies/spacetime/kottler_null_scattering_jacobi.py`
- Create: `studies/spacetime/kottler-null-scattering-jacobi-results.json`

Implement Kottler metric, deterministic metric-derivative Christoffel/Riemann reconstruction, regularized one-turning-point path, declared screen, direct optical projection, full `4x4` RK4 map, graph guard, and controls. Preserve raw Ricci and optical records. Explicitly separate Killing normalization from frequency-converted map. Render deterministic `.8g` JSON, canonicalizing only `abs(value)<1e-7` to `0.0`. Run focused suite to GREEN and commit.

## Task 4 — Publish bounded negative result

**Files**
- Create: `tests/test_kottler_null_scattering_reports.py`
- Create: `audit/kottler-null-scattering-jacobi-report-en.md`
- Create: `audit/kottler-null-scattering-jacobi-report-it.md`
- Create: `theory/spacetime/kottler-null-scattering-jacobi.md`
- Modify: `docs/roadmap.md`

Add report tests first and preserve missing-report RED. Publish semantically aligned EN/IT authority with identical status, equations, values, result, gates, source scope, and limitations. State that any recovered scale from fixed dimensional `Lambda` is imported, not `ell0`; no channel independence without joint covariance. Re-run focused report tests and commit.

## Task 5 — Verify, ship conservatively, and preserve memory

1. Run focused Kottler suites and Schwarzschild/RN cross-controls.
2. Regenerate artifact to a temporary file and compare byte-for-byte.
3. Run `python3 tools/extract_docx.py --check`, `python3 tools/inventory_source.py --check`, full `python3 -m unittest discover -s tests`, and `git diff --check`.
4. Perform direct source-scope, bilingual, equation/sign, boundary, rank, and claim review; record `DIRECT_REVIEW_NO_SUBAGENT`, not independent review.
5. Push branch and open PR. Require green `tests` and `latex` jobs plus mergeability.
6. Auto-merge only if result is conservative, unambiguous, deterministic, and fully green. Otherwise leave PR open.
7. Verify post-merge CI, write timestamped Hermes Inbox note, remove worktree and branches, and leave main clean.
8. Do not cancel loop: this bounded negative result does not meet structural-dead-end criteria.
