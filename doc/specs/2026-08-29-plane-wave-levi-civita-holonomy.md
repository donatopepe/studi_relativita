# Exact Brinkmann plane-wave Levi-Civita holonomy control

## Status and question

Classification: `KNOWN_RESULT`, `PROJECT_DERIVATION`, and `NEGATIVE_RESULT`, separated below.

Question: for a genuine four-dimensional Levi-Civita connection in an exact vacuum Brinkmann plane wave, can closed-loop holonomy or its spectrum provide order-sensitive, nonradial, affine-scale-identifying information beyond the already-retained tidal and Jacobi objects?

UMCH remains `UNPROVEN`. This control cannot create a positive detection claim, a physical detector loop, or a value of `ell0`.

## Alternatives considered

1. **Coordinate rectangular loops in an exact Brinkmann plane wave — selected.** Pull back the four-dimensional Levi-Civita connection to explicit closed loops and integrate parallel transport directly. This replaces prescribed screen `SO(2)` transport with connection-derived transport while keeping path, anchor, orientation, and profile explicit.
2. **Infinitesimal curvature-only loops.** Algebraically simpler, but too weak: they would not test finite-loop composition, reversal, spectra, or profile-history collisions.
3. **Generic non-Abelian exact spacetime.** Scientifically broader, but no bounded detector-derived loop family or exact control is currently fixed. Choosing one now would add geometry and calibration assumptions rather than test the open plane-wave route.

## Geometry and conventions

Use coordinates `(u,v,x1,x2)` and

`ds^2 = 2 du dv + dx^T dx + (x^T K(u) x) du^2`,

where `K(u)` is smooth, symmetric, and tracefree. The tracefree quadratic profile is the declared exact vacuum plane-wave control. Signs are fixed by this metric and checked directly through metric compatibility of numerical transport.

At base point `x=0`, retain null-screen basis `(p,e1,e2,q)=(partial_v,partial_x1,partial_x2,partial_u)` with Gram matrix

`eta=[[0,0,0,1],[0,1,0,0],[0,0,1,0],[1,0,0,0]]`.

The only connection coefficients needed for declared loops are derived from the metric, not prescribed:

- `Gamma^i_uu = -K_ij x^j`;
- `Gamma^v_ui = Gamma^v_iu = K_ij x^j`;
- `Gamma^v_uu = (1/2) x^T K'(u) x`.

Parallel transport obeys `dT/ds = -Gamma_mu(z(s)) zdot^mu T`.

## Loop family and raw record

Use endpoint-labelled coordinate rectangles based at `(u_a,v_0,0,0)`:

1. transverse displacement `0 -> a` at `u_a`;
2. longitudinal segment `u_a -> u_b` at fixed `a`;
3. transverse displacement `a -> 0` at `u_b`;
4. longitudinal return `u_b -> u_a` at `x=0`.

These are mathematical closed loops. They are not asserted causal, detector-realizable, geodesic, or uniquely selected by observation.

Retain raw

`K(u),Gamma_mu(z),loop_vertices,orientation,a,u_a,u_b,T_segments,H_LC,b_LC,spectrum_LC,chi_LC,W_a,P_K,L`.

`H_LC` is the ordered product of segment transports. `b_LC` is extracted only after verifying that `H_LC` has the null-rotation form

`N(b)=[[1,-b1,-b2,-|b|^2/2],[0,1,0,b1],[0,0,1,b2],[0,0,0,1]]`.

## Counterexample-first tests

1. **Connection and metric compatibility.** Compare analytic Christoffel components with finite metric derivatives where useful; require `H_LC^T eta H_LC=eta` and `H_LC p=p`.
2. **Finite null rotation.** Verify direct ordered transport equals `N(b_LC)` and is nonidentity for a nonzero loop.
3. **Spectral collapse.** Verify all four eigenvalues are one and `chi_LC(lambda)=(lambda-1)^4` for distinct nonzero loop amplitudes. Spectrum and characteristic polynomial must therefore fail to recover raw `b_LC`.
4. **Orientation reversal.** Reverse the complete loop and require `H_rev=H_LC^-1=N(-b_LC)`. Raw orientation survives under an anchored basis; spectrum remains unchanged.
5. **Abelian composition.** For two loops based at the same event, verify `N(b1)N(b2)=N(b1+b2)=N(b2)N(b1)`. Finite Levi-Civita holonomy in this pp-wave control does not provide non-Abelian ordering rank.
6. **Profile/window collision and cross-channel map.** Derive and verify, for the declared rectangles, `b_LC=W_a=integral(K(u)du)a` and `H_LC=N(b_LC)`, so this holonomy is dependent on the retained tidal window rather than an independent channel. Construct distinct tracefree profile histories with the same `W_a`; require distinct sampled profiles and colliding endpoint holonomies while Jacobi `P_K` differs, preserving channel distinctions.
7. **Anchor quotient.** Verify common screen rotations conjugate `H_LC` and rotate `b_LC`, preserving `|b_LC|`; verify null-basis boosts rescale the coordinate `b_LC` while preserving the trivial characteristic polynomial. No invariant absolute scale is inferred without physical tetrad and normalization.
8. **Affine/profile scaling.** Apply the declared plane-wave scaling orbit and verify dimensionless holonomy similarity/collision. No `ell0` occurs in the geometry or loop law.
9. **Null competitor.** `K=0` gives identity holonomy for every declared loop.

## Expected bounded result

Expected status:

`EXACT_PLANE_WAVE_LEVI_CIVITA_NULL_ROTATION_HOLONOMY_RAW_LOOP_VECTOR_NONTRIVIAL_SPECTRUM_UNIPOTENT_ABELIAN_AND_AFFINE_SCALE_BLIND_NOT_ELL0`.

Expected physical gate:

`PHYSICAL_CAUSAL_SPACETIME_LOOP_FAMILY_TETRAD_ANCHOR_NULL_NORMALIZATION_DETECTOR_READOUT_AND_ELL0_LAW_NOT_DERIVED`.

Expected scope:

`FOUR_DIMENSIONAL_LEVI_CIVITA_CONNECTION_ON_MATHEMATICAL_BRINKMANN_COORDINATE_LOOPS_NOT_DETECTOR_DERIVED`.

This would be a stronger negative control than prescribed screen holonomy: genuine four-dimensional connection-derived holonomy is nontrivial in raw matrix/vector form, but its ordinary spectrum is identically unipotent and the restricted loop composition is Abelian in this exact pp-wave family. It does not close generic non-Abelian spacetime routes.

## Sources and epistemic boundaries

- Coley–McNutt–Milson (2012), DOI `10.1088/0264-9381/29/23/235023`: exact vacuum Brinkmann plane waves and curvature/geodesic-deviation context already verified by project.
- Leistner (2006), DOI `10.1016/j.geomphys.2005.11.010`: pp-wave definition, parallel null vector, and trivial screen holonomy. Metadata and exact quoted scope must be recorded before use.
- Leistner–Schliebner (2016), DOI `10.1007/s00208-015-1270-4`: pp-waves as Lorentzian manifolds with Abelian holonomy context. Metadata and exact scope must be verified before use.

Sources do not establish this loop protocol, detector calibration, causal support, raw readout, affine normalization, `ell0`, UMCH, or detection. Explicit matrices, collisions, scaling controls, and cross-channel comparisons are project derivations.

## Deliverables and stop conditions

Deliver deterministic Python artifact, focused scientific tests, bilingual audit reports, theory note, plan, source log, and only bounded paper/roadmap/ledger updates if warranted. Run full suite, extraction, inventory, legacy identifiability check, related exact controls, and CI.

Stop rather than merge if direct transport fails metric compatibility, does not reduce to a null rotation under declared conventions, source scope cannot be verified, bilingual semantics diverge, or any result requires a detector or `ell0` law not derived here. No structural dead end is declared.