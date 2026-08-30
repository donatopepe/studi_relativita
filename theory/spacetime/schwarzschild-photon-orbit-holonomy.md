# Schwarzschild photon-orbit Levi-Civita holonomy

## Boundary and raw object

In geometric units, the equatorial circular null geodesic lies at

`r_ph = 3M`, `dt/dphi = 3 sqrt(3) M`.

One future winding has `Delta phi = 2 pi`, coordinate duration `Delta t = 6 pi sqrt(3) M`, and proper duration for the static base observer

`Delta tau = 6 pi M`.

The project loop follows that future null photon orbit and returns along a past-directed static worldline at `r=3M`. Thus only the forward segment is null and geodesic. The closure is an ideal mathematical comparison path, not detector-derived. No photon reflection is used.

With constant coordinate connection generators along both segments,

`T_null = exp[-(Gamma_t Delta t + Gamma_phi Delta phi)]`,

`T_closure = exp[+Gamma_t Delta t]`,

and the raw tetrad operator is

`H_photon = E^-1 T_closure T_null E`.

The full matrices and generators remain primary. Characteristic coefficients are quotient diagnostics only.

## Exact controls

At `M=1`, tests give `Delta tau = 6 pi = 18.84955592`, null residual below `2e-15`, and radial geodesic residual below `3e-16`. Algebraic matrix exponentials agree with independent RK4 connection transport within `8e-10` for the complete loop. `H_photon` is Lorentz-compatible and nontrivial; its nonidentity norm is `148.8621186`.

The segment generators do not commute. Exchanging null and closure segment order changes the raw product by `464.9166525`. This records path ordering is not an independent channel: both products are functions of the same declared connection history and boundary.

## Orientation, winding and quotient

Azimuthal reversal changes the raw anchored matrix but its characteristic coefficients collide to numerical tolerance. A common tetrad rotation acts by conjugacy and preserves characteristic coefficients while changing raw entries. Handedness therefore needs a physical oriented anchor.

A two-winding null segment followed by one long static closure is not the square of the complete one-winding loop: the closure is batched rather than interleaved. This batched winding distinction is boundary/order information. Winding is a discrete protocol label, not a continuously inferred geometric parameter, and supplies no continuous geometric rank by itself.

Partial arcs with an added azimuthal/static closure approach identity as the arc shrinks, but are `MATHEMATICAL_NULL_ARC_WITH_STATIC_CLOSURE_NOT_CLOSED_NULL_GEODESIC`.

## Scale identifiability

The Schwarzschild dilation

`(M,r,Delta t,Delta tau) -> s (M,r,Delta t,Delta tau)`

preserves `Delta tau/M`, the tetrad `H_photon`, winding and all dimensionless quotient data while changing proper duration. The photon-sphere landmark is tied to background mass, `r_ph=3M`; no relation to `ell0` was derived. Therefore `ell0_identified = false`.

## Bounded verdict

`SCHWARZSCHILD_PHOTON_SPHERE_NONRADIAL_NULL_ORBIT_HOLONOMY_PATH_ORDERED_WINDING_DEPENDENT_AND_GEOMETRIC_SCALE_BLIND_NOT_ELL0`.

Scope: `FOUR_DIMENSIONAL_SCHWARZSCHILD_LEVI_CIVITA_CONNECTION_ON_FUTURE_NULL_PHOTON_SPHERE_WINDING_WITH_IDEAL_STATIC_WORLDLINE_CLOSURE_AND_NO_DETECTOR_READOUT`.

Gate: `PHYSICAL_EMITTER_ABSORBER_VECTOR_READOUT_ORIENTED_TETRAD_WINDING_SELECTION_COMMON_STANDARD_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`.

`Darwin1959GravityField` supports Schwarzschild trajectory and critical circular-orbit context only. Finite-loop transport, closure, ordering and scale tests are project derivations. Generic scattering echoes, freely falling endpoints and photon-sphere Jacobi/Sachs instability remain open. UMCH stays `UNPROVEN`; no positive detection claim follows.
