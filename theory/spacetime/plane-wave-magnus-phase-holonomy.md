# Canonical phase-connection Magnus ordering in an exact plane wave

Classification: `EXACT_SPACETIME_CANONICAL_PHASE_CONNECTION_MAGNUS_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

Status: `EXACT_PLANE_WAVE_CANONICAL_MAGNUS_ORDER_NONCOMMUTATIVE_RAW_REVERSAL_ODD_SPECTRAL_QUOTIENT_AND_AFFINE_SCALE_BLIND_NOT_ELL0`.

Gate: `PHYSICAL_SPACETIME_LOOP_PHASE_READOUT_ENDPOINT_ORDER_BRANCH_CALIBRATION_AND_ELL0_LAW_NOT_DERIVED`.

## Raw object and scope

Retain `K(u),M_K(u),Omega_1,Omega_2,P_K,A,B,C,D,chi_P,W(L),L`. Scope: `CANONICAL_JACOBI_PHASE_CONNECTION_NOT_FOUR_DIMENSIONAL_LEVI_CIVITA_LOOP_HOLONOMY`.

For symmetric tracefree plane-wave tidal profile `K(u)`,

`M_K(u)=[[0,I],[-K(u),0]]`, `P_K(L)=T exp[integral M_K(u) du]`.

The first two Magnus terms are

`Omega_1=integral M du`,

`Omega_2=(1/2) integral_(u1>u2) [M(u1),M(u2)] du1 du2`.

Direct multiplication verifies

`[M(u1),M(u2)]=diag(K(u1)-K(u2),K(u2)-K(u1))`

with zero residual. The declared pair has noncommuting norm `0.832733849628806`.

## Reversal counterexample

A smooth ordered two-lobe profile and `K_rev(u)=K(-u)` have the same top-hat window: difference `2.7476618026966064e-16`. Their `Omega_1` difference is `5.509324452557032e-16`. Yet `Omega_2` has norm `0.0569303170520838` and reverses sign with residual `9.813077866773594e-17`.

Full endpoint maps differ raw by `0.11635922583203352`, while the self-adjoint reversal reciprocity involution holds with residual `7.069801625830962e-15`. Characteristic-polynomial coefficients collide with residual `3.0543040520393885e-14`. Thus raw labelled-endpoint phase maps and `Omega_2` retain order orientation, but reversal-blind spectral quotient removes it.

`Omega_2` is not an independent channel beside `P_K`: it is a dependent term in the logarithmic expansion of the same ordered propagator. More noncommuting terms do not automatically add independent physical rank.

## Controls and nuisance orbit

A constant profile gives `Omega_2` norm `7.959187769253229e-16`; the ordered map agrees with `exp(Omega_1)` to `1.8039215853410342e-14`.

Common screen `SO(2)` covariance residual is `3.9744112474508555e-15`. A common `O(2)` reflection leaves characteristic coefficients exactly unchanged, so spectrum does not supply handedness.

Under `K_s(u)=s^-2 K(u/s)`, `L_s=sL`, rate units transform with `D=diag(I,I/s)`. Phase map, `Omega_1`, and `Omega_2` collide by similarity with maximum residual `1.9786328665246608e-14` at `s=1.47`. This leaves absolute affine scale and `ell0` unidentified.

A zero-average profile perturbation preserves `W` to `2.7476618026966064e-16` but changes `Omega_2` by `0.08473426377890564` and the full map by `0.08544174286229406`. Ordering is profile-informative at fixed protocol, not an `ell0` landmark.

## Source scope and disposition

Coley–McNutt–Milson (2012), DOI `10.1088/0264-9381/29/23/235023`, supports exact vacuum Brinkmann plane waves and curvature-driven geodesic deviation. It does not establish Magnus terms as detector output, finite windows, loop family, endpoint labels, phase calibration, affine scale, `ell0`, UMCH or detection. Magnus and matrix identities above are reproduced project derivations.

Result is a negative identifiability control, not a universal observational no-go. Four-dimensional Levi-Civita loops, causal detector-derived paths, endpoint standards, branch conditioning and geometry-`ell/ell0` law remain open. Structural dead end: `NOT_DECLARED`. UMCH: `UNPROVEN`. `ell0` not identified. `NO_POSITIVE_DETECTION_CLAIM`.
