# Continuous screen-readout quotient implementation plan

1. Add failing tests for endpoint collision, intermediate raw-history mobility, pointwise local gauge relation, inertial reconstruction, zero-path collapse, orientation/parity, affine orbit, raw history retention and deterministic artifact.
2. Run focused tests; preserve missing-module RED failure.
3. Implement deterministic sampled partial propagators in `studies/spacetime/plane_wave_continuous_screen_readout.py`, reusing exact plane-wave profile and endpoint-matched paths. Keep full matrices at preregistered sample points.
4. Run focused tests and correct bounded sign/order/convention issues only.
5. Add bilingual audits, theory note and report parity tests with exact classification/status/gate/equations/numerics/source limitations.
6. Run new and related deterministic artifacts, full unittest suite, extraction/inventory/legacy checks, `git diff --check`, and available LaTeX checks.
7. Commit, push and open PR. Require all GitHub tests and LaTeX green before conservative auto-merge.
8. Update `main`, rerun full post-merge verification, update Hermes and remove worktree/branch. Keep loop active because structural-dead-end criteria do not pass.
