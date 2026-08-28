# Finite-holonomy trace aliasing

Classification: `EXACT_GROUP_CONTROL_AND_NEGATIVE_RESULT`.

Status: `FINITE_HOLONOMY_TRACE_PERIODIC_BRANCH_NONIDENTIFIABLE`; `NO_POSITIVE_DETECTION_CLAIM`.

For exact planar rotation holonomy

`H(phi)=[[cos phi,-sin phi],[sin phi,cos phi]]`,

trace is conjugacy invariant `T(phi)=2 cos phi`. It is even and periodic: `T(phi)=T(-phi)=T(phi+2pi n)`. Global inverse therefore has branches

`phi=+-arccos(T/2)+2pi n`.

Trace becomes injective only after preregistering monotone branch such as `[0,pi]`; derivative `-2 sin phi` vanishes at endpoints, so inversion is poorly conditioned there. Orientation reversal is invisible. Full matrix retains sine sign only after frame/orientation convention; unordered eigenvalue set still identifies `+-phi`.

If phase is `phi=k A`, unknown curvature amplitude and loop area are multiplicatively confounded. Conjugacy invariance therefore does not imply global phase or scale identifiability. Branch, winding, orientation, area, anchor and path family must be independently fixed. `ell0` is absent.

This is exact `SO(2)` group algebra, not connection-derived spacetime holonomy or observation. Non-Abelian exact loop routes remain open; no core reformulation is triggered.
