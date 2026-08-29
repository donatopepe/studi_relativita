# Canonical phase Magnus control implementation plan

1. Add focused tests in `tests/test_plane_wave_magnus_phase_holonomy.py` for commutator identity, reversal behavior of `Omega_1/Omega_2`, full-map reciprocity and spectral collision, constant-profile collapse, orientation covariance, affine orbit, profile sensitivity and deterministic nonconfirmatory status. Run and preserve missing-module RED.
2. Implement `studies/spacetime/plane_wave_magnus_phase_holonomy.py` with explicit `4x4` algebra, deterministic quadrature and existing exact Jacobi propagator helpers. Retain raw profile samples, `M`, Magnus terms, full blocks/map, characteristic polynomial, finite window and scaling transforms.
3. Run focused tests and correct bounded sign/order/unit errors. Preserve any failed expectation and correction in audit history.
4. Generate `studies/spacetime/plane-wave-magnus-phase-holonomy-results.json` deterministically.
5. Add `theory/spacetime/plane-wave-magnus-phase-holonomy.md`, bilingual audit reports, and report parity tests. Keep source scope exact and distinguish phase-generator ordering from four-dimensional Levi-Civita loop holonomy.
6. Run new and related artifact checks, full unittest suite, extraction, inventory, legacy identifiability, `git diff --check`, and local LaTeX if available.
7. Commit and push. Open PR; require GitHub tests and LaTeX green. Auto-merge only if result remains conservative, negative, unambiguous, and all checks pass.
8. Pull merged `main`, rerun deterministic artifact and full suite, update Hermes, remove worktree/branch. Keep loop active because structural-dead-end criteria remain unmet.
