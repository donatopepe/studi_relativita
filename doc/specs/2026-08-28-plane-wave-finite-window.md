# Exact plane-wave finite-window operator gate

## Question

Can a connection-derived exact spacetime with varying curvature produce nonradial finite-window operator response, and does that identify `ell0`?

## Designs

1. Keep arbitrary optical profile: already covered, but not tied to exact spacetime.
2. Use exact vacuum Brinkmann plane wave with declared profile (selected).
3. Infer universal scale from profile landmarks: rejected; profile parameters are geometry/source scales, not `ell0`.

## Source and geometry

Use Coley, McNutt and Milson, *Vacuum Plane Waves; Cartan Invariants and physical interpretation*, CQG 29 (2012) 235023, DOI `10.1088/0264-9381/29/23/235023`, arXiv `1210.0746`. Source supports exact vacuum plane-wave form `H=Re[A(u) zeta^2]` and curvature-driven geodesic deviation. It does not support UMCH, a universal floor, `ell0`, or detection.

Choose smooth tracefree transverse tidal profile in a parallel Brinkmann screen:

`K(u)=a(u) [[cos(2 theta(u)), sin(2 theta(u))],[sin(2 theta(u)),-cos(2 theta(u))]]`.

This is a declared exact vacuum plane-wave profile within the sourced family. Parameters are fixed toy geometry controls, not fitted physical claims.

## Finite window

For centered top-hat window of affine width `L`, retain raw operator

`W(L)=int_{-L/2}^{L/2} K(u) du`.

Compare projective direction after Frobenius normalization. Tests:

- fixed polarization `theta=const`: all `W(L)` are radial/collinear;
- rotating polarization: projective direction changes with `L` before zeros, giving connection-derived nonradial response;
- symmetric rotation `theta=omega u` can cancel off-diagonal moment under centered window and remain collinear: symmetry counterexample;
- adding phase/asymmetric rotation can yield nonradiality;
- changing window center or kernel moves/cancels landmarks;
- any turnover/zero is set by profile frequency, phase, center and kernel;
- `ell0` absent, so nonradiality is geometry/protocol shape, not UMCH scale identification.

Classification `EXACT_SPACETIME_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`. No data or detection. Route remains open for physically selected windows, endpoint transport and cross-channel maps; no structural dead end.
