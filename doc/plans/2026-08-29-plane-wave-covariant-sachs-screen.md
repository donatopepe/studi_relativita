# Covariant rotating-screen Sachs plan

1. Add failing tests for zero-connection collapse, inertial/canonical graph covariance, `S_rot=R-A`, direct canonical boundary propagation, twist connection shift, endpoint-rate calibration mobility, common `SO(2)` and `O(2)` parity, affine collision, caustic gate, and deterministic artifact.
2. Implement raw `Y,U,X,P,R,S_rot,S_0,Q,A` control by reusing exact Jacobi and canonical screen propagators.
3. Add Riccati and twist decomposition checks; preserve old inertial twist-area result and record exact scope.
4. Add bilingual theory/audits with equations, source limits, classification/status/gate parity, correction ledger, and no-dead-end scope.
5. Run deterministic old/new artifacts, complete suite, numerical checks, bilingual parity, and `git diff --check`.
6. Commit, push, open PR, wait for green tests/LaTeX, conservative auto-merge, rerun on main, update Hermes, remove worktree/branches.
