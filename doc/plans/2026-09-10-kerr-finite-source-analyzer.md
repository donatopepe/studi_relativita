# Kerr finite source/analyzer implementation plan

**Objective:** test finite Gaussian source covariance and ideal analyzer projection on the verified Kerr Jacobi phase map.

**Metric:** exactly `8/8` controls.

**MVP:** standard-library covariance propagation and scalar analyzer scan; no detector/noise model.

**Escalation:** receiver likelihood only after this preparation gate is GREEN.

## Task 1 — Spec and scenario RED

Add structural/spec tests and J07–J14 manifest expectations. Extend runner handlers only after RED is preserved. Test total `14/14`, each scenario and every category. Commit GREEN.

## Task 2 — Scientific controls RED

Add tests for domain, propagation/SPD, width homogeneity, orientation, extrema, basis covariance, scalar collision, scale/rank/nonclaims and deterministic artifact. Commit RED.

## Task 3 — Source/analyzer engine

Create module reusing Kerr Jacobi map. Implement dimensionless conversion, covariance algebra, eigenvalues, analyzer scan/collision, rotation, scale/rank. GREEN and commit.

## Task 4 — Artifacts and runner

Generate bounded scientific artifact and stable total scenario report. Keep full raw covariance primary; avoid checkpoint dumps. Validate total and granular. Commit.

## Task 5 — Reports and closure

Add theory, EN/IT audit, roadmap/ledger, report tests; update TODO after each milestone. Run CodeGraph sync, UTF-8, focused/full suites, deterministic and granular batteries, CI, Hermes. Work only on main.
