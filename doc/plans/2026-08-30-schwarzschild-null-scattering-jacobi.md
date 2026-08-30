# Schwarzschild finite-boundary null-scattering Jacobi implementation plan

> Direct execution only. User forbids subagents. Follow TDD, preserve raw objects, commit each bounded task.

**Goal:** Add deterministic full transported-screen Jacobi phase-map control along generic finite-boundary Schwarzschild null scattering, then test affine/geometric scale identifiability without detector claims.

**Architecture:** Reuse preregistered scattering path and 4D Schwarzschild helpers. New module computes screen/Riemann profile, integrates primary `4x4` phase map, exposes source/endpoint/caustic/scale/rank controls, and renders deterministic JSON. Existing module remains unchanged.

**Tools:** Python standard library, `unittest`, existing matrix helpers, repository report/source conventions.

---

## Task 1: RED scientific API tests

**Files:**
- Create `tests/test_schwarzschild_null_scattering_jacobi.py`
- Target `studies/spacetime/schwarzschild_null_scattering_jacobi.py`

1. Write focused tests for domain/profile structure, screen orthonormality, symmetric trace-free optical `K`, full-map shape/symplecticity, turning composition, reverse inverse, zero window, source preparations, guarded caustic graph, endpoint actions, affine scaling, geometric scaling, rank fields, and deterministic result status.
2. Run:
   `python3 -m unittest tests.test_schwarzschild_null_scattering_jacobi`
3. Confirm RED via missing module `FileNotFoundError`; preserve diagnostic.
4. Commit tests.

## Task 2: GREEN profile and full phase map

**Files:**
- Create `studies/spacetime/schwarzschild_null_scattering_jacobi.py`
- Modify tests only if test assumptions conflict with preregistered mathematics; document correction.

1. Implement imports/constants and validation.
2. Construct ordered affine samples with turning regularization and branch labels.
3. Implement full Schwarzschild metric/connection/Riemann evaluation including theta derivatives.
4. Construct/transport oriented screen; emit residuals and `K` profile.
5. Integrate `P'=[[0,I],[K,0]]P` with convergent ordered stepping.
6. Implement raw, zero-window, composition, reverse, source-preparation, caustic and endpoint-action controls.
7. Run focused tests until GREEN.
8. Commit implementation.

## Task 3: Scale/rank controls and deterministic artifact

**Files:**
- Modify module and scientific tests
- Create `studies/spacetime/schwarzschild-null-scattering-jacobi-results.json`

1. Implement affine scaling with `D_a` conversion.
2. Implement `M -> sM` geometric conversion `D_s^-1 P(sM) D_s` at fixed dimensionless protocol.
3. Implement preregistered feature vector, finite-difference Jacobian `(rho,R,log M)`, separate ranks/null direction and bounded collision grid.
4. Add `build_result`, `render`, CLI `--check`.
5. Generate artifact twice and compare bytes.
6. Run focused scientific tests.
7. Commit controls/artifact.

## Task 4: Sources, bilingual theory/audit and roadmap

**Files:**
- Create `tests/test_schwarzschild_null_scattering_jacobi_sources.py`
- Create `tests/test_schwarzschild_null_scattering_jacobi_reports.py`
- Create `theory/spacetime/schwarzschild-null-scattering-jacobi.md`
- Create `audit/schwarzschild-null-scattering-jacobi-report-en.md`
- Create `audit/schwarzschild-null-scattering-jacobi-report-it.md`
- Modify `docs/roadmap.md`
- Modify `references/verification-log.md` only for exact existing canonical-key scope; add no invented source.

1. RED tests require source keys/scopes, labels, status/gate, equations and EN/IT semantic parity.
2. Confirm RED for missing reports/theory.
3. Write bounded reports from deterministic artifact. Keep source limitations explicit.
4. Update roadmap and verification scope.
5. Run source/report tests and prior focused Schwarzschild suite.
6. Commit documentation/audit.

## Task 5: Direct review, full verification, PR and CI

1. Directly compare spec, plan, code, artifact, EN/IT reports and source scope. Record `DIRECT_REVIEW_NO_SUBAGENT` because explicit user policy forbids subagents.
2. Run:
   - `python3 studies/spacetime/schwarzschild_null_scattering_jacobi.py --check`
   - focused new suite
   - prior Schwarzschild focused suite
   - `python3 -m unittest discover -s tests`
   - `python3 tools/extract_docx.py --check`
   - `python3 tools/inventory_source.py --check`
   - `git diff --check`
3. Push exact SHA and open conservative PR.
4. Wait for GitHub `tests` and `latex` jobs. Local missing LaTeX never substitutes for CI.
5. Auto-merge only if all checks green, bilingual/source/status review clean, and result remains conservative/non-ambiguous.
6. Update main, remove worktree/branch, and write timestamped Hermes Inbox note. Integrate prior PR #84–#93 notes into shared memory only if no concurrent-write risk; otherwise preserve new Inbox note.
7. Keep durable loop `16588751` active. Do not declare structural dead end.
