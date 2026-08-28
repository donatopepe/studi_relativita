# Operator-native exact-case controls

## Goal

Lift Minkowski, FLRW, Schwarzschild, and VSI toys from scalar norms to channel-native tidal/magnetic endomorphism spectra. Test whether projective/spectral invariants identify scale or merely geometry class.

## Definitions

For declared orthonormal observer frame, store dimensionless electric/magnetic eigenvalue tuples `ell^2 eig(E)` and `ell^2 eig(B)`, plus rank, trace, Frobenius norm, sorted projective spectrum, and anisotropy ratios where defined.

## Expected controls

- Minkowski: zero operators, rank zero, projective spectrum undefined.
- isotropic FLRW tidal operator: triple-degenerate spectrum; projective direction fixed under ell scaling; no ell0 information.
- Schwarzschild static tidal operator: ratio `(-2,1,1)` fixed under ell scaling; anisotropy identifies geometry pattern but not ell0.
- VSI type-N toy: nonzero electric/magnetic operators despite scalar polynomial invariants zero; toy spectrum/polarization fixed under ell scaling.

## Decision

Known exact cases with curvature held fixed and response normalization `ell^2` move radially in operator space as ell varies. Their projective spectra are constant. Thus they validate native objects and distinguish geometry types, but yield `PROJECTIVE_SCALE_NON_IDENTIFIABLE_IN_CURRENT_EXACT_CONTROLS`.

This does not prove every physical multiscale family collinear. A nontrivial ell-dependent operator shape, cross-channel transport, boundary effect, or derived spectral landmark is required.

Core remains `UNPROVEN`; no ell0/detection.
