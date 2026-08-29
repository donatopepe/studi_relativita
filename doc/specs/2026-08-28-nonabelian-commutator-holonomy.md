# Exact non-Abelian commutator holonomy gate

## Goal and classification

Counterexample-first extension beyond `SO(2)`. Classification: `EXACT_GROUP_TOY_CONTROL_AND_NEGATIVE_RESULT`. No spacetime connection or UMCH law is claimed.

## Construction

Use exact `SL(2,R)` shears

`A(a)=[[1,a],[0,1]]`, `B(b)=[[1,0],[b,1]]`

and group commutator

`C(a,b)=A(a)B(b)A(a)^(-1)B(b)^(-1)`.

Direct multiplication gives `det C=1` and `tr C=2+(ab)^2`. Hence conjugacy-invariant trace preserves only magnitude of product `ab`; signs, factor allocation, and ordered path decomposition are lost. Families `(a,b)` and `(ca,b/c)` collide for any nonzero `c`.

For window/path laws `a=kappa ell^p`, `b=rho ell^q`, trace is

`T(ell)=2+(kappa rho)^2 ell^(2(p+q))`.

A trace threshold `tau>2` occurs at

`ell_tau=((tau-2)/(kappa rho)^2)^(1/(2(p+q)))`.

Free shape/product amplitude moves threshold arbitrarily. Equal sum `p+q` gives same scale exponent, so separate exponents are not identified. Any claimed universal landmark requires independent physical derivation/calibration of coefficients, exponents, loop family, anchor, branch, and connection.

## Alternatives

Full matrix retains more coordinate information but is anchor/frame conjugated and not itself gauge invariant. Additional conjugacy invariants in `SL(2)` are algebraically fixed here by determinant and trace. Non-Abelian path sensitivity therefore does not imply parameter or ell0 identification.

## Decision

Expected status: `NONABELIAN_COMMUTATOR_TRACE_PRODUCT_DEGENERACY_NOT_ELL0`. Structural dead-end criteria do not pass because connection-derived 4D loops and physical multi-channel maps remain open. No reformulation.
