# Kerr equatorial photon-ring orientation/scale implementation plan

> Direct MVP execution. No subagent. Recon and closure review are labeled `DIRECT_RECON_NO_SUBAGENT` / `DIRECT_REVIEW_NO_SUBAGENT`; neither is independent review.

**Objective:** determine whether exact prograde/retrograde equatorial Kerr circular null orbits add orientation-sensitive dimensionless shape while joint `M,a` dilation leaves absolute scale and `ell0` unidentified.

**Metric:** all eight preregistered controls pass (`8/8`) under frozen tolerances before accepting a result.

**Fixed cases/order:** radius/range; branch ordering; Schwarzschild collision; radial-potential conformance; signed convention collision; joint dilation; rank/scale-null direction; no-`ell0` gate.

**MVP:** standard-library analytic orbit module using the exact sourced radii, independent radial potential and derivative, exact equatorial Boyer–Lindquist angular rate, representative `chi={0,0.2,0.6,0.9,0.99}`, and scale factor `2.5`. No root solver, symbolic framework, transported screen, finite-boundary scattering, source/receiver, covariance, or data.

**Escalation condition:** add one component only if a named control fails after formula and sign conventions are traced against the primary source. Source ambiguity stops implementation.

**Worktree:** `/home/public/studi_relativita/.worktrees/kerr-photon-ring-orientation-scale`

## Task 1 — Freeze source scope test-first

**Files**
- Create: `tests/test_kerr_photon_ring_sources.py`
- Modify: `references/library.bib`
- Modify: `references/verification-log.md`

1. Require `Teo2003SphericalPhotonOrbits`, DOI `10.1023/A:1026286607562`, complete journal metadata, author PDF, equations `(1a,b)`, `(2)`–`(5a-d)`, radial equation `(10)`, and constant-radius conditions.
2. Require explicit exclusions: no detector, screen/Jacobi map, physical clock, covariance, `ell0`, UMCH evidence, or detection.
3. Preserve RED; add narrowly verified entries; run GREEN; commit immediately.

## Task 2 — Define eight controls RED

**Files**
- Create: `tests/test_kerr_photon_ring_orientation_scale.py`

Write one measured test per frozen control. Require raw branch records with `x_ph`, `r_ph`, `xi/M`, `Omega_phi*M`, `Delta_t_per_2pi/M`, `R` and `R_prime`; convention labels; exact scale audit; local feature Jacobian/rank; global nonclaims. Freeze tolerances before implementation. Preserve RED and commit.

## Task 3 — Implement smallest exact orbit module

**Files**
- Create: `studies/spacetime/kerr_photon_ring_orientation_scale.py`

Implement only:

- prograde/retrograde radius formulas;
- impact parameter from constant-radius equations;
- independently evaluated radial potential and analytic radial derivative;
- equatorial circular `Omega_phi` and unsigned Boyer–Lindquist period;
- signed-spin/orientation convention map;
- Schwarzschild and near-extremal limits;
- exact joint dilation;
- finite-difference rank audit over dimensionless features.

Run focused tests to `8/8`, changing one named defect at a time. Commit immediately when green.

## Task 4 — Generate deterministic artifact

**Files**
- Create: `studies/spacetime/kerr-photon-ring-orientation-scale-results.json`
- Extend focused test with subprocess/artifact equality

Emit exact eight control records, `controls_passed=8`, `controls_total=8`, preserved thresholds, `.8g` values, raw branch maps, source/convention labels, bounded result, physical gate, and global nonclaims. Require byte-identical regeneration. Commit.

## Task 5 — Add bilingual scientific record

**Files**
- Create: `theory/spacetime/kerr-photon-ring-orientation-scale.md`
- Create: `audit/kerr-photon-ring-orientation-scale-report-en.md`
- Create: `audit/kerr-photon-ring-orientation-scale-report-it.md`
- Create: `tests/test_kerr_photon_ring_reports.py`
- Modify: `docs/roadmap.md`
- Modify: `audit/kaluza-klein-reformulation-change-ledger.md`

Write report tests first. Preserve the 5D candidate, tensor conformance, finite `S1` result, prior Schwarzschild controls, and `F_0`. Label Kerr as a deferred-now-completed `4D` comparison baseline, not evidence against or for an extra dimension. Run GREEN; commit.

## Task 6 — Close and publish

1. Run focused source/control/report tests.
2. Run full Python suite and all repository-standard deterministic checks.
3. Run `git diff --check`; inspect every changed file and artifact.
4. Record `DIRECT_REVIEW_NO_SUBAGENT`; fix concrete findings one variable at a time, with immediate tested commits.
5. Rebase or merge current `origin/main` into branch before publication because worktree began at PR #105; rerun focused/full checks.
6. Push branch, open PR, verify tests/LaTeX CI, and auto-merge only if all required checks are green and no convention ambiguity remains.
7. Sync main, post-merge verify, update Hermes, then remove merged Kerr branch/worktree.

## Stop conditions

Stop with bounded negative/inconclusive result if sourced formulas fail the independent radial potential; branch/range/Schwarzschild controls fail; convention reversal fails; dimensionless records change under dilation; scale-null direction disappears without imported dimensional data; or any output treats Boyer–Lindquist time as detector time or derives `ell0`, UMCH evidence, or detection.
