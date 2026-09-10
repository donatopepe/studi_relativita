# TODO — UMCH research engineering

Updated: 2026-09-10

## Active milestone: Kerr shared-calibration robustness MVP

**Objective:** determine whether Kerr plus/minus receiver covariances remain distinguishable under one common but uncertain bounded receiver calibration, while proving that unbounded common attenuation/noise can drive information separation arbitrarily close to zero and preserving the geometric scale null.

**Metric + threshold:** correctness over exactly `8/8` preregistered controls.

**Fixed order and dependencies**

1. [x] Ratify shared-calibration robustness specification.
   - Depends on: completed calibrated receiver milestone `1f5bb15`.
   - Complete when: common-calibration contract, compact toy bounds, exact noncollision statement, asymptotic counterexample, eight controls, J23–J30, source scope and nonclaims are explicit.
   - Test: structural spec test and shared UTF-8 validator.
2. [x] Extend authoritative Kerr scenario matrix and runner.
   - Depends on: task 1.
   - Complete when: J23–J30 and categories are registered with fail-closed handlers; total, per-scenario and per-category JSON runs pass.
   - Test: matrix/runner contract plus every granular command.
3. [x] Implement bounded common-calibration robustness engine.
   - Depends on: tasks 1–2.
   - Complete when: common covariance map, exact finite noncollision, deterministic bounded search, refinement/convergence, boundary control, asymptotic information collapse, basis covariance and scale/nonclaims pass.
   - Test: exactly eight focused controls and deterministic artifact equality.
   - Resolved blocker: cached the two fixed signal covariances once per process; focused controls now complete in about 8 seconds instead of timing out after 900 seconds.
4. [ ] Generate stable artifacts and bilingual scientific record. **ACTIVE**
   - Depends on: task 3 GREEN.
   - Complete when: scientific JSON, total battery report, theory, EN/IT audits, roadmap and ledger align and preserve prior fixed/branch-dependent calibration results.
   - Test: byte-identical generation, report tests and shared UTF-8 validation.
5. [ ] Closure and publication.
   - Depends on: tasks 1–4 GREEN.
   - Complete when: CodeGraph, focused/full tests, total/all granular scenarios, deterministic checks, extraction/inventory, shared UTF-8, clean main, push/CI and Hermes are green.

## Fixed MVP assumptions

- Common receiver calibration applies identically under both branch hypotheses.
- Diagonal gains are positive and bounded in toy range `[0.5,1.5]`; isotropic noise sigma is bounded in `[0.1,1.0]`.
- Bounds are preregistered mathematical controls, not measured hardware priors.
- Deterministic tensor grid is refined once before any result is accepted.
- Unbounded common nuisance is tested separately with gain tending to zero or noise tending to infinity.

## Previous milestone result

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
