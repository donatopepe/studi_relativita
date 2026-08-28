# Finite-loop path-shape landmark gate

## Question

Can a conjugacy-invariant finite-loop trace crossing identify a universal scale when loop shape is free?

## Toy control

Use two shear segment maps `A(a)=[[1,a],[0,1]]`, `B(b)=[[1,0],[b,1]]`. Product has determinant one and trace `2+ab`. Let shape protocol set `a=ell`, `b=-rho ell`, giving trace `2-rho ell^2`. A chosen trace target `tau<2` occurs at `ell_cross=sqrt((2-tau)/rho)`.

This is finite-dimensional matrix algebra, not connection-derived spacetime holonomy.

## Counterexamples and gates

- Trace is similarity invariant, so crossing survives cyclic conjugacy quotient.
- Free positive shape factor `rho` moves crossing to any positive scale: `rho=(2-tau)/ell_cross^2`.
- Thus conjugacy invariance is necessary but not sufficient for scale identifiability.
- Fixed independently derived loop family makes crossing geometric/path-protocol scale only.
- Degenerate `rho=0` removes crossing; sign changes alter existence/domain.
- `ell0` remains absent unless theory fixes `ell_cross=alpha ell0`.

## Decision

Status `HOLONOMY_TRACE_LANDMARK_PATH_SHAPE_MOVABLE_NOT_ELL0`. No reformulation: connection-derived fixed loop families remain open. `UNPROVEN`; `NO_POSITIVE_DETECTION_CLAIM`.
