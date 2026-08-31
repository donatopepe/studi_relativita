# Linearized compact-circle tidal response

## Classification map

- `KNOWN_RESULT`: `Liu2003CompactifiedPotential` gives the exact Newtonian point potential for one periodic spatial circle; `FloratosLeontaris1999` gives the full KK tower and short/long limits; `KehagiasSfetsos2000` gives compact-space eigenmodes and leading Yukawa range/degeneracy.
- `PROJECT_DERIVATION`: differentiate the declared scalar potential into `T_ij=partial_i partial_j Phi`, convolve it with normalized point/sphere/Gaussian source profiles, and average the raw matrix over declared finite windows.
- `TOY_CONTROL`: static weak-field scalar gravity on `R^(1,3) x S1`, localized/uniform source and probe profiles, radial-shell and oriented-box windows, noiseless deterministic arithmetic.
- `NEGATIVE_RESULT`: uniform source or probe removes nonzero modes; source and window scales are preparation nuisances; joint dilation leaves dimensionless records unchanged; absolute `L` and `ell0` are not identified.
- `OPEN_PROBLEM`: nonlinear 5D dynamics, radion stabilization, physical matter localization, gauge-fixed tensor response, calibrated source/probe/window preparation, receiver, covariance, data, and a derived `L`–`ell0` law.
- `HYPOTHESIS`: observed four-dimensional gravity could be a projection or effective sector of higher-dimensional geometry. This candidate is not evidence-supported.

## Raw operator record

For a radial scalar potential, the local raw matrix is retained as

\[
T_{ij}=T_\perp(\delta_{ij}-\hat r_i\hat r_j)+T_\parallel\hat r_i\hat r_j.
\]

Finite windows average transported raw matrix entries. The flat-background Cartesian transport in this bounded toy is explicit. Norms and eigenvalue ratios remain secondary. Averaging, differentiating, source convolution, and scalarization are not generally interchangeable.

## Circle projection

Localized source and localized probe retain the full KK tower, including relative circle-position phases. Any uniform circle profile has zero overlap with nonzero Fourier modes. Therefore absence of tower terms can be a preparation/projection null, not a geometric exclusion.

## Finite sources and windows

Point, compact uniform-sphere, and Gaussian sources preserve fixed total mass. Source radii and Gaussian width are independent preparation scales. Radial-shell and oriented-box windows introduce additional scale and boundary dependence. Zero-source-size and zero-window limits recover point controls away from singular support.

## Scale gate

The dimensionless response depends on ratios such as `r/L`, `source_size/L`, and `window_size/L`. Joint dilation of all lengths preserves the dimensionless raw record. Current rank control has scale null direction `[1,0,0]` for `[log_L,source_size_over_L,window_width_over_L]`.

```text
JOINT_5D_GEOMETRIC_DILATION_NOT_INTERIOR_ABSOLUTE_SCALE
L_NOT_IDENTIFIABLE_WITHOUT_SOURCE_PROBE_AND_WINDOW_CALIBRATION
DEPENDENCE_UNRESOLVED_WITHOUT_JOINT_COVARIANCE
```

Primary result:

```text
LOCALIZED_SOURCE_PROBE_KK_TOWER_ADDS_DIMENSIONLESS_FINITE_WINDOW_TIDAL_SHAPE_BUT_UNIFORM_PROFILE_PROJECTION_SOURCE_WINDOW_DEGENERACY_AND_JOINT_5D_DILATION_PREVENT_ABSOLUTE_SCALE_OR_ELL0_IDENTIFICATION
```

This is a project model result, not evidence for an extra dimension, `L`, `ell0`, or UMCH.

```text
NONLINEAR_5D_DYNAMICS_RADION_STABILIZATION_MATTER_LOCALIZATION_SOURCE_PROBE_PREPARATION_ABSOLUTE_COUPLING_CLOCK_RECEIVER_CALIBRATED_NOISE_JOINT_COVARIANCE_DATA_AND_ELL0_LAW_NOT_DERIVED
```
