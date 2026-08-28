# Jacobi thin-lens profile-location gate

## Question

Does integrated optical focusing strength determine endpoint Jacobi map or caustic when curvature location along path is free?

## Exact distributional control

Use scalar Jacobi equation `d''+k delta(s-a)d=0` with vertex data `d(0)=0,d'(0)=1`, observer at `S>a>0`. Before lens, `d=s`. Across lens, `d` is continuous and derivative jumps `d'(a+)=d'(a-)-k d(a)=1-ka`. After lens,

`d(s)=a+(1-ka)(s-a)`.

Endpoint value is `d(S)=S-k a(S-a)`. Total integrated strength is always `k`, but moving lens location changes endpoint and subsequent zero.

For `ka>1`, first post-lens caustic is `s_c=a+a/(ka-1)`. For fixed positive `k`, caustic exists only when `a>1/k` and varies with `a`; same integrated strength is insufficient.

This is idealized thin-lens distributional scalar optics, not smooth exact spacetime.

## Gates

Need ordered optical profile, affine normalization, screen transport and source/observer boundaries. Profile-location landmark is geometric/path nuisance; `ell0` absent.

## Decision

Status `JACOBI_INTEGRATED_FOCUSING_INSUFFICIENT_PROFILE_LOCATION_REQUIRED`. No reformulation: smooth exact varying-matrix optics remain open. `UNPROVEN`; `NO_POSITIVE_DETECTION_CLAIM`.
