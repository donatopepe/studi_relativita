# Linearized five-dimensional tensor-conformance implementation plan

> Direct MVP execution. No subagent. Recon and closure review are labeled `DIRECT_RECON_NO_SUBAGENT` / `DIRECT_REVIEW_NO_SUBAGENT`; neither is independent review.

**Objective:** determine whether the existing scalar Hessian is exactly the ordinary-space `R_0i0j` block of the declared static linearized five-dimensional dust metric, while recording omitted compact-index curvature without creating a detection claim.

**Metric:** all eight preregistered controls pass (`8/8`) under frozen tolerances before accepting any result.

**Fixed cases/order:** trace reversal; harmonic residual; Ricci/Einstein conformance including vacuum; point/shell `R_0i0j` identity; compact-index/nonzero-mode separation; exact-uniform zero mode; source-stress dependence; joint scaling/rank.

**MVP:** one standard-library module built from analytic second derivatives of the existing exact compact-circle point potential, plus exact uniform zero mode and existing radial-shell quadrature. No symbolic framework, finite wrapped widths, nonlinear gravity, radion stabilization, detector, covariance, or data.

**Escalation condition:** add one new component only if a named control fails after sign/index conventions are traced against primary equations. Convention ambiguity stops implementation rather than triggering architecture growth.

**Worktree:** `/home/public/studi_relativita/.worktrees/kaluza-klein-tensor-conformance`

## Task 1 — Freeze source and convention contract test-first

**Files**
- Create: `tests/test_kaluza_klein_tensor_sources.py`
- Modify: `references/library.bib`
- Modify: `references/verification-log.md`

1. Write failing tests requiring `Robinson2006Normalization` metadata (`gr-qc/0609060`, arXiv DOI), equations `(1)`, `(2a,b)`, `(4)`, `(5a,b)`, `(6a,b)`, `(7a-c)`, `(9)`–`(15)`, and explicit exclusions.
2. Require `AtondoRubio2008Linearized5D` metadata (`hep-th/0609133`, journal reference), equations `(4)`–`(19)` as linearized-curvature context, and an explicit ban on importing its equations `(21)`–`(23)` cylinder ansatz/`h_44=0` into the localized calculation.
3. Preserve RED.
4. Add narrow bibliography and verification-log entries from inspected primary texts.
5. Run GREEN and commit immediately.

## Task 2 — Define exactly eight controls RED

**Files**
- Create: `tests/test_kaluza_klein_tensor_conformance.py`

Write one measured test per fixed control, in frozen order. Tests require:

1. `d=5` dust trace-reversal ratios;
2. maximum harmonic-gauge residual;
3. independent Riemann contraction versus Einstein operator and regular-vacuum residual;
4. point and radial-shell `R_0i0j` versus scalar-Hessian residuals;
5. localized `y`-derivative curvature plus separate `R_i4j4` record;
6. uniform `R_0404=R_0i04=0`, while allowing ordinary-space `R_i4j4`;
7. symbolic alternative diagonal-stress counterexample at fixed `h_00`;
8. joint dilation residual and `log L` null direction.

Freeze dimensionless baseline `L=1`, `r/L=2`, `y/L=0.7`, `shell_width/L=0.3`, scale factor `2.5`, tolerances, raw output keys, conservative tokens, and fail-closed result semantics. Preserve RED and commit tests.

## Task 3 — Implement smallest analytic tensor engine

**Files**
- Create: `studies/spacetime/kaluza_klein_linearized_tensor.py`
- Reuse without broad refactor: `studies/spacetime/kaluza_klein_linearized_tidal.py`

Implement only:

- trace reversal for diagonal static stress labels;
- declared dust metric;
- analytic compact-circle potential derivatives through second order in ordinary radial and compact coordinates;
- full bounded `5x5x5x5` linearized Riemann tensor or deterministic nonzero-entry map;
- Ricci, scalar, Einstein, harmonic residual;
- `R_0i0j`, `R_0404`, `R_0i04`, `R_i4j4` projections;
- radial-shell averaging using existing quadrature convention;
- dimensionless rescaling/rank diagnostic.

Do not numerically differentiate through singular support. Run focused tests to `8/8`; fix one named failure at a time. Commit immediately when green.

## Task 4 — Generate deterministic artifact

**Files**
- Create: `studies/spacetime/kaluza-klein-linearized-tensor-results.json`
- Extend focused test with subprocess/artifact equality check

Add CLI JSON emission. Require exact eight control records, `controls_passed=8`, `controls_total=8`, `.8g` rendering, canonical zero only below `1e-7`, convergence certificate, source/convention labels, full raw maps, conservative bounded result, physical gate, and global nonclaims. Regenerate, compare byte-for-byte, run `git diff --check`, commit.

## Task 5 — Add aligned scientific record

**Files**
- Create: `theory/spacetime/kaluza-klein-linearized-tensor.md`
- Create: `audit/kaluza-klein-linearized-tensor-report-en.md`
- Create: `audit/kaluza-klein-linearized-tensor-report-it.md`
- Create: `tests/test_kaluza_klein_tensor_reports.py`
- Modify: `audit/kaluza-klein-reformulation-change-ledger.md`
- Modify relevant roadmap/index files discovered by tests

Write report tests first. Require aligned equations, baseline values, all eight outcomes, source boundaries, `DIRECT_REVIEW_NO_SUBAGENT`, expected bounded result, physical gate, and every global nonclaim. Preserve earlier scalar and finite-localization negatives plus `F_0`; do not promote model status. Run GREEN and commit.

## Task 6 — Close locally, then publish

1. Run focused tensor source/control/report tests.
2. Run full discovered Python suite using repository-standard command.
3. Run every deterministic generator `--check` or artifact comparison discovered in CI.
4. Run `git diff --check`, repository inventory/extraction checks, and inspect changed files.
5. Record `DIRECT_REVIEW_NO_SUBAGENT`; fix only concrete findings, one variable per iteration, each code fix tested and committed immediately.
6. Update Hermes memory/checkpoint without secrets.
7. Push branch, open conservative PR, verify CI, and merge only if all required checks are green and no scientific ambiguity remains.
8. Sync `main`, verify post-merge suite, then remove only merged branch/worktree. Preserve deferred Kerr branch/worktree.

## Stop conditions

Stop with bounded negative/inconclusive record if any sourced convention is ambiguous; trace reversal/gauge/field equations disagree; vacuum Ricci fails; Hessian identity fails; localized/uniform separation fails; source-dependence control fails; joint scale null fails; or any output implies physical source, stabilization, calibrated coupling, `L`, `ell0`, evidence, or detection.
