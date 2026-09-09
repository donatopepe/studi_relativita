# Kerr finite-boundary endpoint-gate implementation plan

> Direct MVP execution. No subagent. Recon and closure review are `DIRECT_RECON_NO_SUBAGENT` / `DIRECT_REVIEW_NO_SUBAGENT`; neither is independent review.

**Objective:** determine whether finite-boundary equatorial Kerr paths plus ZAMO endpoint tetrads yield consistent local direction/frequency shape while preserving exact geometric scale blindness.

**Metric:** all eight preregistered controls pass (`8/8`) under frozen thresholds.

**Fixed cases/order:** turning root; path/convergence; tetrad; local null reconstruction; orientation; Schwarzschild; dilation; rank/no-`ell0`.

**MVP:** standard-library equations and midpoint/trapezoid quadrature regularized by `r=r_turn+y^2`; no general geodesic solver, elliptic-function package, screen/Jacobi dynamics, detector, covariance, or data.

**Escalation condition:** add parallel screen transport only after endpoint baseline is `8/8`; otherwise fix named path/frame defect first.

## Task 1 — Freeze source contract RED/GREEN

**Files**
- Create `tests/test_kerr_finite_boundary_sources.py`
- Modify `references/library.bib`
- Modify `references/verification-log.md`

Require Gralla–Lupsasca DOI/arXiv metadata, equations `(1)`–`(13f)`, v3 correction status, path/turning scope, and explicit endpoint/detector exclusions. Preserve RED, add source entries, GREEN, commit.

## Task 2 — Define eight controls RED

**Files**
- Create `tests/test_kerr_finite_boundary_endpoint_gate.py`

Freeze baseline, thresholds, output keys, orientation and Schwarzschild counterexamples, scale/rank semantics, nonclaims, and deterministic artifact equality. Preserve missing-module RED and commit.

## Task 3 — Implement path and endpoint MVP

**Files**
- Create `studies/spacetime/kerr_finite_boundary_endpoint_gate.py`

Implement Kerr equatorial metric, radial potential, signed turning roots, regularized in/out path quadrature, ZAMO tetrad, vector projection/reconstruction, orientation/Schwarzschild/dilation/rank controls. Run to `8/8`; one defect per iteration; commit when green.

## Task 4 — Stable artifact

**Files**
- Create `studies/spacetime/kerr-finite-boundary-endpoint-gate-results.json`

Emit raw paths/frames/local records, exact eight controls and thresholds, convergence certificate, bounded result, physical gate, and nonclaims. `.8g`; zero only computed sub-`1e-7` noise, never thresholds. Byte-identical check; commit.

## Task 5 — Scientific record

**Files**
- Create `theory/spacetime/kerr-finite-boundary-endpoint-gate.md`
- Create EN/IT audit reports
- Create report tests
- Update roadmap and reformulation ledger

Preserve Kerr ring, 5D tensor, finite `S1`, Schwarzschild, and `F_0`. State ZAMO is a declared mathematical observer, not physical endpoint. Commit GREEN.

## Task 6 — Closure/publication

Run focused/full suites, deterministic repository checks, artifact comparisons, `git diff --check`, direct review. Push, PR, green tests/LaTeX, conservative auto-merge. Sync main, post-merge verify, Hermes update, remove merged branch/worktree.

## Stop conditions

Stop with bounded negative/inconclusive result on ambiguous source convention, invalid turning branch, non-future path, tetrad/null reconstruction failure, nonconvergence, failed Schwarzschild/convention collision, failed scale null, or any invented detector/clock/`ell0`/evidence claim.
