# Exact plane-wave Sachs boundary/endpoint shear-transfer quotient

## Research question

Does carrying a physically undeclared canonical endpoint-shear calibration through a non-vertex Sachs congruence create new invariant profile information, or can source calibration be absorbed exactly into boundary preparation?

## Compared approaches

1. **Scalar-only optical shifts.** Compare expansion/shear/twist before and after calibration. Rejected as primary because scalarization discards raw `X,V,S,S_0` and can hide graph-coordinate equivalences.
2. **Arbitrary independent `Sp(4)×Sp(4)`.** Already known transitive on full maps and too broad for this bounded question.
3. **Selected: symmetric lower-shear graph transfer.** Keep raw full propagator and congruence matrices. Test exact source-boundary absorption and observer-output shift under
   \[
   G(H)=\begin{pmatrix}I&0\\H&I\end{pmatrix},\qquad H=H^T.
   \]
   This is minimal, block-preserving, and directly joins prior endpoint-shear and non-vertex Sachs controls.

## Exact derivation to test

Let `P` propagate phase-space columns `(X,V)` and let the source graph be `V_s=S_0X_s`, with `X_s=I`. Under

\[
P'=G(H_o)P G(H_s)^{-1},
\]

choose transformed source boundary

\[
S'_0=S_0+H_s.
\]

Then `G(H_s)^{-1}(I,S'_0)^T=(I,S_0)^T`, so

\[
X'_o=X_o,\qquad V'_o=V_o+H_oX_o,\qquad S'_o=S_o+H_o.
\]

Thus source shear is exactly absorbed into `S_0`; observer shear moves symmetric optical content. For symmetric `H_o`, oriented twist is unchanged. The graph relation and twist-area law remain exact away from `det X=0`.

Dimensional scaling must use `H_s,H_o,S_0 ~ 1/L`; under `L→sL`, each scales by `1/s`.

## Counterexample and controls

- Nonzero source shear with compensating boundary shift must produce an exact raw endpoint collision.
- Nonzero observer shear must leave `X` and twist unchanged while moving expansion/shear and `V,S` by predicted amounts.
- Omitting source-boundary compensation must produce a measurable endpoint difference.
- `det X=0` remains explicit caustic gate.
- Affine/profile scaling must preserve dimensionless `X,LV,LS,LS_0,LH_s,LH_o` and transfer residuals.
- Different curvature profiles may remain distinguishable only conditionally at fixed calibration and boundary.

## Classification and interpretation

Classification: `EXACT_SPACETIME_SACHS_CALIBRATION_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

Expected status: `EXACT_PLANE_WAVE_SACHS_SOURCE_SHEAR_ABSORBED_BY_BOUNDARY_OBSERVER_SHEAR_MOVES_OPTICS_NOT_ELL0`.

Open gate: `PHYSICAL_SACHS_SOURCE_BOUNDARY_AND_OBSERVER_CALIBRATION_NOT_DERIVED`.

The shear group is a project nuisance model, not a source-derived detector model. Coley–McNutt–Milson supports exact vacuum Brinkmann plane waves and curvature-driven geodesic deviation, not endpoint calibration, graph-boundary preparation, rotating detector congruences, `ell0`, UMCH, or detection.

This bounded negative result does not test every restricted detector group, independently prepared boundary, common canonical standard, causal window, or cross-channel anchor. Not a structural dead end.

UMCH remains `UNPROVEN`; `NO_POSITIVE_DETECTION_CLAIM`.
