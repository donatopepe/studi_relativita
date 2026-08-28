# Finite-window operator shape: necessary is not sufficient

Classification: `TOY_CONTROL_AND_NEGATIVE_RESULT`.

Status: `NONRADIAL_GEOMETRIC_SHAPE_NOT_ELL0_LANDMARK`; `NO_POSITIVE_DETECTION_CLAIM`.

For operator profiles `A,B`, a deterministic finite-window abstraction is

`R(ell)=ell^2[f(ell)A+g(ell)B]`.

If sampled profiles are separable (`g=0`, or fixed `g/f`), all responses lie on one operator ray and projective scale is non-identifiable. If `A,B` are non-collinear and `g/f` changes, projective shape changes with `ell`: finite-window variation can therefore break radiality.

This does not identify `ell0`. In the control, only `ell`, geometric profile coefficients, and window choice occur. An `ell0` landmark is absent, and free profile/window nuisance may mimic any observed shape. A physical derivation must fix profiles, transport, boundary conditions and nuisance quotient independently, then prove an injective map in `ell/ell0` or a theory-fixed landmark.

This result does not trigger core reformulation. Transport, holonomy/Jacobi, boundary/orientation and cross-channel routes remain open.
