# Plane-wave connection-path cross-channel implementation plan

1. Add `tests/test_plane_wave_connection_path_cross_channel.py` with failing API tests for endpoint-matched connection histories, transported-window mobility, covariant map/Sachs collision, naive-map mobility, orientation/parity, affine collision, caustic gate and deterministic artifact.
2. Run focused tests and preserve expected missing-module failure.
3. Implement `studies/spacetime/plane_wave_connection_path_cross_channel.py` by reusing exact profile, matrix integration, screen rotations, canonical endpoint graphs and non-vertex Sachs boundaries. Keep raw matrices and histories in JSON.
4. Run focused numerical tests; correct only bounded sign/convention/tolerance errors with provenance retained.
5. Add English/Italian audit reports and theory note. Add report parity tests asserting identical classification, status, gate, equations, source scope, numeric controls and no-detection language.
6. Generate artifact twice and run `--check`; run related artifacts, focused tests, full unittest discovery, `git diff --check`, and LaTeX workflow commands.
7. Commit and push exact SHA; open PR. Auto-merge only if review is unambiguous and all GitHub tests/LaTeX checks are green.
8. After merge, update local `main`, rerun deterministic checks and full suite, update Hermes, remove worktree and branch. Preserve `UNPROVEN`, `NO_POSITIVE_DETECTION_CLAIM`, and no structural-dead-end decision.
