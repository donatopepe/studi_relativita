# Candidate A — Hard pointwise constraint

Scientific status: `UNPROVEN`  
Hypothesis class: `POINTWISE_UMCH`

## Domain

Regular timelike worldlines for which proper worldline curvature `κ` is defined. The boundary `κ=0` requires separate treatment because the Frenet normal is undefined there.

## Candidate functional

Schematic constrained functional:

\[
S_A[x,\lambda]=S_0[x]+\int ds\,\lambda(s)(\kappa_0-\kappa).
\]

Provisional complementarity convention:

\[
\lambda\ge0,\qquad \kappa-\kappa_0\ge0,
\qquad \lambda(\kappa-\kappa_0)=0.
\]

Sign and boundary terms must be checked by explicit variation before use.

## Analysis level

`CONJECTURAL` pending variational and constraint audit. Literature on curvature actions supplies methods, not validation of this inequality.

## Differential order

`INCOMPLETE`: dependence on `κ`, which contains second derivatives of the embedding in proper-time gauge, generally leads to higher-order embedding equations after variation. Degeneracy and constraints must be calculated.

## Constraints

KKT-like inequality conditions are proposed. No Dirac first-/second-class classification is claimed. Feasibility, active-set transitions, and admissible initial data remain unresolved.

## Standard limit

Required: as `κ₀→0`, recover standard free relativistic dynamics without residual multiplier forces. This is not established; inactive branch conflicts with enforcing strictly positive curvature.

## Observable

None derived. A trajectory constraint alone does not map to a measured residual acceleration.

## Blocking issue

Need a covariant nonsmooth variational formulation with well-posed active/inactive evolution and a standard limit.
