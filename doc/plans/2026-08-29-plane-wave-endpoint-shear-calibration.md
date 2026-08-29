# Plane-wave endpoint shear-calibration implementation plan

1. Add failing tests for symplectic endpoint shears, exact block action, additive optical-matrix nuisance, movable endpoint spectra, affine-scale degeneracy, and absent `ell0`.
2. Implement pure-Python exact-map control reusing `plane_wave_full_jacobi.py`; generate deterministic JSON.
3. Add bilingual audits and theory note with raw blocks, nuisance scope, canonical-source limitations, negative status, and no-dead-end statement.
4. Run focused tests, artifact check, full suite, numeric audit, and `git diff --check`.
5. Commit, push, open PR, wait for tests/LaTeX CI, conservatively merge if green, update Hermes, and remove worktree/branch.
