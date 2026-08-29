# Plane-wave common-anchor handedness implementation plan

1. Add focused tests for the antisymmetric handed statistic under reversal, common `SO(2)` rotations, common reflections, independent endpoint transpose equivalence, affine/profile rescaling, missing `ell0`, and deterministic artifact. Run RED and preserve missing-module failure.
2. Implement minimal exact control in `studies/spacetime/plane_wave_common_anchor.py`, reusing the same plane-wave/Jacobi conventions. Generate deterministic JSON and run focused GREEN tests.
3. Add theory note and bilingual audits with identical status/classification/conclusion, explicit distinction between mathematical parallel-screen trivialization and physical observational anchor, and no dead-end claim. Add report parity tests RED/GREEN.
4. Run artifact check, complete unittest discovery, numerical identity audit, and `git diff --check`.
5. Commit, push, open PR, wait for tests and LaTeX CI. Merge only if green and conservative. Pull main, rerun post-merge suite/check, update Hermes, and remove temporary branch/worktree.
