# Plane-wave Sachs optical-scalar quotient plan

1. Add failing tests for direct `DB^{-1}` decomposition, Riccati residual, zero twist, common-rotation invariants, additive observer shear mobility, caustic guard, source/observer reversal exchange, affine scaling, deterministic artifact, and absent `ell0`.
2. Implement `studies/spacetime/plane_wave_sachs_optics.py` from full Jacobi blocks, with no independent abstract optical profile. Generate deterministic JSON including raw matrices and quotient residuals.
3. Add theory note and bilingual audits with exact ledger parity, source scope, boundary/screen/caustic conditions, nuisance classification, limitations, and no-dead-end statement.
4. Run focused tests, artifact check, full unittest suite, explicit numeric audit, and `git diff --check`.
5. Commit, push, open PR, wait for tests/LaTeX CI, merge only if green, rerun post-merge checks, update Hermes, then remove worktree and branches.
