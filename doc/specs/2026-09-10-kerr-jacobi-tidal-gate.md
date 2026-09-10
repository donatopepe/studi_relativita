# Kerr finite-boundary Jacobi tidal-map gate

## Status

`RATIFIED_FOR_IMPLEMENTATION_PLANNING`

Human authorized continuation after PR #109. Parallel screen transport passed but its endpoint quotient had rank zero, so the next smallest solution is geodesic deviation on that verified screen.

## MVP-first gate

**Objective:** determine whether the full `4x4` Jacobi phase map along finite equatorial Kerr paths adds orientation-sensitive focusing/shear beyond the identity screen quotient while preserving symplecticity, Schwarzschild conformance, and exact geometric scale blindness.

**Metric and threshold:** correctness over eight preregistered curvature/Jacobi/scale controls; threshold `8/8`.

**Cases/order:** source formula, optical tidal symmetry/vacuum trace, Schwarzschild profile conformance, phase symplecticity, turning/reversal/convergence, orientation shape, source preparations/caustic gate, scale/rank/no-`ell0`.

**Baseline/scenarios:**

| ID | chi | orientation | rho | Rs/M | Ro/M | purpose |
|---|---:|---:|---:|---:|---:|---|
| J01 | 0.6 | +1 | 4.5 | 12 | 15 | prograde-like anchor |
| J02 | 0.6 | -1 | 4.5 | 12 | 15 | retrograde-like counterexample |
| J03 | 0.0 | +1 | 4.5 | 12 | 15 | Schwarzschild conformance |
| J04 | 0.6 | +1 | 4.5 | 12 | 12 | equal-endpoint control |
| J05 | 0.6 | +1 | 4.5 | 12 | 15 | geometric scale factor 2.5 |
| J06 | 0.6 | +1 | 4.5 | 12 | 15 | reverse/turning composition |

**MVP:** exact vacuum optical curvature amplitude in the transported equatorial screen, direct RK4 full phase-map integration, vertex/parallel source preparations, and local rank. No general non-equatorial complex phase, physical source size, detector, covariance, data, or 5D Kerr solution.

## Curvature source and convention

Boero and Moreschi, *Efficient gravitational lens optical scalars calculation of black holes with angular momentum*, MNRAS 492 (2020) 3763–3778, DOI `10.1093/mnras/stz3615`, arXiv `1910.01984` v2:

- equations `(1)`–`(12)` give null geodesic deviation and vacuum optical curvature matrix;
- equations `(106)`–`(127)` establish the parallel-propagated type-D/Walker–Penrose construction and relation to Carter's constant;
- equation `(119)` gives exact Kerr `Psi_0` along any null geodesic;
- equation `(126)` fixes the modulus relation to Carter's constant.

For equatorial `theta=pi/2`, `Q=0`, `E=1`, and real transported screen convention fixed by PR #109, preregister

```text
K_screen=diag(-A,+A)
A=3*M*(xi-a)^2/r^5
```

The sign/order must be checked by exact `chi=0` agreement with the existing independently reconstructed Schwarzschild screen profile. Any mismatch stops implementation; no post-hoc sign tuning.

## Phase map

Evolve

```text
d/dlambda [X;V] = [[0,I],[K_screen,0]] [X;V]
P_source=I_4
```

through incoming/turning/outgoing segments using the same signed-`y` regularization. Keep full

```text
P=[[A_block,B_block],[C_block,D_block]]
```

primary through caustics. Graph `D*B^-1` is emitted only when `B` is nonsingular.

## Eight controls

1. Source metadata/equation scope and exact equatorial reduction.
2. `K_screen` symmetric and vacuum trace zero at every sample.
3. `chi=0` profile and phase map agree with Schwarzschild implementation under identical endpoints/normalization/conversion.
4. Full phase map symplectic residual below `3e-7`.
5. Coarse/fine, reverse-inverse, and turning-composition residuals below `3e-6`.
6. Fixed-spin orientations differ in phase-map shape; simultaneous spin/orientation reversal obeys declared screen action.
7. Vertex and parallel preparations remain distinct; caustic/singular graph never invalidates finite full phase map.
8. Joint dilation preserves dimensionless converted phase map; `log_M` is exact null; no `ell0`.

## Expected result

```text
KERR_FINITE_BOUNDARY_JACOBI_PHASE_MAP_ADDS_ORIENTATION_SENSITIVE_FOCUSING_AND_SHEAR_BEYOND_IDENTITY_SCREEN_QUOTIENT_BUT_JOINT_DILATION_RETAINS_SCALE_BLINDNESS_NOT_ELL0
```

If orientation maps collide, preserve that negative instead. Physical gate:

```text
PHYSICAL_KERR_JACOBI_SOURCE_SIZE_PROFILE_SCREEN_PREPARATION_POLARIZATION_ANALYZER_CAUSTIC_CONTINUATION_RECEIVER_NOISE_JOINT_COVARIANCE_DATA_5D_KERR_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```

## Required runner matrix

Add one scenario manifest and one runner supporting:

```text
--mode total
--mode granular --scenario J01
--mode granular --category conformance|orientation|scale
--report-json PATH
```

Report PASS/FAIL per case and fail closed on missing handlers. This runner is supplementary; unit tests and stable scientific artifact remain authoritative.

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
