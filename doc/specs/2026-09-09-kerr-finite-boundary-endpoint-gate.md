# Kerr finite-boundary equatorial endpoint gate

## Status

`RATIFIED_FOR_IMPLEMENTATION_PLANNING`

Human authorized the recommended continuation after PR #107: move from circular coordinate orbits to the smallest finite-boundary Kerr path with explicit endpoint frames. This specification authorizes implementation planning, not physical-detection claims.

Global state remains:

```text
HIGHER_DIMENSIONAL_GRAVITY_DIRECTION=HUMAN_RATIFIED_RESEARCH_DIRECTION
MODEL=KERR_EQUATORIAL_FINITE_BOUNDARY_4D_CONTROL
UMCH=UNPROVEN_SECONDARY_CANDIDATE
L_identified=false
ell0_identified=false
L_equals_ell0=NOT_DERIVED
extra_dimension_detected=false
structural_dead_end=NOT_DECLARED
Detection=NO_POSITIVE_DETECTION_CLAIM
Maximum interpretation=MODEL_LEVEL_KERR_ENDPOINT_CONFORMANCE_NOT_EVIDENCE
```

## MVP-first gate

**Objective:** determine whether a finite-boundary equatorial Kerr null-scattering path with explicit locally nonrotating endpoint tetrads converts the orbit-level branch labels into a self-consistent local endpoint direction/frequency record while preserving geometric scale blindness.

**Metric and threshold:** correctness over eight preregistered path/endpoint/scale controls; threshold `8/8` under declared analytic or numerical tolerances.

**Cases and order:** turning impact parameter, path first integrals, locally nonrotating tetrad orthonormality, endpoint null reconstruction, branch/orientation asymmetry, Schwarzschild limit, joint dilation, and endpoint-rank/no-`ell0` gate.

**Fixed inputs/order:**

```text
M=1
chi=0.6
rho=r_turn/M=4.5
R_source/M=12
R_observer/M=12
orientation=+1 prograde-like, then -1 retrograde-like
scale_factor=2.5
quadrature coarse/fine=800/1600 after turning-point regularization
```

**MVP:** one equatorial future-null path from source radius to one exterior radial turning point and back to observer radius; conserved `E=1`, `Q=0`; one exact turning impact parameter per signed orientation; numerical path quadrature; locally nonrotating (ZAMO/LNRF) endpoint tetrads; local photon energy and spatial direction. No parallel screen/Jacobi evolution yet, no emitter/absorber dynamics, no detector, no covariance, no data.

**Escalation condition:** add parallel screen transport only if all endpoint/path controls pass and the surviving blocker is specifically lack of transported polarization/Jacobi comparison. Any source or frame ambiguity stops implementation.

## Geometry and path conventions

Use geometrized units `G=c=1`, Boyer-Lindquist coordinates `(t,r,theta,phi)`, equatorial plane `theta=pi/2`, `0<=chi<1`, `a=chi*M`, exterior radii outside `r_+=M+sqrt(M^2-a^2)`.

For `E=1`, `Q=0`, `xi=L_z/E`, use

```text
Delta=r^2-2*M*r+a^2
P=r^2+a^2-a*xi
R(r)=P^2-Delta*(xi-a)^2
Sigma=r^2
Sigma*k^t=((r^2+a^2)*P/Delta)+a*(xi-a)
Sigma*k^r=radial_sign*sqrt(R)
Sigma*k^phi=(a*P/Delta)+(xi-a)
```

The turning point requires `R(rho*M)=0`. For orientation `sigma in {-1,+1}`, preregister the algebraic root

```text
xi_turn=[r_turn^2+a^2+sigma*a*sqrt(Delta_turn)]/[a+sigma*sqrt(Delta_turn)]
```

and verify by substitution. Branch label here is the sign of endpoint azimuthal motion/local azimuthal direction, not automatically the circular-orbit prograde/retrograde label at every radius.

## Endpoint frame

At each endpoint construct a locally nonrotating/ZAMO tetrad from the equatorial Kerr metric:

```text
Sigma=r^2
Delta=r^2-2*M*r+a^2
A=(r^2+a^2)^2-a^2*Delta
alpha=sqrt(Delta*Sigma/A)
omega=2*M*a*r/A
g_phi_phi=A/Sigma

e_(0)=alpha^-1*(partial_t+omega*partial_phi)
e_(r)=sqrt(Delta/Sigma)*partial_r
e_(theta)=Sigma^-1/2*partial_theta
e_(phi)=g_phi_phi^-1/2*partial_phi
```

Verify `g(e_(a),e_(b))=eta_(ab)`. Project the photon covector/vector to local components. Require

```text
omega_local=-g(k,e_(0))>0
n_local=(k^(r),k^(theta),k^(phi))/omega_local
|n_local|=1
```

A ZAMO is a declared mathematical endpoint observer. No physical source/receiver worldline is inferred.

## Source scope

Primary path source: Gralla and Lupsasca, *Null geodesics of the Kerr exterior*, Phys. Rev. D 101, 044032 (2020), DOI `10.1103/PhysRevD.101.044032`, arXiv `1910.12881` v3. Verify equations `(1)`–`(13f)` for Kerr metric, conserved quantities, momentum reconstruction, radial/angular potentials, turning points, and source/observer integral form.

Retain `Teo2003SphericalPhotonOrbits` only for the prior circular-orbit baseline and compatible Kerr conventions. Neither source establishes this project's ZAMO endpoint protocol, detector, absolute clock/frequency standard, screen transport, covariance, `ell0`, UMCH, evidence, or detection.

## Eight counterexample-first controls

### 1. Turning impact parameter

Both signed roots must be finite and satisfy `R(r_turn)=0`. Their endpoint azimuthal directions must be checked rather than inferred from root sign.

### 2. Path first integrals and convergence

Regularize the turning endpoint with `r=r_turn+y^2`. Integrate incoming and outgoing halves. Require future `k^t>0`, nonnegative radial potential over the path, signed radial reversal, and coarse/fine convergence of `Delta_t`, `Delta_phi`, and affine length.

### 3. ZAMO tetrad orthonormality

At source and observer endpoints, maximum Gram residual must stay below tolerance. Fail if endpoint lies at/inside horizon or lapse is nonpositive.

### 4. Endpoint null reconstruction

Coordinate and local tetrad components must reconstruct each other; coordinate null residual and local `-|k^(0)|^2+|k_space|^2` residual must vanish. `omega_local>0` and `|n_local|=1`.

### 5. Orientation asymmetry and convention map

At fixed positive spin, signed orientation branches must differ in at least one dimensionless path/endpoint feature. Simultaneous `(a,orientation)->(-a,-orientation)` must preserve unsigned geometry/local-frequency records and reverse signed azimuthal direction.

```text
KERR_ENDPOINT_ORIENTATION_ASYMMETRY_IS_FRAME_DRAGGING_SHAPE_NOT_ABSOLUTE_SCALE
```

### 6. Schwarzschild limit

At `chi=0`, opposite orientations must collide in unsigned path duration, bending magnitude, local frequency, and radial local direction, while azimuthal local direction reverses.

```text
KERR_FINITE_BOUNDARY_ORIENTATION_BRANCHES_COLLIDE_IN_SCHWARZSCHILD_UNSIGNED_RECORD
```

### 7. Joint geometric dilation

Under `(M,a,r,xi,t,lambda)->s*(M,a,r,xi,t,lambda)` with fixed dimensionless endpoints and `E=1`, dimensionless path and local endpoint records remain invariant after declared component conversions.

```text
KERR_FINITE_BOUNDARY_ZAMO_RECORD_RETAINS_JOINT_GEOMETRIC_SCALE_NULL
```

### 8. Endpoint rank and no-`ell0` gate

For dimensionless endpoint/path features over parameters `[log_M,chi,rho,R_source/M,R_observer/M]`, `log_M` must remain a null column. Report other local rank without claiming global injectivity or physical identifiability. `M`, `a`, source clock, detector time, and `ell0` are not internally identified.

## Raw output contract

```text
geometry
turning_record
path_samples
Delta_t/M
Delta_phi
affine_length/M
source_ZAMO_tetrad
observer_ZAMO_tetrad
source_local_frequency
observer_local_frequency
source_local_direction
observer_local_direction
coordinate_null_residual
local_null_residual
reconstruction_residual
orientation_control
Schwarzschild_control
scale_control
rank_control
convergence_certificate
source_scope
limitations
```

## Expected bounded result

If all controls pass:

```text
KERR_FINITE_BOUNDARY_ZAMO_ENDPOINTS_CONVERT_COORDINATE_PATHS_TO_LOCAL_DIRECTION_AND_RELATIVE_FREQUENCY_SHAPE_BUT_WITHOUT_PHYSICAL_ENDPOINT_STANDARDS_OR_SCREEN_TRANSPORT_JOINT_DILATION_RETAINS_ABSOLUTE_SCALE_BLINDNESS_NOT_ELL0
```

Physical gate:

```text
PHYSICAL_KERR_EMITTER_ABSORBER_WORLDLINES_CLOCKS_AFFINE_FREQUENCY_STANDARD_PARALLEL_SCREEN_JACOBI_PREPARATION_RECEIVER_NOISE_JOINT_COVARIANCE_DATA_5D_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```

## Explicit exclusions

No claim of realistic emitter/observer motion, detector angle, physical clock, calibrated frequency, polarization, Jacobi/Sachs map, caustic imaging, 5D Kerr solution, 4D/5D detection, data fit, `L`, `ell0`, universal curvature floor, evidence, or detection.
