# Exact plane-wave common-anchor handedness

## Native objects and group actions

Keep the same exact Brinkmann plane-wave control:

\[
W(L)=\int_{-L/2}^{L/2}K(u)\,du,\qquad
B(L)=D(L/2),\quad D''+KD=0,
\]

with vertex data `D(-L/2)=0`, `D'(-L/2)=I`. Profile reversal gives `W_rev=W` and `B_rev=B^T`.

For

\[
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
a(B)=\frac{B_{21}-B_{12}}2=-\frac12\operatorname{tr}(JB),
\]

common oriented frame changes act by `B -> Q B Q^T`, `Q in SO(2)`. Since `QJQ^T=J`, `a(B)` is invariant, while `a(B^T)=-a(B)`. Thus a common oriented screen anchor conditionally retains profile-reversal sign discarded by the independent endpoint quotient `SO(2) x SO(2)`.

This recovery requires both **common identification** and **handedness**. Under `Q in O(2)`, `QJQ^T=det(Q)J`; a reflection flips `a(B)`. Therefore a common but unoriented anchor does not make its sign observable.

## Scale counterexample

Under `L2=s L1`, `K2(u)=K1(u/s)/s^2`, Jacobi scaling gives `B2=s B1`; hence `a(B2)/L2=a(B1)/L1`. Oriented anchoring does not remove affine/profile scale degeneracy. No `ell0` enters the map.

## Result

Status: `EXACT_PLANE_WAVE_COMMON_ORIENTED_ANCHOR_RECOVERS_REVERSAL_SIGN_CONDITIONALLY_NOT_ELL0`.

Classification: `EXACT_SPACETIME_CROSS_CHANNEL_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

Open gate: `PHYSICAL_ORIENTED_ENDPOINT_ANCHOR_NOT_DERIVED`.

The Brinkmann parallel screen supplies a mathematical trivialization for this exact control. It does not derive source/observer tetrads, their physical identification, parity/handedness, transport realization, boundary calibration, or detector observability. The result is conditional profile-orientation recovery, not support-scale or `ell0` identification. UMCH remains `UNPROVEN`; conclusion remains `NO_POSITIVE_DETECTION_CLAIM`.

Canonical source scope remains exact vacuum plane waves and curvature-driven geodesic deviation. Common anchoring, finite-window protocol, boundary choice, UMCH, `ell0`, and detection are project choices or claims, not established by that source.
