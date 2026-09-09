# Kerr finite-boundary ZAMO endpoint gate

## Bounded object

`GrallaLupsasca2020KerrNullGeodesics`, equations `(1)`–`(13f)`, supports Kerr conserved quantities, radial/angular potentials, turning points, momentum reconstruction, and finite source/observer integral structure. This project restricts to equatorial `Q=0`, `E=1`, one exterior radial turning point, and two finite endpoints.

For each signed orientation, impact parameter is solved algebraically and checked by `R(r_turn)=0`. Integrals are regularized with `r=r_turn+y^2`; coarse/fine quadrature certifies coordinate time, azimuth, and affine length.

## Endpoint frame

Each endpoint uses a declared ZAMO tetrad. Its Gram matrix is tested against Minkowski signature. Photon coordinate components are projected to

```text
local_frequency=-g(k,e_(0))
local_direction=(k^(r),k^(theta),k^(phi))/local_frequency
```

and reconstructed back to coordinates. Coordinate and local null residuals vanish. ZAMO is a declared mathematical endpoint observer, not a physical emitter or physical observer. No source dynamics, receiver response, or absolute clock/frequency standard is supplied.

## Counterexamples

At fixed positive spin, opposite signed paths differ in finite-boundary duration, azimuth, affine length, local frequency, and direction. Simultaneous spin/orientation reversal preserves unsigned records and reverses azimuthal signs. At `chi=0`, opposite orientations collide in unsigned records.

Joint dilation of all dimensional geometry leaves endpoint/path features invariant after declared conversions. Feature Jacobian over `[log_M,chi,rho,R_source/M,R_observer/M]` has rank four and exact scale-null direction `[1,0,0,0,0]`.

## Result

All `8/8` preregistered controls pass:

```text
KERR_FINITE_BOUNDARY_ZAMO_ENDPOINTS_CONVERT_COORDINATE_PATHS_TO_LOCAL_DIRECTION_AND_RELATIVE_FREQUENCY_SHAPE_BUT_WITHOUT_PHYSICAL_ENDPOINT_STANDARDS_OR_SCREEN_TRANSPORT_JOINT_DILATION_RETAINS_ABSOLUTE_SCALE_BLINDNESS_NOT_ELL0
MODEL_LEVEL_KERR_ENDPOINT_CONFORMANCE_NOT_EVIDENCE
PHYSICAL_KERR_EMITTER_ABSORBER_WORLDLINES_CLOCKS_AFFINE_FREQUENCY_STANDARD_PARALLEL_SCREEN_JACOBI_PREPARATION_RECEIVER_NOISE_JOINT_COVARIANCE_DATA_5D_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```

This resolves coordinate-to-local endpoint consistency. It does not resolve parallel screen transport, Jacobi preparation, physical endpoint standards, covariance, data, 5D Kerr comparison, or `ell0`. Prior Kerr ring, 5D tensor, finite `S1`, Schwarzschild, and `F_0` records remain preserved.
