# Kerr finite-sample covariance uncertainty plan

**Objective:** derive exact Gaussian covariance-estimation RMS and conservative branch-separation risk bound.

**Metric:** `8/8`.

1. Ratify known-zero-mean Wishart identity, four independent estimates, counts `[16,64,256]`, risk `0.05`, J71-J78 and nonclaims.
2. Add RED controls and extend authoritative matrix/runner fail-closed.
3. Implement analytic finite-sample engine reusing correlated-noise covariances and threshold.
4. Generate deterministic artifact and theory/EN/IT record.
5. Run focused/full, total/all granular, deterministic, UTF-8, diff, CodeGraph and CI gates; publish only green.

No new tool needed; reuse Kerr runner and shared Hermes UTF-8 validator.
