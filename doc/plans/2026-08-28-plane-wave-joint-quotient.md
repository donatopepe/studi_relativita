# Plane-wave joint quotient implementation plan

1. Add `tests/test_plane_wave_joint_quotient.py` specifying raw reversal sensitivity, equality of `W`, transpose reciprocity, quotient invariant equality, exact affine rescaling, missing `ell0`, and deterministic artifact. Run it and preserve missing-module RED.
2. Implement minimal numerical study in `studies/spacetime/plane_wave_joint_quotient.py`, reusing the declared exact plane-wave profile and RK4 conventions. Generate `studies/spacetime/plane-wave-joint-quotient-results.json`; run focused GREEN tests.
3. Add bilingual audit reports and theory note. Add report parity tests for identical status/classification/conclusion and explicit common-anchor limitation; run focused tests.
4. Run deterministic `--check`, complete unittest discovery, `git diff --check`, and inspect artifact tolerances and source scope.
5. Commit, push, open PR, wait for both tests and LaTeX CI. Auto-merge only if all checks are green and result remains a conservative negative exact control. Update main and Hermes, rerun post-merge checks, remove branch/worktree.
