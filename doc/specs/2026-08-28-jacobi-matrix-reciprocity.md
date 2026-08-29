# Exact matrix Jacobi multi-segment reciprocity gate

## Question

Does two-segment transpose reciprocity of the vertex Jacobi block survive three or more exact symmetric optical segments, or can a fixed-screen singular-value record retain profile reversal?

## Design and alternatives

1. **Two-segment-only extension:** vary lengths and rotations. Cheap, but cannot test whether transpose identity is structural or accidental.
2. **Three-segment exact product (selected):** use same closed-form symplectic segment maps, compare ordered profile `(K1,K2,K3)` with reversed `(K3,K2,K1)`, and test full-map characteristic polynomial, vertex block transpose, singular values, determinant and Frobenius norm.
3. **Smooth numerical Sachs integration:** physically closer, but introduces discretization and solver nuisance before exact finite-product reciprocity is understood.

Selected approach is strongest algebraically closed counterexample-first step.

## Exact construction

Each symmetric positive screen matrix has exact propagator

`P(K,L)=[[C,S],[-KS,C]]`,

with spectral matrix functions. For traversal list, total map is left-ordered product. Reverse full profile, including segment lengths and matrices.

Pre-registered tests:

- every segment is symplectic;
- two-segment reversed vertex block is transpose, reproducing prior control;
- generic three-segment reversal is tested rather than assumed;
- aligned diagonal profiles reduce to independent scalar modes;
- isotropic profiles erase orientation effects;
- full-map spectrum and vertex singular values are compared separately;
- `ell0` must be absent.

If generic three-segment singular values differ, result establishes order sensitivity only after fixed screen metric and fully specified source/observer frames. If they remain equal, document stronger reciprocity/null space. Neither outcome supplies `ell0`.

## Scope

`EXACT_MATRIX_JACOBI_CONTROL_AND_NEGATIVE_RESULT`. Piecewise-constant optical matrices, not connection-derived smooth Sachs profile in exact spacetime. Boundary vertex, affine normalization, screen metric, transport and observed block are fixed by construction. No structural dead end: smooth matrix profiles and spacetime derivation remain open.
