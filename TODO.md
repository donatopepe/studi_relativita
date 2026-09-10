# TODO — UMCH research engineering

Updated: 2026-09-10

## Active milestone: Kerr finite source/analyzer MVP

**Objective:** determine whether the verified Kerr Jacobi orientation shape survives a declared finite Gaussian source covariance and endpoint analyzer projection, while distinguishing geometry from preparation nuisance and preserving the absolute-scale null.

**Metric + threshold:** correctness over exactly `8/8` preregistered controls.

**Fixed order and dependencies**

1. [x] Ratify bounded source-covariance/analyzer specification.
   - Depends on: merged Kerr Jacobi gate `5e3f5db`.
   - Complete when: inputs, formulas, eight cases, source scope, stop conditions and nonclaims are explicit.
   - Test: spec structural test and UTF-8 validator.
2. [x] Extend authoritative scenario matrix and runner.
   - Depends on: task 1.
   - Complete when: all new scenarios have stable IDs/categories/handlers; total, scenario and category modes fail closed and emit JSON.
   - Test: matrix/runner tests plus total and every granular execution.
3. [x] Implement smallest finite Gaussian source covariance and analyzer readout.
   - Depends on: tasks 1–2.
   - Complete when: covariance propagation uses the existing `4x4` phase map, raw covariance remains primary, analyzer is declared and nuisance controls are explicit.
   - Test: eight focused controls.
4. [x] Generate bounded deterministic artifacts and reports.
   - Depends on: task 3 GREEN.
   - Complete when: stable scientific JSON, scenario report, theory note and EN/IT audits agree.
   - Test: byte-identical regeneration and report tests.
5. [x] Closure and publication.
   - Depends on: tasks 1–4 GREEN.
   - Complete when: CodeGraph synced; UTF-8, focused/full tests, total/granular runner, deterministic checks and CI pass; main/origin align; Hermes updated.

## Milestone result

- Scientific controls: `8/8`.
- Scenario battery: `14/14`; every scenario and category granular run passed.
- Full suite: `1110/1110`.
- Deterministic artifacts, UTF-8, extraction, inventory and CodeGraph gates passed locally.
- Publication complete: `main=origin/main` at `d9cbc1f`; GitHub Actions run `34468583168` tests/LaTeX passed.

## Current scientific guardrails

```text
UMCH=UNPROVEN_SECONDARY_CANDIDATE
L_identified=false
ell0_identified=false
L_equals_ell0=NOT_DERIVED
extra_dimension_detected=false
structural_dead_end=NOT_DECLARED
NO_POSITIVE_DETECTION_CLAIM
```

## Completed milestones

- [x] Kerr circular photon-ring baseline — PR #107.
- [x] Kerr finite ZAMO endpoints — PR #108.
- [x] Kerr parallel screen transport — PR #109.
- [x] Kerr Jacobi tidal phase map — main `5e3f5db`, `8/8`, scenarios `6/6`, suite `1096/1096`, CI green.
