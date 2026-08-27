# Correcting UMCH operational assumptions

## Authorized correction scope

Correct assumptions that are definitional or protocol-level without inventing evidence. Do not resolve assumptions requiring external physics, data, calibration, or human scientific validation.

## Corrections

### Domain circularity

Separate two domains:

- survey domain `D_survey`: preregistered physical scales `ell` selected independently of unknown `ell0`;
- model support: candidate parameter values must satisfy `ell0<=ell_min` for every sample used by a family defined only at `x>=1`.

No observation is discarded after fitting because inferred `ell0` exceeds its scale. Such parameter value/family receives `DOMAIN_INCONSISTENT`. This removes using unknown `ell0` to select data, but does not identify `ell0`.

### Scale and region protocol

Preregister region construction, scale estimator, channel windows/circuits, comparator, and exclusion rules independently of response values. Exact choices remain future protocol inputs.

### Channel dependence and norms

Raw vector remains primary. `C_2` and `C_infinity` are descriptive preregistered summaries, not six independent evidences and not a likelihood factorization. No independence assumption is made. Positive inference additionally requires preregistered joint covariance/dependence model; absent it, status is `DEPENDENCE_UNRESOLVED` and summaries cannot confirm.

### Family selection

All preregistered families including `F_0` are reported. A single confirmatory family must be selected/derived before data; otherwise analysis is model-comparison/exploratory only and cannot confirm.

## Unresolved assumptions

Frame uniqueness, channel-specific physical normalizations, calibrated uncertainty/nuisance models, fixed turnover shape, nonlocal mechanism, data/replication, and human review remain unresolved. No scientific status is promoted.
