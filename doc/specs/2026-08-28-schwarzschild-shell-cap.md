# Schwarzschild shell-cap finite-window factorization gate

## Route

Combine exact Schwarzschild tidal radial amplitude with orientation-cap family, under explicitly assumed common tangent-space alignment rather than Schwarzschild parallel transport. Let

`E(r,n)=m r^-3 (I-3nn^T)`.

Use product measure: normalized radial density `w(r)` on shell `[r1,r2]` and uniform angular cap `0<=theta<=Theta`. Because amplitude and pattern separate, average factors exactly:

`Ebar=<m/r^3>_w * diag((c+c^2)/2,(c+c^2)/2,-c-c^2)`, `c=cos Theta`.

For positive mass and positive radial weights, radial shell changes only positive amplitude. Projective shape, hemisphere zero and signed-ray reversal depend only on cap boundary. Correlating radial and angular measure can break factorization, but then nonradiality is measure/protocol structure unless a physical covariant region law is independently derived.

## Counterexamples and gates

- Any two positive radial densities with different `<r^-3>` give same projective response at fixed cap.
- Hemisphere is zero for every radial shell.
- Above/below hemisphere signed sectors are determined by cap, not radial curvature scale.
- If cap angle is made scale-dependent, its crossing is movable by cap law.
- `ell0` is absent.

## Scope and decision

Classification `EXACT_PATTERN_WINDOW_CONTROL_AND_NEGATIVE_RESULT`; expected status `SCHWARZSCHILD_PRODUCT_SHELL_CAP_REMAINS_FACTORABLE_NOT_ELL0`. Exact Schwarzschild algebraic tidal field plus exact product integration after assumed Euclidean alignment. Not bitensorial Schwarzschild parallel transport, causal 4D window, physical orientation measure, data, or UMCH mechanism. Structural dead-end criteria fail because covariant correlated spacetime regions remain open. No reformulation.
