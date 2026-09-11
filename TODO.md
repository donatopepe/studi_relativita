# TODO — UMCH research engineering

Updated: 2026-09-11

## Active milestone: Kerr correlated-noise mismatch threshold MVP

**Objective:** determine whether a shared full correlated-noise covariance cancels in signal-minus-calibration observables and derive exact differential-mismatch threshold where branch collision returns.

**Metric + threshold:** correctness over exactly `8/8` preregistered controls.

**Fixed cases/order:** full-noise domain, shared-noise cancellation, sign-cone noncollision, analytic mismatch threshold, bounded residual, threshold collision, basis/scale invariance, nonclaims.

**Fixed order and dependencies**

1. [x] Ratify correlated-noise mismatch specification.
   - Depends on: bounded reference-drift milestone `b1ca8a8` and green CI `34587982249`.
   - Complete when: full SPD shared-noise model, differential mismatch norm, exact critical threshold, 0.8 bounded fraction, collision witness, eight controls, J63–J70 and nonclaims are preregistered.
   - Test: structural spec test and shared UTF-8 validator.
2. [x] Extend authoritative Kerr scenario matrix and runner.
   - Depends on: task 1.
   - Complete when: J63–J70 and `calibration_mismatch` category have fail-closed handlers; total, per-scenario and per-category JSON runs pass.
   - Test: matrix/runner contract plus every granular command.
3. [x] Implement correlated-noise mismatch engine.
   - Depends on: tasks 1–2.
   - Complete when: SPD validation, shared-noise cancellation, sign-cone proof, analytic operator-norm threshold, safe lower bound, exact threshold collision, basis/scale null and guardrails pass.
   - Test: exactly eight focused controls and deterministic artifact equality.
4. [ ] Generate stable artifacts and bilingual scientific record. **ACTIVE**
   - Depends on: task 3 GREEN.
   - Complete when: scientific JSON, total battery report, theory, EN/IT audits, roadmap and ledger align and preserve corrected history/nonclaims.
   - Test: report tests plus deterministic artifact equality.
5. [ ] Closure and publication.
   - Depends on: tasks 1–4 GREEN.
   - Complete when: focused/full tests, total and all granular runs, deterministic checks, shared UTF-8, diff, CodeGraph and CI pass; `main=origin/main`; Hermes updated.

## Previous milestone closure evidence

- Scientific controls: `8/8`.
- Scenario battery: `62/62`; all 62 per-scenario and 15 per-category granular runs green.
- Full suite: `1189/1189`.
- Deterministic artifact/report, extraction/inventory, shared UTF-8, diff and CodeGraph gates green.
- Exact safe midpoint radii `[0.077332007,37.595673]`; conservative 0.8 drift keeps minimum obstruction `0.0021528862`. Endpoint loses obstruction/rank; outside crossing collides at `8.8817842e-16`.
- Published `main=origin/main` at `08a6164`; GitHub Actions run `34587257553` tests/LaTeX passed.

## Previous corrected milestone evidence

- Corrected scientific controls: `8/8`.
- Scenario battery: `54/54`; all 54 per-scenario and 14 per-category granular runs green.
- Full suite: `1176/1176`.
- Corrected and predecessor artifacts deterministic; extraction/inventory, shared UTF-8, diff and CodeGraph gates green.
- Root correction: positive placement product permits collision. Inside references `[0.1,10.0]` block it; outside `[0.02,0.02]` collides at residual `1.7763568e-15`. Unknown reference collision remains `8.8817842e-16`.
- Published corrected `main=origin/main` at `fc8a759`; GitHub Actions run `34572177197` tests/LaTeX passed.

## Superseded milestone evidence requiring correction

- Scientific controls: `8/8`.
- Scenario battery: `46/46`; all 46 per-scenario and 13 per-category granular runs green.
- Full suite: `1163/1163`.
- Deterministic artifact/report, extraction/inventory, shared UTF-8, diff and CodeGraph gates green.
- Root result: known reference outside each branch-variance interval gives positive sign obstruction; calibration-only rank stays one, joint signal/reference rank becomes two. Unknown reference restores exact collision residual `8.8817842e-16`.
- Published `main=origin/main` at `dd7b03c`; GitHub Actions run `34568400157` tests/LaTeX passed.

## Previous milestone closure evidence

- Scientific controls: `8/8`.
- Scenario battery: `38/38`; all 38 per-scenario and 12 per-category granular runs green.
- Full suite: `1150/1150`.
- Deterministic artifact/report, extraction/inventory, shared UTF-8, diff and CodeGraph gates green.
- Root distinction resolved analytically: same-point common calibration and separately profiled composite nuisance are different claims; bounded composite sets are disjoint by second-channel interval gap `8.9423947`, while relaxed positive gains collide to residual `8.8817842e-16`.
- Published `main=origin/main` at `fdc3076`; GitHub Actions run `34554175739` tests/LaTeX passed.

## Previous milestone closure evidence

- Scientific controls: `8/8`.
- Scenario battery: `30/30`; 30 scenario and 11 category granular runs green.
- Full suite: `1137/1137`.
- Deterministic artifact/report, shared UTF-8, extraction/inventory, diff and CodeGraph gates green.
- Performance blocker solved by caching fixed Kerr covariances: focused runtime dropped from timeout `>900s` to under `10s`.
- Published `main=origin/main` at `9b203a1`; GitHub Actions run `34537112452` tests/LaTeX passed.

## Fixed MVP assumptions

- Common receiver calibration applies identically under both branch hypotheses.
- Diagonal gains are positive and bounded in toy range `[0.5,1.5]`; isotropic noise sigma is bounded in `[0.1,1.0]`.
- Bounds are preregistered mathematical controls, not measured hardware priors.
- Deterministic tensor grid is refined once before any result is accepted.
- Unbounded common nuisance is tested separately with gain tending to zero or noise tending to infinity.

## Preserved milestone results

- Kerr finite source/analyzer: scientific `8/8`, scenario battery `14/14`, suite `1110/1110`, CI green at `cd188ab`.
- Full covariance retains orientation shape, but an unknown branch-dependent analyzer scalar has an exact collision.
- Kerr calibrated receiver: scientific `8/8`, scenarios `22/22`, suite `1124/1124`, CI green at `1f5bb15`.
- Fixed calibration distinguishes branches; branch-dependent unconstrained gain/noise gives exact covariance collision `diag(1,100)`.

## Scientific guardrails

```text
UMCH=UNPROVEN_SECONDARY_CANDIDATE
L_identified=false
ell0_identified=false
L_equals_ell0=NOT_DERIVED
extra_dimension_detected=false
structural_dead_end=NOT_DECLARED
NO_POSITIVE_DETECTION_CLAIM
```
