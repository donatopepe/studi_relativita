# Schwarzschild mixed-plane holonomy audit

Classification: `EXACT_SPACETIME_LEVI_CIVITA_HOLONOMY_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

Status: `EXACT_SCHWARZSCHILD_MIXED_PLANE_LEVI_CIVITA_HOLONOMY_NONABELIAN_PATH_ORDERED_BOUNDARY_DEPENDENT_AND_GEOMETRIC_SCALE_BLIND_NOT_ELL0`.

Scope: `FOUR_DIMENSIONAL_SCHWARZSCHILD_LEVI_CIVITA_CONNECTION_ON_MATHEMATICAL_PIECEWISE_COORDINATE_LOOPS_NOT_DETECTOR_DERIVED`.

Gate: `PHYSICAL_CAUSAL_LOOP_FAMILY_PROPER_TIME_LENGTH_STANDARD_TETRAD_ANCHOR_DETECTOR_READOUT_AND_ELL0_LAW_NOT_DERIVED`.

## Derivation and counterexamples

For the exact exterior metric, RK4 integrates `dV/ds=-Gamma_mu dz^mu/ds V` on labelled equatorial rectangles. Common-base static-tetrad matrices are `H_tr` and `H_rphi`. Metric-connection residual is `6.680156279261934e-10`; maximum Lorentz residual is `1.7871742506134475e-13`. Nonidentity norms are `0.05483794566090526` and `0.09510550908422082`. Orientation reversal satisfies `H_reverse=H^-1` to `6.93556937731235e-15`.

Mixed-plane products are genuinely order dependent: commutator nonidentity norm `0.00368784364042176`, ordered-product difference `0.0036878373757369145`. Non-Abelianity does not imply independent rank: both matrices derive from one declared metric, connection and boundary family.

For a shrinking loop, local curvature-flux residual per coordinate area is `8.119881880118987e-05`. For the finite loop, naive single-flux residual is `0.03959321213476851`. `H is not assumed equal to exp(integral R)`; finite transport requires `PATH_ORDERED_CONNECTION_HISTORY_REQUIRED`.

Equal coordinate-area rectangles at shifted radial boundaries collide in coordinate area but differ in raw holonomy by `0.03490123492447132`. This is boundary/placement sensitivity, not an `ell0` landmark. Reversal characteristic coefficients collide to `2.220446049250313e-16`; common tetrad conjugacy preserves characteristic coefficients to `8.881784197001252e-16` while raw anchored matrices can differ.

## Scale and scope

Under `(M,r,T)->(sM,sr,sT)` with `s=1.47` and fixed angular aperture, maximum holonomy residual is `2.59660112853674e-14`, although proper scales differ. No absolute scale is identified.

Loops are mathematical piecewise-coordinate loops: not geodesic, not causal, not detector-derived. Sources establish only Schwarzschild geometry and curvature--holonomy context, not finite loop choice, numerical readout or UMCH.

UMCH: `UNPROVEN`. Result: `NO_POSITIVE_DETECTION_CLAIM`. `ell0_identified=false`; `structural_dead_end=NOT_DECLARED`.
