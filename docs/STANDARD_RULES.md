# Standard project rules

Updated: 2026-09-10

1. Work only in primary `main` checkout. Do not create or use worktrees.
2. Before analysis or edits, verify/sync CodeGraph and use `query`, `explore`, or `node` for impact.
3. Start with smallest useful MVP: one objective, one metric/threshold pair, fixed cases/order.
4. Use direct agent path; no subagents unless user explicitly requests them.
5. Seek root cause and concrete solution; do not stop at problem description. Change one measured variable per iteration.
6. Validate each code change with focused tests, then commit immediately. Do not accumulate validated uncommitted code.
7. Every simulation family must have one authoritative scenario matrix plus reusable runner supporting total, scenario, and category modes with machine-readable report and fail-closed missing handlers.
8. Preserve deterministic artifacts, explicit thresholds, negative results, provenance, source scope, and scientific nonclaims.
9. Keep text UTF-8. Run automated encoding/mojibake validation; auto-fix only unambiguous reversible cases.
10. Never store secrets in repository, CodeGraph, logs, artifacts, or Hermes memory.
11. Before completion: focused and full tests, total and granular scenario runs, deterministic checks, `git diff --check`, UTF-8 validation, CodeGraph sync, clean status, remote CI when published.
12. Update this file and project memory whenever global rules change; verify propagation through tests.
