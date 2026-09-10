# TODO — UMCH research engineering

Updated: 2026-09-10

## Active milestone: Kerr calibrated receiver/noise likelihood MVP

**Objective:** determine whether Kerr orientation-dependent observer covariance remains statistically distinguishable under one declared calibrated Gaussian receiver model, while testing exact collisions caused by unknown gain/noise nuisances and preserving the absolute-scale null.

**Metric + threshold:** correctness over exactly `8/8` preregistered controls.

**Fixed order and dependencies**

1. [x] Ratify bounded receiver/noise/likelihood specification.
   - Depends on: completed finite source/analyzer milestone `cd188ab`.
   - Complete when: receiver equation, Gaussian likelihood/KL conventions, fixed versus nuisance calibration, eight controls, scenario IDs, sources, stop conditions and nonclaims are explicit.
   - Test: structural spec test and UTF-8 validation.
2. [x] Extend authoritative Kerr scenario matrix and reusable runner.
   - Depends on: task 1.
   - Complete when: J15–J22 are registered with categories/handlers; total, per-scenario and per-category JSON runs pass or fail closed.
   - Test: scenario matrix/runner tests and all granular commands.
3. [x] Implement smallest deterministic receiver likelihood engine.
   - Depends on: tasks 1–2.
   - Complete when: calibrated covariance, Gaussian KL symmetry controls, noise monotonicity, finite-sample expected likelihood, nuisance collision, basis covariance and scale null pass.
   - Test: exactly eight focused controls and deterministic artifact equality.
4. [ ] Generate artifacts and bilingual scientific record. **ACTIVE**
   - Depends on: task 3 GREEN.
   - Complete when: scientific JSON, total scenario report, theory, EN/IT audits, roadmap and ledger agree and preserve all prior negative results.
   - Test: report contracts, byte-identical regeneration, UTF-8 gate.
5. [ ] Closure and publication.
   - Depends on: tasks 1–4 GREEN.
   - Complete when: CodeGraph sync, focused/full suite, total/all granular scenarios, deterministic checks, UTF-8, extraction/inventory, clean main, push and remote CI are green; Hermes updated.

## Previous milestone result

- Kerr finite source/analyzer: scientific `8/8`, scenario battery `14/14`, suite `1110/1110`, CI green at `cd188ab`.
- Full covariance retains orientation shape, but an unknown branch-dependent analyzer scalar has an exact collision.

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
