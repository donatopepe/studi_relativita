# Schwarzschild radar cross-channel rank implementation plan

> Execute directly without subagents under binding user instruction. Preserve RED output and bounded interpretations.

**Goal:** Determine whether joint radar duration and radial Levi-Civita boost provide local dimensionless endpoint rank, then test orientation quotient, global collisions and absolute-scale loss.

**Architecture:** Reuse deterministic radar transport. New dependency-free module extracts signed boost rapidity, verifies boost reconstruction, computes centered finite-difference Jacobians/SVD analytically for 2x2 matrices, follows fixed-duration tangents, scans declared endpoint domain, and emits sorted JSON. Reports separate raw local rank from statistical channel independence and global/absolute identifiability.

## Task 1 — Scientific RED

Create `tests/test_schwarzschild_radar_cross_channel_rank.py` requiring:

- rapidity/reconstruction and numerical transport agreement;
- duration rank one and nonzero holonomy derivative along duration collision;
- raw dimensionless Jacobian rank two at baseline;
- reversal/characteristic global collision despite quotient-local rank;
- common-anchor conjugacy;
- three-variable scale null direction and changed proper time;
- deterministic grid scan, shrinking/flat rank loss;
- raw record and no-claim states.

Run missing-module RED; commit.

## Task 2 — Rank GREEN

Create module and deterministic artifact. Use stable centered differences with convergence check. Implement exact 2x2 singular values from eigenvalues of `J^T J`. Preserve sample domain, step, tolerance and scan extrema. Run focused tests; commit.

## Task 3 — Source scope

Reuse audited Schwarzschild, Ambrose--Singer and Lin sources. Add a source only if a novel known result beyond basic Lorentz boost algebra is used. Add focused test that current logs exclude cross-channel independence, endpoint rank, detector covariance and `ell0` claims.

## Task 4 — Bilingual authority

Write report contract first. Add theory and aligned English/Italian audits, plus conservative roadmap note. Include exact labels, equations, rank values, collisions, source scope and all limitations. Commit after focused public-doc tests.

## Task 5 — Verification and delivery

Run artifacts, focused exact controls, full suite, extraction, inventory, legacy identifiability and diff checks. Push PR; require duplicate tests/LaTeX CI green. Auto-merge only bounded negative result. Sync main, run post-merge tests, write Hermes Inbox note, remove worktree/branch. Keep durable loop active because dead-end criteria remain unmet.
