# Operational Spacetime Response Protocols

## Goal

Complete currently schematic `R_hol`, `R_clock`, `R_null`, and `R_cong`, and make vacuum-frame/`ell0` identifiability requirements explicit without claiming measurements.

## Fixed boundaries

- Finite-region, dimensionless responses at `ell>=ell0`.
- Raw vector remains public; `C_2` and `C_infinity` preregistered.
- Geodesic `a=0` allowed; no reaction force.
- `FRAME_UNRESOLVED` cannot confirm.
- No real data, detection, or `ell0` estimate in this milestone.

## Protocol components

### Holonomy

Use small finite loops with preregistered shape/orientation and area bivector `Sigma^{mu nu}`. Leading response scales as norm of curvature action on loop area. Define normalized toy/exact-case response only where approximation/order is declared. Loop optimization after results prohibited.

### Clock networks

Compare proper-time residuals between preregistered worldlines after subtracting flat kinematic baseline. Response is absolute fractional residual using fixed reference duration. Network geometry and synchronization convention declared.

### Null bundles

Use optical Jacobi/Sachs observables: convergence/shear or Jacobi-map departure from flat propagation, normalized at fixed affine/source-observer geometry. Caustics and affine normalization explicitly scoped.

### Congruences

Use expansion/shear/vorticity departures from matched flat congruence over fixed scale. Initial congruence data are preregistered; arbitrary congruence selection prohibited.

## Frame hierarchy

Implement decision schema:

1. unique timelike `Tmunu` eigenvector → `MATTER_FRAME_RESOLVED`;
2. vacuum with unique preregistered cosmological continuation → `CMB_CONTINUATION_RESOLVED`;
3. otherwise `FRAME_UNRESOLVED`.

No confirmation from unresolved cases.

## Identifiability

`ell0` identifiable only if:

- physical frame resolved;
- region/scale and response protocol fixed;
- norm/family fixed;
- response likelihood/uncertainty model exists;
- null and positive families distinguishable over sampled scales;
- nuisance degeneracies bounded.

Otherwise `NON_IDENTIFIABLE`.

## Exact/toy controls

Minkowski must return zero for every protocol. Curved toy controls may return nonzero only with equations/assumptions stated. Results are definition tests, not positive-floor evidence.

## Acceptance

Bilingual protocol docs/audit, deterministic calculations, tests, roadmap update, and CI. Core remains `UNPROVEN`; no positive detection claim.
