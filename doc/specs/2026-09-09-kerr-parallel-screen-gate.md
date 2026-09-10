# Kerr finite-boundary parallel-screen transport gate

## Status

`RATIFIED_FOR_IMPLEMENTATION_PLANNING`

Human authorized continuation after PR #108. The endpoint gate passed, so its explicit escalation condition selects parallel screen transport as the next MVP. This specification authorizes planning and bounded implementation, not detector or evidence claims.

## MVP-first gate

**Objective:** determine whether a source ZAMO screen parallel transported along the existing finite equatorial Kerr null path reaches the observer as a metric-compatible screen map with orientation-sensitive but scale-blind endpoint holonomy.

**Metric and threshold:** correctness over eight preregistered transport/convention/scale controls; threshold `8/8`.

**Cases/order:** connection/metric compatibility, geodesic-tangent transport, screen orthonormality/transversality, source-to-observer screen map, reversal, orientation convention, Schwarzschild limit, joint dilation/rank/no-`ell0`.

**Baseline:** reuse PR #108 `M=1`, `chi=0.6`, `rho=4.5`, equal endpoint radii `12M`, orientations `+/-1`; add unequal endpoint control `R_source=12M`, `R_observer=15M`; RK4 resolutions `400/800`; screen order `(polar,equatorial-transverse)`.

**MVP:** direct Levi-Civita parallel transport of source ZAMO screen and null tangent along existing regularized path. No Riemann optical tidal matrix, Jacobi phase map, source polarization, detector analyzer, covariance, data, or 5D Kerr metric.

**Escalation condition:** add Jacobi/Sachs dynamics only after this transport baseline is `8/8`; otherwise fix the named connection/frame/path defect.

## Screen construction

At source, PR #108 provides ZAMO basis `(e_r,e_theta,e_phi)` and unit local ray direction `n=(n_r,0,n_phi)`. Define

```text
s_1=e_theta
s_2=n_phi*e_r-n_r*e_phi
```

with declared order `(polar,equatorial-transverse)`. Verify `g(s_A,s_B)=delta_AB` and `g(s_A,k)=0`.

Transport each vector with

```text
k^nu nabla_nu s_A^mu=0
```

using analytic equatorial Kerr metric radial derivatives and Levi-Civita connection. Simultaneously transport `k` as a numerical geodesic-conformance control. Parameterize the complete incoming/outgoing path by signed `y`, with `r=r_turn+y^2`, and use analytic turning limits.

At observer, compare transported screen to the observer ZAMO endpoint screen:

```text
Q_AB=g(s_A^transported,s_B^observer)
```

`Q` is a coordinate/frame endpoint map, not a detector Jones matrix. Equal endpoint radii may be a symmetry/null control; unequal endpoints prevent accepting only an accidental identity map.

## Sources

- `GrallaLupsasca2020KerrNullGeodesics`: path/tangent and turning structure, equations `(1)`–`(13f)`.
- `Dolan2018GeometricalOptics`: leading null rays and parallel-propagated polarization/screen vectors; inspect geometrical-optics sections 3.1–3.3 and null-tetrad/lensing Sec. 4.1, including the parallel-transport statements around equations `(20)`–`(28)`.

Neither source defines this ZAMO joining, screen order, RK4 implementation, detector, polarization preparation, analyzer, covariance, 5D comparator, `ell0`, UMCH, evidence, or detection.

## Eight controls

1. **Levi-Civita connection:** lower-index metric compatibility at sampled points and Christoffel lower-index symmetry below `2e-10`.
2. **Geodesic tangent:** transported source `k` agrees with analytic observer `k`; residual below `2e-8`.
3. **Screen preservation:** transported screen remains orthonormal and transverse to analytic `k`; residual below `2e-8`.
4. **Endpoint map/convergence:** `Q^T Q=I`, `det Q=+1`, and coarse/fine `Q` residual below `2e-8`; include unequal endpoint case.
5. **Path reversal:** observer-to-source reverse transport composes with forward transport to identity below `2e-8`.
6. **Spin/orientation convention:** simultaneous `(a,orientation)->(-a,-orientation)` obeys preregistered screen sign action; fixed positive spin branches retain distinct path labels even if equatorial reflection makes the screen quotient collide.
7. **Schwarzschild limit:** opposite orientations have the expected reflection-related screen map and identical unsigned transport invariants below `2e-8`.
8. **Joint dilation/rank/no-`ell0`:** dimensionless screen map is invariant under joint scaling; `log_M` is exact null. No raw map entry is an independent physical channel or `ell0`.

## Expected bounded outcomes

If a nontrivial rotation survives:

```text
KERR_FINITE_BOUNDARY_PARALLEL_SCREEN_HAS_ORIENTATION_SENSITIVE_ENDPOINT_ROTATION_BUT_JOINT_DILATION_RETAINS_SCALE_BLINDNESS_NOT_ELL0
```

If equatorial symmetry forces a quotient collision:

```text
KERR_EQUATORIAL_FINITE_BOUNDARY_PARALLEL_SCREEN_TRANSPORT_IS_METRIC_COMPATIBLE_BUT_ENDPOINT_SCREEN_QUOTIENT_COLLIDES_UNDER_EQUATORIAL_SYMMETRY_WHILE_JOINT_DILATION_RETAINS_SCALE_BLINDNESS_NOT_ELL0
```

Both are valid scientific results. Physical gate:

```text
PHYSICAL_KERR_SCREEN_PREPARATION_POLARIZATION_SOURCE_ANALYZER_JACOBI_TIDAL_MAP_CAUSTICS_RECEIVER_NOISE_JOINT_COVARIANCE_DATA_5D_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```

## Nonclaims

```text
UMCH=UNPROVEN_SECONDARY_CANDIDATE
L_identified=false
ell0_identified=false
L_equals_ell0=NOT_DERIVED
extra_dimension_detected=false
structural_dead_end=NOT_DECLARED
NO_POSITIVE_DETECTION_CLAIM
```
