# TODO — UMCH research engineering

Updated: 2026-09-11

## Active milestone: Kerr calibration-reference placement correction MVP

**Objective:** correct the auxiliary-channel collision theorem by testing reference variance inside versus outside the open interval between branch variances and preserve both exact outcomes.

**Metric + threshold:** correctness over exactly `8/8` preregistered controls.

**Fixed cases/order:** corrected algebra, inside-interval collision, outside-interval obstruction, two-channel joint witness, Fisher rank, unknown-reference collision, weak-channel limit, scale/nonclaims.

**Fixed order and dependencies**

1. [x] Ratify corrected reference-placement specification.
   - Depends on: published auxiliary-channel milestone `16c9718`; prior reference `[0.02,0.02]` lay below both branch variances, so its positive product permits collision rather than obstructing it.
   - Complete when: sign error is explicit; inside references `[0.1,10.0]`, outside controls `[0.02,0.02]`, exact gain/noise witnesses, eight controls, J47–J54 and nonclaims are preregistered.
   - Test: structural spec test and shared UTF-8 validator.
2. [ ] Extend authoritative Kerr scenario matrix and runner. **ACTIVE**
   - Depends on: task 1.
   - Complete when: J47–J54 and `reference_placement` category have fail-closed handlers; total, per-scenario and per-category JSON runs pass.
   - Test: matrix/runner contract plus every granular command.
3. [ ] Correct calibration-channel engine and artifact.
   - Depends on: tasks 1–2.
   - Complete when: inside-interval known reference blocks positive collision; outside-interval known reference admits explicit exact collision; Fisher/precision/weak/scale controls and guardrails pass.
   - Test: exactly eight focused controls, regression of erroneous polarity and deterministic artifact equality.
4. [ ] Correct bilingual scientific record and preserved history.
   - Depends on: task 3 GREEN.
   - Complete when: theory, EN/IT audits, roadmap and ledger explicitly supersede erroneous claim without deleting historical evidence.
   - Test: report tests plus deterministic artifact equality.
5. [ ] Closure and publication.
   - Depends on: tasks 1–4 GREEN.
   - Complete when: focused/full tests, total and all granular runs, deterministic checks, shared UTF-8, diff, CodeGraph and CI pass; `main=origin/main`; Hermes correction recorded.

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
