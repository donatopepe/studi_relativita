# TODO — UMCH research engineering

Updated: 2026-09-12

## Active milestone: Kerr paired-stream common-noise cancellation MVP

**Objective:** quantify exact covariance-estimation gain when paired signal/calibration streams share additive Gaussian noise, and test whether pairing materially reverses the AR(1) sample burden.

**Metric + threshold:** correctness over exactly `8/8` preregistered controls.

**Fixed cases/order:** joint block domain, cross-Wishart identity, paired coefficient, AR(1) RMS, safe count, zero-shared limit, basis/scale invariance, nonclaims.

**Fixed order and dependencies**

1. [x] Ratify paired-stream common-noise specification.
   - Depends on: AR(1) temporal-dependence milestone `7cb1ab5` and green CI `34688124833`.
   - Complete when: paired latent/noise model, cross-covariance Wick term, fixed rho `0.5`, counts `[16,64,256]`, expected small-gain negative, eight controls, J95–J102 and nonclaims are preregistered.
   - Test: structural spec test and shared UTF-8 validator.
2. [x] Extend authoritative Kerr scenario matrix and runner.
   - Depends on: task 1.
   - Complete when: J95–J102 and `cross_stream_dependence` category have fail-closed handlers; total, per-scenario and per-category JSON runs pass.
   - Test: matrix/runner contract plus every granular command.
3. [x] Implement paired-stream covariance engine.
   - Depends on: tasks 1–2.
   - Complete when: joint SPD validation, cross-Wishart identity, paired MSE coefficient, rho-0.5 RMS/count gate, independent-stream recovery, basis/scale null and guardrails pass.
   - Test: exactly eight focused controls and deterministic artifact equality.
4. [x] Generate stable artifacts and bilingual scientific record.
   - Depends on: task 3 GREEN.
   - Complete when: scientific JSON, total battery report, theory, EN/IT audits, roadmap and ledger align and preserve small-gain negative/nonclaims.
   - Test: report tests plus deterministic artifact equality.
5. [x] Closure and publication.
   - Depends on: tasks 1–4 GREEN.
   - Complete when: focused/full tests, total and all granular runs, deterministic checks, shared UTF-8, diff, CodeGraph and CI pass; `main=origin/main`; Hermes updated.

## Local closure evidence

- Scientific controls: `8/8`.
- Scenario battery: `102/102`; all 102 per-scenario and 20 per-category granular runs green.
- Full suite: `1254/1254`.
- Deterministic scientific artifact/total report, extraction/inventory, constraint study, shared UTF-8, diff and CodeGraph gates green.
- Root result: paired shared receiver noise lowers RMS only `0.4098%` and conservative count gate from `88` to `87`; `N=64` remains unsafe (`0.067498804`). Zero shared covariance restores count `88`.
- Publication pending final closure commit, push and remote CI.

## Historical milestone index

- Kerr AR(1) temporal-dependence penalty MVP: tasks 1–5 completed; depends on estimated-mean milestone `4a84c16`; scientific `8/8`, scenarios `94/94`, suite `1241/1241`, CI green at `7cb1ab5`.

## Previous milestone closure evidence

- Scientific controls: `8/8`.
- Scenario battery: `94/94`; all 94 per-scenario and 19 per-category granular runs green.
- Full suite: `1241/1241`.
- Deterministic artifact/report, extraction/inventory, shared UTF-8, diff and CodeGraph gates green.
- At rho `0.5`, RMS `[9.7334408,4.9038744,2.4524884]`; count gate rises to `88`; `N=64` fails (`0.068055453`). Near rho `0.99`, effective covariance df at N=64 is `2.9130205`.
- Published `main=origin/main` at `dc9bea4`; GitHub Actions run `34687669744` tests/LaTeX passed.

## Previous milestone closure evidence

- Scientific controls: `8/8`.
- Scenario battery: `86/86`; all 86 per-scenario and 18 per-category granular runs green.
- Full suite: `1228/1228`.
- Deterministic artifact/report, extraction/inventory, shared UTF-8, diff and CodeGraph gates green.
- Estimated mean costs exact factor `N/(N-1)`: RMS `[7.8472642,3.8290729,1.9032411]`. Conservative count gate rises from 53 to 54; `N=16` remains unsafe (`0.17426927`).
- Published `main=origin/main` at `dbcb71e`; GitHub Actions run `34652593522` tests/LaTeX passed.

## Previous milestone closure evidence

- Scientific controls: `8/8`.
- Scenario battery: `78/78`; all 78 per-scenario and 17 per-category granular runs green.
- Full suite: `1215/1215`.
- Deterministic artifact/report, extraction/inventory, shared UTF-8, diff and CodeGraph gates green.
- Exact combined covariance MSE coefficient `923.69333`; RMS follows inverse-root count. Markov risk ceiling 0.05 requires minimum equal count `53`; `N=16` fails (`0.16337744`), `N=64` passes (`0.04084436`) only this toy gate.
- Published `main=origin/main` at `ed8f113`; GitHub Actions run `34631514528` tests/LaTeX passed.

## Previous milestone closure evidence

- Scientific controls: `8/8`.
- Scenario battery: `70/70`; all 70 per-scenario and 16 per-category granular runs green.
- Full suite: `1202/1202`.
- Deterministic artifact/report, extraction/inventory, shared UTF-8, diff and CodeGraph gates green.
- Root semantic correction stayed local: full branch-set distance is `tau=18.797837`, not singular-cone margin. Aggregate mismatch 0.8 leaves separation `3.7595673`; exact full threshold collides at `1.3322676e-15` with observed minimum eigenvalue `0.39954509`.
- Published `main=origin/main` at `203295f`; GitHub Actions run `34608855632` tests/LaTeX passed.

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
