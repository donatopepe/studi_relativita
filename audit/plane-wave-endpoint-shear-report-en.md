# Exact plane-wave endpoint shear-calibration audit — English

## Ledger

- Classification: `EXACT_SPACETIME_CROSS_CHANNEL_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.
- Status: `EXACT_PLANE_WAVE_LABELLED_ENDPOINT_OPTICAL_SPECTRA_NONIDENTIFIABLE_UNDER_CANONICAL_SHEAR_CALIBRATION_NOT_ELL0`.
- Open gate: `PHYSICAL_PHASE_SPACE_ENDPOINT_CALIBRATION_NOT_DERIVED`.
- UMCH remains `UNPROVEN`.
- Conclusion: `NO_POSITIVE_DETECTION_CLAIM`.

## Counterexample-first result

Keep labelled source/observer endpoints and raw `A`, `B`, `C`, `D`. For symmetric endpoint-local calibration matrices, define

`S(H)=[[I,0],[H,I]]`,

and

`P'=S(H_o)P S(H_s)^{-1}`.

These shears are symplectic and preserve endpoint labels. Exact block algebra gives `A'=A-BH_s`, `B'=B`, `D'=D+H_oB`, and `C'=C+H_oA-(D+H_oB)H_s`. Consequently optical endpoint matrices transform as

`(B')^{-1}A'=B^{-1}A-H_s`,

`D'(B')^{-1}=DB^{-1}+H_o`.

Free symmetric shears move endpoint spectra, eigenvalue gaps, and eigenframes. Scalar shears already move absolute eigenvalues while preserving gaps. Therefore labelled endpoints alone do not make these optical spectra calibration invariant.

Affine/profile scaling remains exact when `H` scales as `1/L`; the dimensionless calibrated full map is unchanged. Absolute support scale and `ell0` remain unidentified.

## Scope and limits

This bounded nuisance model does not erase every full-map invariant: `B` remains unchanged. It does not establish nonidentifiability under every physical calibration group. Independent derivation of measured phase-space variables, source/observer tetrads, transport, gains, leakage, and detector response remains required.

Coley–McNutt–Milson (2012), DOI `10.1088/0264-9381/29/23/235023`, supports exact vacuum Brinkmann plane waves and curvature-driven geodesic deviation. Endpoint shear calibration, finite-window protocol, detector observability, UMCH, `ell0`, and detection are not established by the source.

Full Sachs observables, causal windows, physical calibration restrictions, and other exact geometries remain open. This is not a structural dead end. No data or detection claim.
