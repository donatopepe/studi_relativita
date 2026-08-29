# Plane-wave Sachs endpoint-shear transfer plan

1. Add failing tests for exact source-shear absorption, observer-shift law, uncompensated source sensitivity, twist invariance, affine/profile scaling, caustic guard, profile sensitivity, absent `ell0`, and deterministic artifact.
2. Implement raw phase-space graph propagation by composing existing exact full-Jacobi, endpoint-shear, and non-vertex Sachs modules. Preserve `P,X,V,S,S_0,H_s,H_o`.
3. Add bilingual audits and theory with identical classification/status/gate, equations, source scope, dimensional rules, alternatives, and no-dead-end limitation.
4. Run focused tests after each red/green step, artifact `--check`, full suite, numeric audit, `git diff --check`, and repository CI.
5. Commit, push, open PR. Auto-merge only after tests and LaTeX are green. Rerun complete verification on merged `main`, update Hermes, remove worktree and branches.
