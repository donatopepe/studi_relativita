# Exact Einstein-static spatial Levi-Civita holonomy control

## Status and question

Classification: `KNOWN_RESULT`, `PROJECT_DERIVATION`, `TOY_CONTROL`, and `NEGATIVE_RESULT`, separated below.

Question: after the exact Brinkmann pp-wave control collapsed to Abelian null rotations, does a connection-derived finite loop in an exact four-dimensional spacetime with non-Abelian Levi-Civita holonomy create identifiable cross-channel rank or an invariant scale landmark?

UMCH remains `UNPROVEN`. This control cannot create a detector protocol, a value of `ell0`, or a positive detection claim.

## Alternatives considered

1. **Einstein static universe, spatial geodesic loops — selected.** The four-dimensional product spacetime `R x S^3` is exact and algebraically closed. Great two-spheres are totally geodesic, spherical triangles have exact finite holonomy, and loops in distinct spatial planes generate noncommuting `SO(3)` rotations. This directly tests whether genuine non-Abelian spacetime holonomy adds rank.
2. **de Sitter coordinate rectangles.** Full Lorentzian holonomy is attractive, but finite coordinate-loop transport requires a larger numerical connection calculation and introduces static-patch/horizon restrictions before the basic rank question is isolated.
3. **Schwarzschild finite loops.** Physically familiar but path closure, endpoint tetrads, radial/angular transport, horizon domain, and detector interpretation add nuisances not needed for this bounded counterexample-first step.

## Geometry, frame, domain, and loops

Use the exact product metric

`ds^2=-dt^2+R^2[d chi^2+sin^2(chi)(d theta^2+sin^2(theta)d phi^2)]`.

The selected loops lie at fixed `t` in totally geodesic great `S^2` submanifolds. At a common base point retain an oriented orthonormal tetrad `(e0,e1,e2,e3)`, with `e0=partial_t`. For each oriented spherical triangle `T_ij(alpha,beta)` in plane `(ei,ej)`, two sides have angular lengths `alpha,beta` and meet orthogonally. The geodesic closing side is fixed by spherical geometry. Require `0<alpha,beta<pi/2`; this avoids antipodal ambiguity and fixes the short geodesic closure.

Let `E(alpha,beta)` be the oriented spherical excess. Parallel transport around the triangle is

`H_ij=diag(1,Rot_ij(E))`.

The time leg is fixed. Orientation reversal sends `E -> -E` and `H -> H^-1`. For loops in planes `(e1,e2)` and `(e2,e3)`, require a nonzero commutator at generic nonzero excesses.

This is a mathematical spacelike loop family. It is not asserted to be causal, geodesic for a detector, or experimentally realizable.

## Exact formulas and channel relations

For the right spherical triangle,

`cos(c)=cos(alpha)cos(beta)`

and, using the spherical law of cosines for angles,

`cos(A)=cos(alpha)sin(beta)/sin(c)`,

`cos(B)=sin(alpha)cos(beta)/sin(c)`,

`E=A+B-pi/2`.

The intrinsic Gaussian curvature on the great sphere is `1/R^2`; Gauss--Bonnet gives

`E=Area(T)/R^2`.

Define retained finite-window curvature channel

`W_T=(1/R^2) Area(T) J_ij=E J_ij`.

Then the declared loop obeys the exact dependent cross-channel map

`H_ij=exp(W_T)`.

Therefore holonomy is not an independent channel for this family even though multiple loop planes generate a non-Abelian group.

## Counterexample-first controls

1. **Metric and transport:** `H^T eta H=eta`, `H e0=e0`.
2. **Finite nonidentity and reversal:** nonzero excess gives nonidentity; reversed orientation gives inverse.
3. **Non-Abelian composition:** rotations in distinct planes have nonzero commutator. Preserve raw ordered products.
4. **Cross-channel dependence:** verify `H_ij=exp(W_T)` and mark `holonomy_independent_channel=false`.
5. **Trace/conjugacy rank loss:** in `SO(3)`, trace of an individual simple rotation depends only on `cos(E)` and loses sign and `2pi` winding. Common tetrad conjugation rotates axes without changing spectra.
6. **Shape collision:** distinct right triangles `(alpha,beta)` can have equal excess after a bounded numerical solve; their raw boundary lengths differ but `W_T` and `H_ij` collide.
7. **Curvature-radius scaling:** replacing `(R,L_i)` by `(sR,sL_i)` preserves angular side lengths, excess, `W_T`, holonomy, spectra, and commutator. Hence dimensionless loop observables are blind to absolute `R` without externally fixed proper-length calibration.
8. **Flat/null limit:** `R -> infinity` at fixed proper side lengths gives identity holonomy.
9. **Jacobi distinction:** along a great-circle segment, dimensionless transverse Jacobi map depends on angular length; equal-area/equal-holonomy triangles may retain different labelled segment Jacobi maps. This prevents counting holonomy as a complete history channel.
10. **ell0 gate:** no symbol or law connects `R`, loop lengths, excess, or segment maps to `ell0`.

## Raw record

Retain at minimum:

`R,eta,tetrad,loop_planes,orientation,alpha_i,beta_i,c_i,proper_side_lengths,area_i,E_i,W_T_i,H_i,ordered_products,commutator,spectrum_i,chi_i,segment_Jacobi_i,shape_collision,scale_factor,flat_control`.

Scalar trace and spectrum remain dependent projections, not replacements for raw matrices and loop labels.

## Expected interpretation

Passing controls supports only a scoped negative result:

`EXACT_EINSTEIN_STATIC_SPATIAL_LEVI_CIVITA_HOLONOMY_NONABELIAN_RAW_ORDER_DEPENDENT_WINDOW_EXPONENTIAL_AND_CURVATURE_RADIUS_SCALE_BLIND_NOT_ELL0`.

Scope:

`FOUR_DIMENSIONAL_PRODUCT_SPACETIME_LEVI_CIVITA_CONNECTION_ON_MATHEMATICAL_SPACELIKE_GEODESIC_TRIANGLES_NOT_DETECTOR_DERIVED`.

Physical gate:

`PHYSICAL_CAUSAL_LOOP_FAMILY_PROPER_LENGTH_STANDARD_TETRAD_ANCHOR_DETECTOR_READOUT_AND_ELL0_LAW_NOT_DERIVED`.

Non-Abelianity would refute the idea that pp-wave Abelian collapse is generic, but would not identify `ell0` or add independent cross-channel rank under the exact `H=exp(W_T)` relation. Generic causal Lorentzian loops, detector calibration, nonconstant curvature, finite-window kernels, and physically fixed length standards remain open. No structural dead end is declared.

## Sources and limits

Canonical sources must be verified before implementation for: Einstein static product geometry, spherical-triangle identities, Gauss--Bonnet holonomy, and round-sphere holonomy. They may support those known geometric statements only. They do not establish this project's selected loop family, raw record, detector interpretation, cross-channel classification, scale nuisance, `ell0`, UMCH, or detection.

## Acceptance gates

- Deterministic dependency-free artifact and focused tests pass.
- Exact/nonexact tolerances are explicit and stricter than observed residuals.
- Non-Abelian raw composition, cross-channel dependence, shape collision, scaling orbit, flat limit, and Jacobi distinction are all tested.
- Theory and English/Italian audits share labels, formulas, deterministic values, source limits, and nonclaim language.
- Full suite, extraction, inventory, legacy identifiability, `git diff --check`, GitHub tests, and LaTeX CI are green before any conservative merge.
- Artifact preserves `ell0_identified=false`, `umch_status=UNPROVEN`, `positive_detection_claim=false`, and `structural_dead_end=NOT_DECLARED`.
