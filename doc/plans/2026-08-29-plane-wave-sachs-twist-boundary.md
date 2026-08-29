# Plane-wave Sachs twist-boundary plan

1. Add failing tests for non-vertex propagation, Riccati decomposition, twist-area conservation, boundary-amplitude mobility, `SO(2)` invariance/`O(2)` sign reversal, affine/profile orbit, profile sensitivity, caustic guard, absent `ell0`, and deterministic artifact.
2. Implement `plane_wave_sachs_twist_boundary.py` by reusing exact RK4 Jacobi propagation; keep raw `X,V,S` and boundary matrix.
3. Add bilingual audits and theory with exact ledger parity, source scope, parity/boundary/scale nuisance, limits, and no-dead-end statement.
4. Run focused tests, artifact check, full suite, numeric audit, and `git diff --check`.
5. Commit, push, open PR, require green tests/LaTeX, merge only if conservative and green, rerun post-merge suite, update Hermes, clean worktree/branches.
