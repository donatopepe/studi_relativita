# Plane-wave full Jacobi-map quotient implementation plan

1. Add focused tests for four-block propagation, symplecticity, reversal reciprocity, labelled endpoint optical-spectrum swap, endpoint-swap quotient equivalence, affine/profile dimensionless scaling, absent `ell0`, and deterministic artifact. Run RED; preserve missing-module/artifact failure.
2. Implement `studies/spacetime/plane_wave_full_jacobi.py` with pure-Python 2x2/4x4 helpers, reuse exact profile and RK4 integrator, preserve raw blocks, and generate deterministic JSON. Run focused GREEN tests.
3. Add theory note and bilingual audit reports with exact status/classification/open gates, canonical-source limitation, raw-versus-derived distinction, boundary-label dependence, and no structural-dead-end claim. Add report parity tests RED then GREEN.
4. Run artifact `--check`, full unittest discovery, exact residual audit, and `git diff --check`.
5. Commit and push one conservative change, open PR, require green tests and LaTeX CI, merge, update main, rerun post-merge checks, append Hermes, remove worktree and local/remote branch. Keep loop active unless dead-end criteria unexpectedly pass.
