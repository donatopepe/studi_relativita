# Four-dimensional Levi-Civita holonomy in an exact plane wave

Classification: `EXACT_SPACETIME_LEVI_CIVITA_HOLONOMY_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

Status: `EXACT_PLANE_WAVE_LEVI_CIVITA_NULL_ROTATION_HOLONOMY_RAW_LOOP_VECTOR_NONTRIVIAL_SPECTRUM_UNIPOTENT_ABELIAN_AND_AFFINE_SCALE_BLIND_NOT_ELL0`.

Physical gate: `PHYSICAL_CAUSAL_SPACETIME_LOOP_FAMILY_TETRAD_ANCHOR_NULL_NORMALIZATION_DETECTOR_READOUT_AND_ELL0_LAW_NOT_DERIVED`.

Scope: `FOUR_DIMENSIONAL_LEVI_CIVITA_CONNECTION_ON_MATHEMATICAL_BRINKMANN_COORDINATE_LOOPS_NOT_DETECTOR_DERIVED`.

## Connection-derived control

For

`ds^2=2 du dv+dx^T dx+(x^T K(u)x)du^2`,

with symmetric tracefree `K`, direct transport around the declared coordinate rectangle gives

`H_LC=N(b_LC)=[[1,-b1,-b2,-|b|^2/2],[0,1,0,b1],[0,0,1,b2],[0,0,0,1]]`.

This is derived from the four-dimensional Levi-Civita Christoffel symbols, unlike the earlier prescribed screen connection. Raw `H_LC` and `b_LC` are nontrivial and orientation-labelled. Retain `K(u),Gamma_mu(z),loop_vertices,orientation,a,u_a,u_b,T_segments,H_LC,b_LC,spectrum_LC,chi_LC,W_a,P_K,L`.

Every `N(b)` is unipotent: `chi_LC(lambda)=(lambda-1)^4`. Distinct raw loop vectors therefore have identical ordinary spectra. Reversal gives `N(-b)=N(b)^-1`, but again leaves spectrum unchanged. Same-base-point compositions satisfy `N(b1)N(b2)=N(b1+b2)=N(b2)N(b1)`: this exact pp-wave holonomy control is Abelian, so non-Abelian order rank is absent here.

Profile reversal supplies a sharper cross-channel collision. Distinct histories yield colliding endpoint `H_LC` while the canonical Jacobi map `P_K` differs. Holonomy is therefore not an independent channel merely because it is connection-derived; channel relations remain profile, path, anchor, and readout dependent.

Common screen rotation conjugates `H_LC` and rotates `b_LC`; a null-basis boost rescales its coordinate components. The declared affine/profile orbit preserves dimensionless holonomy. No physical tetrad, null normalization, causal detector loop, `ell0` law, or absolute calibration is derived.

Source facts about exact plane waves, parallel null structure, trivial screen holonomy, and Abelian pp-wave holonomy are `KNOWN_RESULT`. Explicit finite-loop matrices and numerical collisions are `PROJECT_DERIVATION`; spectral and scale failures are `NEGATIVE_RESULT`; physical loop/readout/calibration remain `OPEN_PROBLEM`.

UMCH remains `UNPROVEN`; state remains `NO_POSITIVE_DETECTION_CLAIM`; structural dead end remains `NOT_DECLARED`.