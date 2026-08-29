# Canonical rotating-screen plan

1. Add failing tests for zero-connection collapse, canonical-generator endpoint equivalence, velocity/canonical conversion, standard versus pulled-back symplecticity, characteristic non-equivalence, endpoint angular-velocity calibration mobility, common-basis covariance, affine collision, and deterministic artifact.
2. Implement canonical `(x,p)` generator, endpoint maps, velocity-to-canonical transformations, symplectic residuals, endpoint-calibration counterexample, and scale orbit by reusing exact-plane-wave controls.
3. Correct PR #77 theory/audits/artifact: keep velocity equation/map, relabel characteristic polynomial as velocity-coordinate diagnostic, add canonical-map pointer and supersession ledger.
4. Add bilingual theory/audits with raw variables, equations, source limits, classification/status/gate parity, and no-dead-end scope.
5. Run deterministic checks for old/new artifacts, complete suite, numeric audit, bilingual parity, and `git diff --check`.
6. Commit, push, open PR, await green CI/LaTeX, conservative auto-merge, rerun on main, update Hermes, remove worktree/branches.
