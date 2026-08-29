# Exact scalar Jacobi three-segment permutation gate

## Goal

Test whether two-segment vertex-displacement order blindness survives three exact scalar segments and distinguish cyclic conjugacy from noncyclic permutations.

## Construction

Use same exact `SL(2,R)` segment propagators `P_i`. Total map for traversal order `(i,j,k)` is `P_k P_j P_i`. Cyclic rotations of three factors are similar, so trace/determinant/eigenvalues coincide. Noncyclic reversal is not generally related by cyclic conjugation and may change trace as well as vertex endpoint.

Enumerate all six permutations for fixed distinct `(lambda_i,L_i)`. Partition by:

- characteristic polynomial `(trace,det)`;
- vertex displacement `M01`;
- full map.

Expected: two cyclic classes, each with common spectrum; vertex displacement may distinguish or collide depending on exact reciprocity identities. Full permutation generally not identifiable from spectrum alone. Any endpoint inference requires boundary/affine normalization. Special equal segments create larger collisions.

## Identifiability

No ell0 appears. Segment phases and ordering are optical geometry. Even if a permutation landmark exists, relabeling/profile/boundary nuisance must be fixed, and a universal-scale relation is absent.

## Scope and decision

Classification `EXACT_JACOBI_CONTROL_AND_NEGATIVE_RESULT`; status determined by exact test. Piecewise-constant scalar optics, not smooth matrix Sachs or exact spacetime. Structural dead-end criteria fail. No reformulation.
