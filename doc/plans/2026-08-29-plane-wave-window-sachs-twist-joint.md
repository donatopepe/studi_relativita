# Plane-wave window/Sachs-twist joint plan

1. Add failing tests for raw joint object, top-hat/triangular affine collisions, boundary mobility with unchanged window, movable landmark, profile sensitivity, absent `ell0`, and deterministic artifact.
2. Implement by composing exact finite-window and non-vertex Sachs modules; preserve full matrices and dimensionally correct boundary scaling.
3. Add bilingual audits and theory with exact ledger parity, source limits, support/kernel/boundary/screen nuisance, limits, and no-dead-end statement.
4. Run focused tests, artifact check, full suite, explicit numeric audit, and `git diff --check`.
5. Commit, push, open PR, require green tests/LaTeX, merge only if conservative, rerun post-merge tests, update Hermes, clean worktree/branches.
