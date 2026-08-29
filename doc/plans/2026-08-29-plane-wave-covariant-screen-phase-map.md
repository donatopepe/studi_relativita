# Covariant rotating-screen phase-map correction plan

1. Write failing tests for zero-connection collapse, direct-generator/endpoint-graph equivalence, naive-map counterexample, common-basis covariance, right-anchor covariance, affine collision, deterministic artifact, and explicit supersession ledger.
2. Implement analytic `A,A'`, rotating first-order generator, RK4 phase-map integration, endpoint state maps `G_s,G_o`, corrected `P_covariant`, and residual controls.
3. Rename previous `P_transport` outputs and documentation to `P_naive_conjugated_profile`; preserve finite-window results while superseding rotating-coordinate interpretation.
4. Add bilingual theory/audits with exact equations, source scope, correction history, classification/status/gate parity, and no-dead-end language.
5. Run deterministic check, complete test suite, numerical audit, bilingual parity, and `git diff --check`.
6. Commit, push, open PR, await green CI/LaTeX, conservatively auto-merge, rerun verification on merged main, update Hermes, and clean branch/worktree.
