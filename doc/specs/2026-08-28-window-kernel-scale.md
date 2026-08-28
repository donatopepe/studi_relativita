# Finite-window kernel-scale landmark gate

## Question

Can nonradial spectral crossing from finite-window averaging identify a universal scale when kernel width convention is free?

## Toy control

Use local operator profile `K(s)=diag(1,s^2)` and normalized top-hat window on `[-kappa ell,kappa ell]`. Average is

`R(ell,kappa)=diag(1,kappa^2 ell^2/3)`.

Projective spectrum varies nonradially and becomes isotropic at `ell_cross=sqrt(3)/kappa`.

This is exact integration of a synthetic operator profile, not an exact spacetime geometry.

## Counterexamples and gates

- Any positive target crossing is produced by `kappa=sqrt(3)/ell_target`.
- Reparameterizing reported scale as physical half-width `L=kappa ell` fixes crossing at `L=sqrt(3)`, showing coordinate convention dependence.
- Fixed independently preregistered kernel makes crossing a profile/window geometric scale only.
- Common amplitude leaves projective crossing unchanged; kernel dilation moves it.
- `ell0` is absent unless physical theory derives `ell_cross=alpha ell0` under fixed scale convention.

## Decision

Status `FINITE_WINDOW_SPECTRAL_LANDMARK_KERNEL_DILATION_MOVABLE_NOT_ELL0`. No reformulation: covariant exact-geometry kernels remain open. `UNPROVEN`; `NO_POSITIVE_DETECTION_CLAIM`.
