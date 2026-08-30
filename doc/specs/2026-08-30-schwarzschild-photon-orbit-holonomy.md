# Schwarzschild photon-orbit Levi-Civita holonomy control

## Bounded question

Can a nonradial, causally selected exact Schwarzschild boundary produce operator-valued finite-loop structure beyond radial radar, and does its joint timing/holonomy record identify any absolute or UMCH scale?

UMCH remains `UNPROVEN`. No detector, source preparation, mirror, data, mechanism, `ell0`, bound or detection is introduced.

## Alternatives considered

1. **Photon-sphere winding loop — selected.** A future null circular Schwarzschild geodesic at `r=3M` completes one or more azimuthal windings and is closed by the past-directed segment of the matching static worldline. Connection coefficients are constant along each segment, so transport is algebraically closed by matrix exponentials. This is genuinely nonradial, causal on the forward leg, exact, and simpler than generic lensing.
2. **Generic nonradial scattering echo.** More observationally suggestive, but turning-point branches, elliptic integrals, emitter/receiver matching and numerical boundary solves obscure the first nonradial identifiability test.
3. **Photon-sphere Jacobi/Sachs bundle.** Directly probes instability and conjugate structure, but source screen, affine normalization, endpoint covariance and closure readout must first be specified. Retained as next route.

## Known geometry and project derivation

For equatorial Schwarzschild null circular motion,

`r_ph=3M`, `dt/dphi=orientation*3*sqrt(3)*M`,

so one winding has coordinate duration `Delta t=6*pi*sqrt(3)*M` and static-observer proper duration `Delta tau=sqrt(1-2M/r_ph)*Delta t=6*pi*M`.

- Photon sphere and null circular geodesic: `KNOWN_RESULT`, source scope to be verified canonically.
- Finite connection transport, loop holonomy, winding/orientation/quotient controls: `PROJECT_DERIVATION`.
- Past closure and common static tetrad family: `TOY_CONTROL`.
- Scale, rank and collision results: `NEGATIVE_RESULT` unless tests show otherwise.
- Physical emission/absorption/readout and `ell0` law: `OPEN_PROBLEM`.

## Raw contract

Preserve

`M,r_ph,f_ph,tetrad,orientation,winding,Delta_phi,Delta_t,Delta_tau,null_tangent,null_residual,geodesic_residual,Gamma_t,Gamma_phi,A_null,A_closure,T_null,T_closure,H_photon,ordered_reverse,H_reverse,characteristic_coefficients,spectrum_or_surrogate,winding_products,Jacobian_joint,scale_factor,scale_orbit,flat_or_large_radius_control`.

No characteristic polynomial may replace `H_photon` as primary.

## Counterexample-first controls

1. Verify tangent nullity and radial geodesic equation at `r=3M`; reject arbitrary circular null paths as causal photon orbits.
2. Compare algebraic segment exponentials with high-resolution numerical transport.
3. Verify Lorentz preservation in the base tetrad, nonidentity and reversal inversion.
4. Compare one winding with two windings. Determine whether `H(2)=H(1)^2` for the complete repeated loop and preserve any failure caused by closure ordering.
5. Reverse azimuthal orientation. Compare raw matrices, characteristic coefficients and common-conjugacy data; do not infer handedness without anchor.
6. Compare `T_null*T_closure` against reversed segment order to expose noncommutativity/path ordering. This is one loop history, not an independent channel.
7. Form joint dimensionless map `(Delta tau/M,H_photon)` over winding/orientation. Test whether winding adds continuous rank or only a discrete protocol label. Winding must not be promoted to a geometric scale.
8. Apply `(M,r_ph,Delta t,Delta tau)->s(...)`. Tetrad holonomy and dimensionless duration must remain invariant while proper duration changes.
9. Separate photon-sphere landmark `r_ph=3M` from `ell0`: it is set by background mass and scales with `M`.
10. Test shrinking azimuth for mathematical partial arcs only as a null limit, explicitly not as a closed null geodesic protocol.

## Interpretation gates

Passing nontriviality or path-ordering checks establishes only a finite Levi-Civita operator on the declared mathematical closure. It does not derive an instrument capable of storing/comparing vectors after a photon orbit, an emitter/absorber action, continuous phase readout, endpoint covariance or statistically independent channels.

Provisional status if scale orbit survives:

`SCHWARZSCHILD_PHOTON_SPHERE_NONRADIAL_NULL_ORBIT_HOLONOMY_PATH_ORDERED_WINDING_DEPENDENT_AND_GEOMETRIC_SCALE_BLIND_NOT_ELL0`.

Scope:

`FOUR_DIMENSIONAL_SCHWARZSCHILD_LEVI_CIVITA_CONNECTION_ON_FUTURE_NULL_PHOTON_SPHERE_WINDING_WITH_IDEAL_STATIC_WORLDLINE_CLOSURE_AND_NO_DETECTOR_READOUT`.

Gate:

`PHYSICAL_EMITTER_ABSORBER_VECTOR_READOUT_ORIENTED_TETRAD_WINDING_SELECTION_COMMON_STANDARD_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`.

No structural dead end is declared. Generic nonradial scattering networks, freely falling endpoints and photon-sphere Jacobi/Sachs instability remain open.
