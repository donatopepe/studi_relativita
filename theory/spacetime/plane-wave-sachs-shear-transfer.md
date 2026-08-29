# Exact plane-wave Sachs endpoint-shear transfer

## Raw graph object

Keep `P,X,V,S,S_0,H_s,H_o` raw, with `S=VX^{-1}` away from `det X=0`. Symmetric endpoint shear uses

`G(H)=[[I,0],[H,I]]`, `P'=G(H_o)PG(H_s)^{-1}`.

This lower-shear group is a project calibration nuisance, not a source-derived detector group.

## Exact boundary transfer

For source graph `(I,S_0)` choose `S'_0=S_0+H_s`. Then source calibration cancels before propagation:

`G(H_s)^{-1}(I,S'_0)^T=(I,S_0)^T`.

Hence at observer

`X'_o=X_o`, `V'_o=V_o+H_oX_o`, `S'_o=S_o+H_o`.

Source shear is exactly absorbed by boundary preparation. Observer shear moves symmetric expansion/shear but preserves oriented twist because `H_o` is symmetric. Without source-boundary compensation, raw endpoint matrices change. `det X=0` produces `CAUSTIC_OR_CONGRUENCE_BLOCK_SINGULAR`.

Under affine/profile scaling, `S_0,H_s,H_o -> (S_0,H_s,H_o)/s`; dimensionless `X,LV,LS,LS_0,LH_s,LH_o` collide. Different profiles remain conditionally distinguishable only with boundary and calibration fixed.

## Ledger

Classification: `EXACT_SPACETIME_SACHS_CALIBRATION_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

Status: `EXACT_PLANE_WAVE_SACHS_SOURCE_SHEAR_ABSORBED_BY_BOUNDARY_OBSERVER_SHEAR_MOVES_OPTICS_NOT_ELL0`.

Open gate: `PHYSICAL_SACHS_SOURCE_BOUNDARY_AND_OBSERVER_CALIBRATION_NOT_DERIVED`.

Coley–McNutt–Milson supports exact vacuum Brinkmann plane waves and curvature-driven geodesic deviation. Endpoint calibration, graph-boundary preparation, rotating detector congruence, affine/profile nuisance, UMCH, `ell0`, and detection are not source-established.

Restricted detector groups, independently prepared boundary, common standards, physical screen transport, causal windows, caustic continuation, and cross-channel anchors remain open. Not a structural dead end.

UMCH remains `UNPROVEN`; `NO_POSITIVE_DETECTION_CLAIM`.
