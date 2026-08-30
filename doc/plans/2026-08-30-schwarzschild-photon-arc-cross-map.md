# Implementation plan: Schwarzschild photon-sphere finite-arc cross-map

**Goal:** Add a deterministic counterexample-first audit of the joint open-arc Levi-Civita transport and optical Jacobi phase map on the Schwarzschild photon sphere, testing caustics, endpoint/affine/geometric nuisances, joint rank and provenance against the existing one-winding controls without making an `ell0` or detection claim.

**Architecture:** Reuse the verified Schwarzschild connection and photon-sphere optical helpers. Add one bounded study module that keeps the raw connection endpoint map and raw `4x4` optical phase map primary, emits canonical JSON, and exposes only preregistered derived diagnostics. Add focused scientific, source-scope and bilingual-report tests before implementation/documentation. No generic scattering solver, detector model or new dependency is introduced.

**Test runner:** `python3 -m unittest` because the baseline `/usr/bin/python3` lacks `pytest`.

## Task 1 — Freeze the scientific contract in RED tests

**Create:**
- `tests/test_schwarzschild_photon_arc_cross_map.py`
- `tests/test_schwarzschild_photon_arc_cross_map_sources.py`
- `tests/test_schwarzschild_photon_arc_cross_map_reports.py`

1. Write scientific tests requiring:
   - open finite-arc null/geodesic geometry and declared affine anchor;
   - raw `T_arc` and `P_arc` objects with Lorentz/symplectic residuals;
   - exact/RK4 agreement at `0, pi/3, pi, 3*pi/2, 2*pi`;
   - zero-window identity/generator limits;
   - semigroup composition;
   - caustic singularity only in graph blocks, never the full phase map;
   - orientation and endpoint action behavior;
   - separate affine and Schwarzschild scale-orbit collisions;
   - joint dimensionless Jacobian rank one in `(alpha,log M)` with convergent finite differences;
   - `alpha=2*pi` provenance against the existing photon-orbit null segment and separately composed closure;
   - exact state/scope/gate strings and `ell0_identified=false`.
2. Write source tests limiting `Darwin1959GravityField` to Schwarzschild trajectory/critical orbit context and `Sachs1961` to null optical framework; explicitly forbid source support for finite arc, endpoint preparation, detector, covariance, `ell0`, UMCH or detection.
3. Write bilingual report parity tests for state, scope, gate, raw-object labels, core numbers, source limitations, direct-review exception and no-evidence language.
4. Run:

   `python3 -m unittest tests.test_schwarzschild_photon_arc_cross_map tests.test_schwarzschild_photon_arc_cross_map_sources tests.test_schwarzschild_photon_arc_cross_map_reports -q`

   Expected: RED due missing module/artifact/reports.
5. Commit: `test: define photon-arc cross-map controls`.

## Task 2 — Implement raw maps and deterministic artifact

**Create:**
- `studies/spacetime/schwarzschild_photon_arc_cross_map.py`
- `studies/spacetime/schwarzschild-photon-arc-cross-map-results.json`

1. Import/reuse only local verified helpers from:
   - `schwarzschild_mixed_levi_civita_holonomy.py`;
   - `schwarzschild_photon_orbit_holonomy.py`;
   - `schwarzschild_photon_sphere_jacobi.py`.
2. Implement open-arc geometry `r=3M`, `L=3M alpha`, `Delta t=3 sqrt(3) M alpha`, `Delta phi=epsilon alpha` and verify null/geodesic residuals.
3. Implement exact raw connection endpoint map with source/observer static tetrads and independent fixed-step transport.
4. Implement exact raw optical phase map and independent RK4 propagation; preserve split `A,B,C,D` blocks and safe vertex/nonvertex graphs.
5. Implement zero-window derivatives and semigroup controls.
6. Implement caustic flags at `alpha=n*pi` while retaining finite/invertible full phase maps.
7. Implement orientation reversal and explicit endpoint actions for connection and phase-space maps.
8. Implement separate affine and Schwarzschild geometric-scale conversions using declared rate matrices.
9. Implement fixed deterministic feature vector, finite-difference Jacobian, singular values/rank and scale-null residual; retain raw maps independently of features.
10. Implement `alpha=2*pi` cross-check against the old future-null segment and separately against the old closed-loop composition.
11. Emit sorted, indented canonical JSON and `--check` byte comparison.
12. Run focused scientific tests until GREEN and regenerate artifact.
13. Commit: `feat: audit photon-sphere finite-arc cross-map`.

## Task 3 — Write bounded theory and bilingual audits

**Create:**
- `theory/spacetime/schwarzschild-photon-arc-cross-map.md`
- `audit/schwarzschild-photon-arc-cross-map-report-en.md`
- `audit/schwarzschild-photon-arc-cross-map-report-it.md`

**Modify:**
- `docs/roadmap.md`

1. Document equations, endpoint-map versus holonomy distinction, raw objects, caustics, quotient/rank result and separate scale nuisances.
2. State that two operator maps and many entries still carry one calibrated continuous shape direction in this exact family; do not generalize beyond scope.
3. Keep source scope explicit and identical in EN/IT.
4. Record that direct conformance review replaces subagent review because the user explicitly prohibited subagents.
5. Preserve `UNPROVEN`, `NO_POSITIVE_DETECTION_CLAIM`, `ell0_identified=false`, no structural dead end, and open alternatives.
6. Update roadmap with exact state/scope/gate and next bounded routes.
7. Run report and source tests until GREEN.
8. Commit: `docs: report photon-arc rank loss`.

## Task 4 — Direct conformance review and verification

1. Compare spec, implementation, artifact, theory, EN audit and IT audit field-by-field.
2. Run focused suite:

   `python3 -m unittest tests.test_schwarzschild_photon_arc_cross_map tests.test_schwarzschild_photon_arc_cross_map_sources tests.test_schwarzschild_photon_arc_cross_map_reports -q`
3. Run artifact check:

   `python3 studies/spacetime/schwarzschild_photon_arc_cross_map.py --check`
4. Run repository checks used by CI, including full unit discovery, extraction/inventory and LaTeX commands declared by `.github/workflows/verify.yml`.
5. Run `git diff --check` and verify clean generated artifacts.
6. If any failure occurs, diagnose root cause before editing; preserve environmental failures separately from scientific failures.
7. Resolve closure-review setting. Because subagents are explicitly forbidden, record the direct-review exception rather than dispatching one.

## Task 5 — Ship conservatively

1. Commit any bounded verification corrections.
2. Push `research/schwarzschild-photon-arc-cross-map` and open a PR with state/scope/gate, verification evidence and source limitations.
3. Wait for both `tests` and `latex` CI jobs.
4. Auto-merge only if all checks are green and the result is conservative, unambiguous and negative/diagnostic. Otherwise leave PR open.
5. After merge, sync `main`, remove worktree and local branch.
6. Write a timestamped Hermes Inbox note with PR, merge SHA, CI URL, exact state/scope/gate, numerical controls, open blockers and explicit no-detection/no-`ell0` conclusion.
7. Do not declare a structural dead end. Keep loop `16588751` active.
