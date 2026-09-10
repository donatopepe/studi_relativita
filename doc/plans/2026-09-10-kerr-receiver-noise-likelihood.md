# Kerr receiver/noise likelihood implementation plan

**Objective:** test fixed Gaussian receiver distinguishability and calibration-nuisance collision.

**Metric:** `8/8`.

**MVP:** exact 2D Gaussian covariance/log-likelihood/KL; deterministic quadrature only for conformance.

## Task 1 — Source/spec tests

Add Kullback–Leibler and NIST metadata/log scope; structural spec tests. Commit GREEN.

## Task 2 — Scenario RED

Extend matrix J15–J22 and runner categories/handlers; require total `22/22`, all scenario/category granular, JSON report, fail-closed. Commit RED expectations then GREEN handlers.

## Task 3 — Receiver engine RED/GREEN

Tests then module for covariance, density, KL, noise scan, expected LLR, basis covariance, nuisance collision, scale/null. Deterministic artifact. Commit each validated code change.

## Task 4 — Reports/closure

Reports, theory, roadmap/ledger, TODO. CodeGraph, UTF-8, focused/full suite, total/granular, deterministic checks, push/CI, Hermes. Main only.
