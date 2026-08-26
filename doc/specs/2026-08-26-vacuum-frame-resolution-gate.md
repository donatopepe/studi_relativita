# Vacuum frame resolution gate

## Goal

Replace binary vacuum-frame placeholder with conservative provenance-aware decision gate. No algorithm invents a CMB continuation from local vacuum curvature.

## Decisions

1. Unique regular future-timelike eigenvector of `T^mu_nu` resolves `MATTER_FRAME_RESOLVED`.
2. In vacuum/degenerate sector, CMB continuation resolves only when all are preregistered and documented:
   - boundary/anchor hypersurface;
   - future-directed unit timelike anchor field;
   - transport rule;
   - path/domain family;
   - uniqueness over admissible paths within declared tolerance;
   - causal/domain coverage of target region.
3. Missing input, failed uniqueness, insufficient coverage, or competing admissible continuation returns `FRAME_UNRESOLVED` with reason codes.
4. `FRAME_UNRESOLVED` is never confirmatory and forces ell0 `NON_IDENTIFIABLE`.
5. Resolved frame is necessary, never sufficient, for ell0 identifiability or positive-floor evidence.

## Controls

- FLRW comoving matter frame: resolved matter control.
- Schwarzschild exterior with no cosmological boundary data: unresolved.
- Vacuum toy with stipulated unique continuation certificate: resolved only as protocol fixture, not physical derivation.
- Competing-path toy: unresolved.

## Limits

No local preferred frame, Lorentz violation, real CMB reconstruction, threshold fit, data, detection, or ell0 value. Core remains `UNPROVEN`; ell0 remains `NON_IDENTIFIABLE` in project evidence state.
