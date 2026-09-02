# Kerr equatorial photon-ring orientation and scale control

## Status

`DRAFT_FOR_RATIFICATION`

Design-only bounded continuation. No implementation, test, artifact, bibliography edit, UMCH change, or detection claim is authorized by this draft.

Global state remains:

```text
UMCH=UNPROVEN
ell0_identified=false
structural_dead_end=NOT_DECLARED
Detection=NO_POSITIVE_DETECTION_CLAIM
Maximum interpretation=CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE
```

## Bounded question

Do exact prograde/retrograde equatorial circular null orbits in subextremal Kerr add orientation-sensitive dimensionless shape beyond Schwarzschild while retaining a joint geometric dilation that prevents identification of an absolute interior scale or `ell0`?

This first Kerr increment audits orbit radius, azimuthal orientation, Boyer–Lindquist coordinate timing, radial-potential conformance, convention collisions, and scale rank. It does not yet construct a transported screen, Jacobi/Sachs phase map, finite-boundary scattering protocol, source, absorber, endpoint tetrad, detector, covariance, or physical clock.

## Alternatives considered

1. **Equatorial circular photon-ring radius/orientation/timing/scale — selected.** Exact formulas expose frame-dragging branch asymmetry, the Schwarzschild collision, sign conventions, and geometric scale symmetry with few gauge choices. Boyer–Lindquist timing is retained only as a coordinate record, not a detector clock.
2. **Generic finite-boundary equatorial Kerr scattering — deferred.** Adds turning points and endpoint dependence, but also requires branch solves, endpoint frames, screen transport, affine normalization, and a wider convention surface before the basic spin/orientation collision is audited.
3. **Full Kerr Jacobi/Sachs screen transport or source/receiver microphysics — deferred.** More operator-native, but tetrad choice, parallel screen transport modulo null gauge, phase-space normalization, endpoint preparation, caustics, and readout would make the first Kerr falsification test too broad. This is a later increment, not evidence supplied by the orbit-level result.

Recommendation: select approach 1. It is the smallest exact counterexample-first test of whether frame dragging supplies more than dimensionless shape.

## Domain and conventions

Use geometrized units `G=c=1` and standard Boyer–Lindquist coordinates `(t,r,theta,phi)`.

```text
M>0
0<=chi<1
chi=|a|/M
|a|<M
r=r_ph=constant
theta=pi/2
future-directed circular null geodesic
```

Primary implementation convention uses `a>=0`. Define branch label

```text
branch=prograde    iff dphi/dt>0
branch=retrograde  iff dphi/dt<0
```

for that primary convention. Prograde means motion in the same azimuthal direction as the hole rotation; retrograde means the opposite direction. At `a=0`, the labels become physically degenerate even if both records are retained.

A separate signed-spin convention control may use `spin_sign in {-1,+1}` and `azimuthal_orientation in {-1,+1}`. Relative orientation is

```text
relative_orientation=spin_sign*azimuthal_orientation
```

with `+1` prograde and `-1` retrograde. The simultaneous transformation

```text
(a,azimuthal_orientation) -> (-a,-azimuthal_orientation)
```

preserves relative orientation and radius while reversing signed azimuthal motion. It must not be confused with orientation reversal at fixed `a`, which exchanges prograde and retrograde branches.

Extremal `chi=1` is excluded from the numerical domain because the prograde orbit reaches the horizon-limit convention surface. Limits as `chi->1^-` may be reported separately, never treated as an interior subextremal sample.

## Canonical geometry and source scope

For `chi=|a|/M`, define dimensionless Boyer–Lindquist radii

```text
x_pro = 2*[1+cos((2/3)*acos(-chi))]
x_retro = 2*[1+cos((2/3)*acos(chi))]
r_pro=M*x_pro
r_retro=M*x_retro
```

with expected range

```text
1<=x_pro<=3<=x_retro<=4
```

and Schwarzschild collision

```text
chi->0: x_pro=x_retro=3
```

These formulas, the prograde/retrograde definitions, branch ordering, range, and zero-spin limit are `KNOWN_RESULT` within the limited verified scope of Edward Teo, *Spherical photon orbits around a Kerr black hole*, *General Relativity and Gravitation* 35 (2003) 1909–1926, DOI `10.1023/A:1026286607562`, author PDF `https://phyweb.physics.nus.edu.sg/~phyteoe/kerr/paper.pdf`, especially Eq. (1a,b) and surrounding discussion.

For radial conformance, use the equatorial null potential in a declared energy normalization. With `xi=L_z/E`, `q_C=Q_C/E^2`,

```text
Delta=r^2-2*M*r+a^2
R(r)=[r^2+a^2-a*xi]^2-Delta*[(xi-a)^2+q_C]
q_C=0
R(r_ph)=0
dR/dr(r_ph)=0
```

Teo Secs. II–III, including its radial Eq. (10) and constant-radius conditions, is source support only for Kerr coordinates/geodesic equations and `R=R'=0`. Any code-level residual, normalization, signed convention map, timing record, scaling audit, rank result, or UMCH interpretation remains `PROJECT_DERIVATION` or `NEGATIVE_RESULT`.

No source establishes this project's operational protocol, detector, physical endpoint, covariance, scale identifiability, `ell0`, UMCH, or detection.

## Raw bounded record

Primary orbit-level record remains structured rather than prematurely scalarized:

```text
R_Kerr_orbit=(
  geometry,
  branch_records,
  radial_potential_conformance,
  convention_controls,
  Schwarzschild_collision,
  geometric_scale_control,
  rank_control,
  provenance,
  limitations
)
```

Each branch record must preserve at least:

```text
branch
relative_orientation
azimuthal_orientation
chi
x_ph=r_ph/M
r_ph
xi_over_M
Omega_phi*M
Delta_t_per_2pi/M
R_residual
R_prime_residual
```

`Omega_phi=dphi/dt` and `Delta_t_per_2pi=2*pi/abs(Omega_phi)` are Boyer–Lindquist coordinate quantities. They are not proper time, source phase, photon phase, asymptotic detector timing, or a physical clock. A later implementation may derive their exact circular-orbit expressions from the declared Kerr equations, but must preregister and source-check those expressions before using them as test or ledger authority.

No scalar norm of this record replaces the record itself.

## Preregistered controls

### 1. Radius formula and range

For representative `chi` values in `[0,1)`, both direct formulas must be finite and satisfy

```text
1<x_pro<=3<=x_retro<4
```

for strict subextremal nonzero spin, with equality at the appropriate zero-spin or extremal limits only.

### 2. Branch ordering

For `0<chi<1`,

```text
x_pro<x_retro
```

Frame dragging therefore adds branch-sensitive dimensionless shape. This is not an absolute scale.

### 3. Schwarzschild collision

At `chi=0`, both branch radii equal `3M`; any signed timing/orientation distinction is a retained label convention, not a geometrically distinct Schwarzschild photon radius.

Expected classification:

```text
KERR_PROGRADE_RETROGRADE_BRANCHES_COLLIDE_IN_SCHWARZSCHILD_LIMIT
```

### 4. Radial-potential conformance

Derived `xi` and each radius must satisfy `R=0` and `dR/dr=0` under the same declared energy normalization. Formula agreement without radial-potential agreement fails the control.

This conformance test does not establish stability, screen dynamics, observable flux, or detector response.

### 5. Signed convention collision

Simultaneously flip spin sign and azimuthal orientation. Relative branch, dimensionless radius, and unsigned period must agree; signed angular velocity must reverse. Flip orientation alone at fixed nonzero spin and verify that the branch changes.

Expected classification:

```text
SIMULTANEOUS_SPIN_ORIENTATION_REVERSAL_IS_CONVENTION_COLLISION_NOT_ELL0
```

### 6. Joint geometric dilation

At fixed `chi`, apply

```text
(M,a,r,xi,lambda) -> (s*M,s*a,s*r,s*xi,s*lambda), s>0
```

with coordinate time scaled as `t->s*t`. Expected invariant or covariant records are

```text
chi invariant
r/M invariant
xi/M invariant
Omega_phi*M invariant
Delta_t_per_2pi/M invariant
```

while dimensional radii and coordinate periods scale by `s`.

Expected classification:

```text
JOINT_MA_GEOMETRIC_DILATION_NOT_INTERIOR_SCALE
```

### 7. Rank and scale-null direction

For dimensionless features at fixed `chi`, preregister parameters

```text
parameters=[log_M,chi]
```

The exact `log_M` feature column must vanish. The `chi` column may have nonzero rank because spin changes dimensionless branch shape. Report rank and null direction without interpreting local rank as global physical identifiability.

Expected scale-null direction:

```text
[1,0]
```

### 8. No `ell0` identification

Neither `a`, `M`, `r_ph`, `xi`, a coordinate period, nor their ratios are automatically `ell0`. Fixed dimensional `M`, `a`, frequency, or clock information would be an imported standard unless physically derived under the UMCH protocol.

Expected bounded result if all controls pass:

```text
KERR_FRAME_DRAGGING_ADDS_PROGRADE_RETROGRADE_DIMENSIONLESS_ORBIT_SHAPE_BUT_JOINT_MA_DILATION_RETAINS_ABSOLUTE_SCALE_BLINDNESS_NOT_ELL0
```

## Falsification and stop conditions

The selected design is falsified or must be revised if any of these occur:

- sourced radius formulas fail radial-potential conformance under consistent conventions;
- branch ordering or Schwarzschild collision fails away from declared numerical tolerance;
- simultaneous spin/orientation reversal does not produce the preregistered collision;
- a supposedly dimensionless record changes under exact joint dilation;
- dimensional timing is presented as a physical clock without endpoint worldline and readout derivation;
- an external mass, spin, frequency, or time standard is silently counted as internally identified;
- `ell0` is inferred without a derived geometry-to-`ell/ell0` law;
- full Jacobi/screen claims appear without a separately ratified design.

A failed control is preserved as a negative or contradictory result; it is not tuned away by changing conventions after inspection.

## Determinism and later implementation contract

If ratified, implementation must proceed through a sibling plan and TDD. Numerical artifacts use `.8g`; canonicalize to `0.0` only when `abs(value)<1e-7`. Tests must include source scope, exact/analytic identities where available, representative numerical controls, report alignment in English/Italian, deterministic artifact comparison, and full `python3 -m unittest discover -s tests`.

Implementation must preserve formulas and raw records before derived classifications. No full Jacobi map, screen basis, polarization, source coherence, detector, noise, or covariance may be added under this spec.

## Boundaries and open gate

This control remains geometry-level. It does not derive:

```text
PHYSICAL_KERR_SOURCE_EMISSION_ABSORPTION_ENDPOINT_FRAME_SCREEN_PREPARATION_ABSOLUTE_CLOCK_RECEIVER_TRANSFER_CALIBRATED_NOISE_JOINT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED
```

Even a passing result is at most `CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE`. It does not justify a structural-dead-end declaration because generic Kerr scattering, full Jacobi/screen transport, and physical source/receiver routes remain open.

## Ratification gate

Current state: `DRAFT_FOR_RATIFICATION`.

Human ratification must choose one timing scope before any implementation:

- **A — recommended:** include signed Boyer–Lindquist angular velocity and coordinate period as explicitly nonphysical orbit records, after exact expression/source verification;
- **B — narrower:** implement radius/orientation/radial-potential/scaling only and defer all timing.

After ratification, next action is writing `doc/plans/2026-08-30-kerr-photon-ring-orientation-scale.md`. No implementation is permitted before that gate.
