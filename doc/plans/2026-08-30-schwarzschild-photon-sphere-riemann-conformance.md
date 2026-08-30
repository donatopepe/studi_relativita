# Schwarzschild photon-sphere full-Riemann conformance implementation plan

> Direct execution only. Subagents and closure-review dispatch are excluded by the user; record `DIRECT_REVIEW_NO_SUBAGENT` and perform an explicit direct conformance review.

**Goal:** Independently reconstruct the circular photon-sphere optical matrix from the full four-dimensional Schwarzschild Riemann tensor, falsify or confirm the legacy profile, and regenerate all dependent deterministic controls without changing the UMCH contract.

**Architecture:** Add a bounded conformance module that reuses the tested numerical metric/Riemann machinery from the scattering conformance control but supplies independent circular-orbit tangent and ordered screen vectors. Then correct the legacy photon-sphere module only after a failing cross-conformance test proves the mismatch. Keep full phase maps primary and preserve source/history limitations.

**Tech:** Python standard library, `unittest`, deterministic JSON/Markdown, Git/GitHub CI.

---

### Task 1: RED direct circular full-Riemann contract

**Files:**
- Create: `tests/test_schwarzschild_photon_sphere_riemann_conformance.py`
- Create: `studies/spacetime/schwarzschild_photon_sphere_riemann_conformance.py` only after RED

1. Write tests requiring explicit `(polar,radial)` screen order, null/screen metric checks, coarse/fine four-dimensional Riemann projections, convergence, symmetry/vacuum trace, and direct disagreement with the legacy matrix.
2. Require corrected projection to be independently compared to the legacy module; do not hardcode the scattering helper's analytic profile as the reconstruction.
3. Run `python3 -m unittest tests.test_schwarzschild_photon_sphere_riemann_conformance`; confirm failure because the module/API does not exist.
4. Commit RED tests.

### Task 2: GREEN conformance reconstruction and legacy correction

**Files:**
- Create: `studies/spacetime/schwarzschild_photon_sphere_riemann_conformance.py`
- Modify: `studies/spacetime/schwarzschild_photon_sphere_jacobi.py`
- Modify: `tests/test_schwarzschild_photon_sphere_jacobi.py`

1. Implement circular tangent/screen construction and direct projection via full Riemann with `r` and `theta` derivatives.
2. Expose raw coarse/fine matrices and residuals; derive the corrected analytic matrix only after observing convergence.
3. Add a failing legacy phase-map/caustic expectation test based on the reconstructed matrix.
4. Correct legacy `optical_K`, explicit screen order, curvature control and dependent phase/caustic calculations minimally.
5. Run focused tests and commit GREEN implementation.

### Task 3: Deterministic artifacts and cross-controls

**Files:**
- Create: `studies/spacetime/schwarzschild-photon-sphere-riemann-conformance-results.json`
- Modify: `studies/spacetime/schwarzschild-photon-sphere-jacobi-results.json`
- Modify focused tests as needed.

1. Implement deterministic `build_result`, `render`, CLI and `--check` in the conformance module.
2. Regenerate both artifacts.
3. Verify exact/RK4 phase agreement, symplecticity, inverse, caustic graph gating, endpoint action, orientation, affine conversion and `M` scaling.
4. Require history fields that name the falsified profile and corrected convention.
5. Commit artifact/control updates.

### Task 4: Bilingual audit, theory, roadmap and source scope

**Files:**
- Create: `audit/schwarzschild-photon-sphere-riemann-conformance-report-en.md`
- Create: `audit/schwarzschild-photon-sphere-riemann-conformance-report-it.md`
- Create: `theory/spacetime/schwarzschild-photon-sphere-riemann-conformance.md`
- Modify: `audit/schwarzschild-photon-sphere-jacobi-report-en.md`
- Modify: `audit/schwarzschild-photon-sphere-jacobi-report-it.md`
- Modify: `theory/spacetime/schwarzschild-photon-sphere-jacobi.md`
- Modify: `docs/roadmap.md`
- Modify: `references/verification-log.md`
- Create report/source tests.

1. Write tests first for exact bilingual labels, matrices, numbers, limitations, source keys and forbidden overclaims.
2. Confirm RED.
3. Add aligned documents, preserving the PR #90 result as falsified history and PR #95 context.
4. Keep canonical source scope bounded to `Schwarzschild2003Translation`, `Darwin1959GravityField`, `Sachs1961`.
5. Commit audit/docs.

### Task 5: Direct review, full verification, PR/CI/Hermes

1. Inspect `git diff main...HEAD`, test/source assertions and generated artifacts directly; record `DIRECT_REVIEW_NO_SUBAGENT`.
2. Run focused suites, both artifact `--check` commands, `python3 -m unittest discover -s tests`, extraction/inventory checks and `git diff --check`.
3. Push branch SHA, open PR, watch `tests` and `latex`.
4. Auto-merge only if all checks are green and correction remains conservative/unambiguous.
5. Verify main CI, write a timestamped Hermes Inbox note, remove worktree and local/remote branch.
6. Do not cancel loop unless the binding stop/reformulation conditions are met; this bounded correction is not a structural dead end.
