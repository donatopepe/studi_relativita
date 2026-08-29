# Smooth matrix Jacobi reversal reciprocity gate

## Question

Does finite-product identity `B_reverse=B_forward^T` extend to continuous symmetric optical profiles, and under exactly which assumptions?

## Designs

1. Only numerical integration: useful control but not derivation.
2. Product-limit derivation plus deterministic smooth integration (selected).
3. Claim general spacetime reciprocity: rejected; connection-derived screen transport and physical boundary frames are not supplied.

## Route

Consider first-order system `Y'=H(s)Y`,

`H(s)=[[0,I],[-K(s),0]]`,

on fixed affine interval `[0,S]`, with real continuous symmetric `K(s)`. Define reversed profile `K_rev(s)=K(S-s)` and block exchange `E=[[0,I],[I,0]]`.

Use piecewise-constant approximants. Every segment exponential is fixed by anti-involution `R(P)=E P^T E`; reversing partition order gives `P_rev,N=R(P_N)`. Continuity of `K`, standard convergence of ordered exponential/product approximants, and continuity of `R` imply

`P_rev=R(P)`.

Thus, if `P=[[A,B],[C,D]]`, then

`P_rev=[[D^T,B^T],[C^T,A^T]]`,

and `B_rev=B^T`.

## Counterexamples and scope gates

- nonsymmetric `K`: generator no longer fixed by `R`; identity need not hold;
- reversed profile must use same affine normalization and full interval;
- endpoint screens remain distinct spaces; independent endpoint quotient still identifies `B` and `B^T`;
- discontinuous profiles may be admitted under weaker integrability, but this bounded derivation claims continuous `K` only;
- numerical Runge-Kutta controls test smooth rotating anisotropic profiles and a nonsymmetric counterexample;
- `ell0` absent.

Classification: `PROJECT_DERIVATION_AND_NEGATIVE_RESULT`. No exact four-dimensional spacetime derivation, physical screen connection, data or UMCH mechanism. Exact-spacetime transport and cross-channel laws remain open; no structural dead end.
