# Screen-connection holonomy quotient implementation plan

1. Add focused failing tests for ordered/analytic Wilson equality, intermediate-path mobility, endpoint relative collision, trace sign/winding aliasing, canonical endpoint-loop collision, zero connection, orientation/parity, affine orbit and deterministic artifact.
2. Run tests and preserve missing-module RED evidence.
3. Implement `studies/spacetime/plane_wave_screen_connection_holonomy.py`, reusing endpoint-matched prescribed connection histories and canonical endpoint maps. Retain raw sampled holonomies, angles, matrices, traces, eigenvalue pairs and relative loops.
4. Run focused tests. Correct only bounded sign/order/unit issues; preserve failures.
5. Add English theory note, bilingual audits and semantic-parity tests. State exact source scope and distinguish prescribed screen `SO(2)` connection from four-dimensional Levi-Civita holonomy.
6. Run new and related deterministic artifact checks, full unittest suite, extraction/inventory/legacy checks, `git diff --check`, and available local LaTeX.
7. Commit, push and open PR. Require GitHub tests and LaTeX green before conservative auto-merge.
8. Pull merged `main`, rerun full checks, update Hermes, remove branch/worktree. Keep loop active: structural-dead-end criteria do not pass.
