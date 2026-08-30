# Schwarzschild scattering screen/Riemann conformance implementation plan

> Direct execution only. User explicitly forbids subagents. Follow TDD red-green-refactor and preserve negative outcomes.

**Goal:** Test whether PR #94's declared scattering screen is Levi-Civita parallel modulo explicit null gauge and independently reproduce its optical tidal profile from a four-dimensional finite-difference Riemann tensor.

**Architecture:** Add a standalone conformance module reusing path/domain helpers but not the existing analytic optical-profile implementation for its Riemann reconstruction. Keep raw vectors/matrices primary. Generate deterministic artifact; then add bilingual reports and bounded source scope.

---

## Task 1: RED screen transport contract

**Files:**
- Create `tests/test_schwarzschild_scattering_screen_conformance.py`

1. Add tests for coordinate metric products, null ray, screen orthonormality and handed orientation.
2. Require `screen_transport_control` to return raw covariant derivatives, null-gauge coefficients, quotient vectors, screen rotation and coarse/fine convergence.
3. Fix acceptance bounds before implementation: interior quotient maximum `<2e-5`, screen rotation maximum `<2e-5`, refined residual no worse than coarse plus `1e-10`.
4. Run focused test and observe missing-module/API failure.
5. Commit RED tests.

## Task 2: GREEN screen transport audit

**Files:**
- Create `studies/spacetime/schwarzschild_scattering_screen_conformance.py`

1. Reuse regularized path samples and convert tetrad `k,e1,e2,l` to coordinates.
2. Implement full equatorial Christoffel symbols needed for covariant derivative, including polar entries.
3. Compute derivatives along retained path with nonuniform-lambda finite differences; separate endpoint and interior diagnostics.
4. Fit/subtract null gauge; preserve raw and quotient vectors.
5. Pass Task 1 tests without changing bounds.
6. Commit implementation.

## Task 3: RED/GREEN independent Riemann reconstruction

**Files:**
- Modify `tests/test_schwarzschild_scattering_screen_conformance.py`
- Modify `studies/spacetime/schwarzschild_scattering_screen_conformance.py`

1. First add failing tests requiring centered metric derivatives in both `r` and `theta`, full Riemann projection, symmetry/trace checks, orientation agreement and convergence.
2. Require checkpoint maximum analytic mismatch `<5e-5` at fine step and refined mismatch below coarse mismatch.
3. Observe RED against absent API.
4. Implement generic metric, numerical inverse, numerical Christoffel, numerical derivatives of Christoffel, lowered Riemann and full optical projection.
5. Add photon-sphere-limit anchor and deterministic `build_result/render/--check` API.
6. Pass focused tests and commit.

## Task 4: Artifact and bilingual/source audit

**Files:**
- Create `studies/spacetime/schwarzschild-scattering-screen-conformance-results.json`
- Create `theory/spacetime/schwarzschild-scattering-screen-conformance.md`
- Create `audit/schwarzschild-scattering-screen-conformance-report-en.md`
- Create `audit/schwarzschild-scattering-screen-conformance-report-it.md`
- Create `tests/test_schwarzschild_scattering_screen_conformance_reports.py`
- Create `tests/test_schwarzschild_scattering_screen_conformance_sources.py`
- Modify `docs/roadmap.md`
- Modify `references/verification-log.md`

1. Add RED report/source tests for exact shared status, gate, values, limitations and source keys.
2. Observe missing-file failures.
3. Generate artifact twice and verify byte identity.
4. Write theory and semantically aligned EN/IT audits; record `KNOWN_RESULT`, `PROJECT_DERIVATION`, `TOY_CONTROL`, `NEGATIVE_RESULT`, `OPEN_PROBLEM` scopes.
5. Reuse only existing canonical Schwarzschild/Sachs keys unless a genuinely needed canonical source is verified; state what sources do not establish.
6. Pass report/source tests; commit.

## Task 5: Direct conformance review, verification, PR/CI/Hermes

1. Directly compare spec, tests, implementation and artifact. Record `DIRECT_REVIEW_NO_SUBAGENT` because explicit user policy forbids subagents.
2. Run focused conformance suite and prior scattering/Jacobi suites.
3. Run `python3 -m unittest discover -s tests`, artifact `--check`, extraction `--check`, inventory `--check`, `git diff --check`.
4. Push exact SHA and open conservative PR only if result is unambiguous and negative/non-evidential.
5. Require PR and main `tests`/`latex` CI green before auto-merge.
6. Update main, remove worktree/branch, write timestamped Hermes Inbox note.
7. Keep loop active. If tests instead expose an unresolved scientific mismatch, do not auto-merge a passing claim; report bounded failure and preserve it.
