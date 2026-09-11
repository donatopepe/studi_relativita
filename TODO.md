# TODO — UMCH research engineering

Updated: 2026-09-11

## Active milestone: Kerr composite common-calibration profile gate MVP

**Objective:** determine whether separately profiled common-calibration nuisance sets for plus/minus Kerr hypotheses overlap on preregistered bounded domain, instead of comparing branches only at same nuisance point.

**Metric + threshold:** correctness over exactly `8/8` preregistered controls.

**Fixed cases/order:** analytic covariance-set overlap, domain validation, bounded profile separation, deterministic refinement, boundary witness, exact relaxed-domain collision, basis/scale invariance, nonclaims.

**Fixed order and dependencies**

1. [ ] Ratify composite-hypothesis profile specification. **ACTIVE**
   - Depends on: completed common-calibration milestone `5654b18` and green CI `34537767931`.
   - Complete when: shared physical calibration versus separate nuisance profiling is explicit; compact toy domain, exact overlap equations, relaxed-domain counterexample, eight controls, J31–J38 and nonclaims are preregistered.
   - Test: structural spec test and shared UTF-8 validator.
2. [ ] Extend authoritative Kerr scenario matrix and runner.
   - Depends on: task 1.
   - Complete when: J31–J38 and `profiling` category have fail-closed handlers; total, per-scenario and per-category JSON runs pass.
   - Test: matrix/runner contract plus every granular command.
3. [ ] Implement composite profile/overlap engine.
   - Depends on: tasks 1–2.
   - Complete when: analytic diagonal overlap interval, deterministic bounded pair search, refinement, positive bounded lower gate, exact relaxed-domain covariance collision, basis/scale invariance and guardrails pass.
   - Test: exactly eight focused controls and deterministic artifact equality.
4. [ ] Generate stable artifacts and bilingual scientific record.
   - Depends on: task 3 GREEN.
   - Complete when: scientific JSON, total battery report, theory, EN/IT audits, roadmap and ledger align and preserve prior results/nonclaims.
   - Test: report tests plus deterministic artifact equality.
5. [ ] Closure and publication.
   - Depends on: tasks 1–4 GREEN.
   - Complete when: focused/full tests, total and all granular runs, deterministic checks, shared UTF-8, diff, CodeGraph and CI pass; `main=origin/main`; Hermes updated.

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
