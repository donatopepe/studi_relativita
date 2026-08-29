# Canonical versus velocity phase variables in a rotating screen

## Question

The corrected rotating-screen map of PR #77 used the state `(x,x')`. Is its ordinary symplectic spectrum channel-native, or does the choice between coordinate velocity and canonical momentum introduce an endpoint shear nuisance?

## Approaches

1. Treat `(x,x')` as canonical: rejected unless `A=0`; rotating-coordinate velocity does not carry the standard symplectic form.
2. Stop at a general warning: insufficient; exact endpoint transformation allows a deterministic counterexample.
3. Selected: derive canonical momentum `p=x'+Ax=Q^T y'`, integrate both generators, verify their endpoint graph relation and symplectic structures, then test spectral mobility under endpoint angular velocity.

## Exact derivation

For `y=Qx`, `Q'=QA`, `A=-omega J`, define

`p=x'+Ax=Q^T y'`.

Canonical state `z_c=(x,p)` satisfies

`x'=p-Ax`,

`p'=-Q^T K Q x-Ap`,

so

`M_c=[[-A,I],[-Q^T K Q,-A]]`.

Because `A^T=-A`, `M_c` is Hamiltonian with standard `Omega`; its propagator `P_c` is symplectic. Endpoint relation uses

`C(u)=diag(Q(u),Q(u))`,

`P_c=C_o^-1 P_inertial C_s`.

Velocity state `z_v=(x,x')` obeys `z_c=H(A)z_v`,

`H(A)=[[I,0],[A,I]]`.

Since `A` is antisymmetric, `H(A)` is not a canonical lower shear. Exact relation:

`P_c=H(A_o) P_v H(A_s)^-1`.

The velocity map preserves endpoint-dependent pulled-back two-forms, not standard `Omega` in general.

## Counterexample-first tests

- `omega=0`: canonical and velocity maps coincide and are standard symplectic.
- Direct canonical generator equals both canonical endpoint graph and velocity-to-canonical endpoint conversion.
- `P_c` satisfies standard symplecticity; `P_v` generally does not.
- Their characteristic polynomials generally differ. Thus PR #77 characteristic values for `(x,x')` are phase-variable/calibration dependent, not canonical invariants.
- Modify only endpoint angular-velocity calibration while holding `K,Q` and inertial `P` fixed: velocity-map characteristic coefficients move, while canonical map remains fixed. This is a calibration counterexample, not a physical connection solution.
- Common constant screen basis canonically conjugates `P_c` and preserves its characteristic polynomial.
- Affine/profile/connection scaling preserves canonical characteristic coefficients and still does not identify absolute scale.
- Source/observer labels, `A_s,A_o`, screen handedness, and displacement/momentum units remain explicit.

## Classification and correction ledger

Classification: `EXACT_SPACETIME_CANONICAL_SCREEN_PHASE_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

Status: `EXACT_PLANE_WAVE_ROTATING_SCREEN_VELOCITY_SPECTRUM_ENDPOINT_CALIBRATION_DEPENDENT_CANONICAL_MAP_AFFINE_SCALE_BLIND_NOT_ELL0`.

PR #77 differential equation and endpoint graph for `(x,x')` remain correct. Superseded: any interpretation of its ordinary characteristic polynomial as a canonical screen invariant. Retain it as a velocity-coordinate diagnostic. New canonical object is `P_c` in `(x,p)`.

Open gate: `PHYSICAL_SCREEN_CANONICAL_MOMENTUM_ENDPOINT_ANGULAR_VELOCITY_AND_UNIT_CALIBRATION_NOT_DERIVED`.

Coley–McNutt–Milson 2012 supports exact vacuum Brinkmann plane waves and curvature-driven geodesic deviation. It does not establish rotating detector phase variables, canonical detector momentum, endpoint angular velocity, unit calibration, finite windows, affine nuisance law, UMCH, `ell0`, or detection.

Physical detector action/readout, tetrads, transport path, causal support, and block-preserving calibration group remain open. Not a structural dead end.

UMCH remains `UNPROVEN`; `NO_POSITIVE_DETECTION_CLAIM`.
