# Exact plane-wave joint quotient gate

## Objective and classification

Test whether the connection-derived joint record `(W,B)` from an exact vacuum plane wave retains profile-order or scale information after the physically general endpoint-frame quotient and affine/profile rescaling nuisance.

Classification: `EXACT_SPACETIME_CROSS_CHANNEL_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

## Candidate designs

1. **Raw common-frame comparison.** Compare matrix entries of `W` and `B`. Rejected as primary because it silently anchors source and observer screens and does not survive independent endpoint calibration.
2. **Individual invariant compression.** Compare eigenvalues of symmetric `W` and singular values of `B`. Selected as the minimal exact `SO(2)`/endpoint-orthogonal quotient control, while explicitly recording that it may discard joint orientation.
3. **Assume a common anchored endpoint frame.** Deferred: this requires a physical anchor, handedness, path transport and calibration protocol not supplied by the exact metric alone.

## Exact counterexample

Use a smooth symmetric plane-wave optical profile `K(u)` on the centered affine interval and its reversal `K_rev(u)=K(-u)`.

- `W_rev=int K(-u)du=W` exactly on the centered interval.
- Jacobi reciprocity gives `B_rev=B^T` for vertex boundaries.
- Therefore eigenvalues of `W` and singular values, determinant and Frobenius norm of `B` agree.
- For a generic asymmetric rotating profile, raw `B_rev != B`; this difference is removed by the independent endpoint-frame quotient.

The joint quotient is thus profile-reversal blind even though the raw Jacobi channel is order-sensitive.

## Scale nuisance

Retain the exact rescaling `L2=sL1`, `K2(u)=K1(u/s)/s^2`, which preserves `LW` and `B/L`. The reversal counterexample and affine rescaling are distinct degeneracies: one destroys order after quotient; the other destroys absolute support scale without fixed affine/profile calibration.

## Scope and stop decision

The result does not prove that every joint invariant or physically anchored observable fails. It identifies the null space of the minimal endpoint-frame quotient for this exact family. Common-frame cross-invariants remain admissible only after a physical endpoint anchor is independently derived. `ell0` is absent. No structural dead end, mechanism, data result, or detection is declared.
