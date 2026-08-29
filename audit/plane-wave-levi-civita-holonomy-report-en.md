# Audit — exact plane-wave Levi-Civita holonomy

Classification: `EXACT_SPACETIME_LEVI_CIVITA_HOLONOMY_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

Status: `EXACT_PLANE_WAVE_LEVI_CIVITA_NULL_ROTATION_HOLONOMY_RAW_LOOP_VECTOR_NONTRIVIAL_SPECTRUM_UNIPOTENT_ABELIAN_AND_AFFINE_SCALE_BLIND_NOT_ELL0`.

Physical gate: `PHYSICAL_CAUSAL_SPACETIME_LOOP_FAMILY_TETRAD_ANCHOR_NULL_NORMALIZATION_DETECTOR_READOUT_AND_ELL0_LAW_NOT_DERIVED`.

Scope: `FOUR_DIMENSIONAL_LEVI_CIVITA_CONNECTION_ON_MATHEMATICAL_BRINKMANN_COORDINATE_LOOPS_NOT_DETECTOR_DERIVED`.

Epistemic labels: `KNOWN_RESULT`, `PROJECT_DERIVATION`, `NEGATIVE_RESULT`, `OPEN_PROBLEM`.

## Protocol and raw record

Use the exact vacuum Brinkmann control `ds^2=2 du dv+dx^Tdx+(x^TK(u)x)du^2` and transport the null-screen basis around an explicitly anchored coordinate rectangle. The loop is mathematical, not detector-derived, causal, geodesic, or observationally selected.

Retain `K(u),Gamma_mu(z),loop_vertices,orientation,a,u_a,u_b,T_segments,H_LC,b_LC,spectrum_LC,chi_LC,W_a,P_K,L`.

Direct connection transport gives the null rotation

`N(b)=[[1,-b1,-b2,-|b|^2/2],[0,1,0,b1],[0,0,1,b2],[0,0,0,1]]`.

Observed deterministic controls:

- nonidentity norm: `0.15084556081713096`;
- null-rotation residual: `5.927021026752577e-13`;
- metric-compatibility residual: `1.1854037716696464e-12`;
- composition commutator residual: `0.0`;
- profile-reversal Jacobi-map difference despite holonomy collision: `0.1163592258321023`;
- maximum affine dimensionless residual at scale `1.47`: `3.9523245835994223e-13`.

## Negative result

Every finite loop matrix is unipotent with `chi_LC(lambda)=(lambda-1)^4`. Distinct nonzero `b_LC` values collide in spectrum and characteristic polynomial. Complete loop reversal maps `b_LC` to `-b_LC` and inverts `H_LC`, while spectrum remains unchanged. Same-base null rotations commute and add parameters. Thus genuine four-dimensional Levi-Civita holonomy is raw-operator informative but ordinary spectrum supplies no extra rank in this exact pp-wave family.

Common screen rotations and null-basis boosts expose anchor and normalization dependence. Affine/profile scaling preserves dimensionless holonomy. No `ell0` is present or identified. Holonomy is not an independent channel from the retained connection/Jacobi record by declaration alone.

## Source scope

Coley–McNutt–Milson 2012, DOI `10.1088/0264-9381/29/23/235023`, supports exact vacuum Brinkmann plane-wave and curvature/geodesic-deviation context. Leistner 2006, DOI `10.1016/j.geomphys.2005.11.010`, supports pp-wave, parallel-null, and screen-holonomy context. Leistner–Schliebner 2016, DOI `10.1007/s00208-015-1270-4`, supports Abelian pp-wave holonomy context. These sources do not establish this loop family, numerical transport, causal support, detector tetrads, null normalization, readout, affine calibration, `ell0`, UMCH, or detection.

UMCH: `UNPROVEN`. Detection: `NO_POSITIVE_DETECTION_CLAIM`. Structural dead end: `NOT_DECLARED`.