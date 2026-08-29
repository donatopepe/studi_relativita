# Plane-wave joint window/full-map common-spectrum plan

1. Add failing tests in `tests/test_plane_wave_joint_common_spectrum.py` for top-hat and triangular exact joint scale collisions, block scaling/canonical similarity, profile sensitivity, shifted landmark coordinate, deterministic artifact, and absent `ell0`.
2. Implement `studies/spacetime/plane_wave_joint_common_spectrum.py`, reusing exact plane-wave window/Jacobi utilities. Record raw matrices, characteristic polynomial, numeric residuals, classification, source scope, and negative status in deterministic JSON.
3. Add `theory/spacetime/plane-wave-joint-common-spectrum.md` plus bilingual audit reports and parity tests. State group, support, kernel, boundary, affine/profile orbit, raw/dependent object distinction, canonical-source scope, open alternatives, and no-dead-end decision.
4. Run focused red/green tests, artifact `--check`, full unittest suite, explicit numerical audit, and `git diff --check`.
5. Commit and push one conservative branch, open PR, require tests and LaTeX CI green, merge, rerun post-merge checks, update Hermes, and remove temporary worktree/branches.
