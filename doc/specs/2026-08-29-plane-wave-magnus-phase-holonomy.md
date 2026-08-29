# Exact plane-wave canonical phase connection: Magnus ordering and quotient

## Question

Does non-Abelian path ordering of the connection-derived canonical Jacobi generator supply an independent cross-channel observable or an `ell0` landmark beyond the retained finite-window operator and full Jacobi map?

## Classification

`EXACT_SPACETIME_CANONICAL_PHASE_CONNECTION_MAGNUS_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

Project derivation and negative identifiability control in exact Brinkmann plane waves. It is not four-dimensional tangent-bundle Levi-Civita loop holonomy, detector calibration, data, an `ell0` law, or UMCH evidence.

## Inventory and declared object

For symmetric transverse tidal profile `K(u)`, use canonical phase generator

`M_K(u)=[[0,I],[-K(u),0]]`,

and ordered propagator

`P_K(L)=T exp[integral M_K(u) du]`.

Retain raw `K(u),M_K(u),Omega_1,Omega_2,P_K,A,B,C,D,chi_P,W(L),L`. Here

`Omega_1=integral M du`,

`Omega_2=(1/2) integral_(u1>u2) [M(u1),M(u2)] du1 du2`.

`Omega_1` contains the integrated tidal/window information. `Omega_2` is a dependent expansion term of the same ordered map, not a preregistered independent channel.

## Counterexample-first design

Use an ordered smooth two-lobe exact plane-wave profile and its affine reversal `K_rev(u)=K(-u)`. Both share the same top-hat average `W`, local invariant distribution, support and amplitude. Their ordering differs.

For the declared generator,

`[M(u1),M(u2)]=diag(K(u1)-K(u2),K(u2)-K(u1))`.

Therefore `Omega_2` can be nonzero and reverses sign when profile order reverses, while `Omega_1` and `W` collide. This directly demonstrates non-Abelian phase ordering beyond average curvature.

But the full propagator already contains all Magnus orders. For the self-adjoint reversed profile, reciprocity/reversal relates endpoint maps; characteristic-polynomial coefficients remain equal within tolerance. Thus:

- raw labelled-endpoint map and `Omega_2` can retain order orientation;
- endpoint swap or reversal-blind spectral quotient removes that orientation;
- adding `Omega_2` beside `P_K` does not create an independent channel;
- noncommutativity alone does not identify absolute affine scale or `ell0`.

## Alternatives considered

1. **Canonical Magnus decomposition — selected.** Uses existing exact plane-wave Jacobi dynamics and gives a bounded non-Abelian path-ordering control without inventing detector loops.
2. **Screen `SO(2)` holonomy.** Already tested in PR #82; Abelian and endpoint-matched.
3. **Four-dimensional Levi-Civita closed loops.** Stronger physically, but current protocol lacks detector-derived spacetime loop family, anchor, tangent tetrad, branch and readout. Remains open.

## Required tests

1. `K` remains symmetric/tracefree and reversal preserves integrated window.
2. Analytic commutator identity agrees with direct `4x4` multiplication.
3. `Omega_1` collides under reversal; `Omega_2` is nonzero and sign-reverses.
4. Reversed full maps differ raw but obey declared reciprocity involution.
5. Characteristic polynomials collide under reversal.
6. Constant-profile control has `Omega_2=0` and ordered map equals constant-generator exponential.
7. Common screen `SO(2)` acts covariantly; common `O(2)` does not create spectral orientation.
8. Under `K_s(u)=s^-2 K(u/s)`, `L_s=sL`, compare phase maps using rate-unit similarity `D=diag(I,I/s)` and preserve dimensionless Magnus diagnostics with corresponding block units.
9. A profile perturbation at fixed average changes `Omega_2`/full map, proving profile sensitivity but not `ell0`.
10. Deterministic artifact, bilingual audits, source scope, full tests and CI.

## Interpretation gates

Status expected:

`EXACT_PLANE_WAVE_CANONICAL_MAGNUS_ORDER_NONCOMMUTATIVE_RAW_REVERSAL_ODD_SPECTRAL_QUOTIENT_AND_AFFINE_SCALE_BLIND_NOT_ELL0`.

Physical gate:

`PHYSICAL_SPACETIME_LOOP_PHASE_READOUT_ENDPOINT_ORDER_BRANCH_CALIBRATION_AND_ELL0_LAW_NOT_DERIVED`.

No structural dead end. Four-dimensional connection loops, physically labelled endpoints, calibrated phase readout, causal loop families, branch conditioning and a geometry-`ell/ell0` law remain open.

## Source scope

Coley–McNutt–Milson (2012), DOI `10.1088/0264-9381/29/23/235023`, supports exact vacuum Brinkmann plane waves and curvature-driven geodesic deviation. It does not establish this Magnus decomposition as detector output, finite windows, endpoint labels, phase calibration, loop readout, affine scale, `ell0`, UMCH or detection. Magnus and matrix identities are reproduced project derivations; no new citation claim is made.
