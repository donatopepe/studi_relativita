# Transport gauge quotient for operator comparison

## Question

Can apparent nonradial operator evolution be caused solely by scale-dependent frame/basis transport?

## Control

Use real symmetric 2x2 operator `A=diag(a,b)` and rotated representations `A(theta)=Q(theta) A Q(theta)^T`. Coordinate entries change and vectorized projective direction may move, while trace, determinant and eigenvalues remain invariant.

Compare true spectral evolution where eigenvalue ratio changes against pure conjugation. This is finite-dimensional linear algebra, not a spacetime transport derivation.

## Gates

- Without fixed/certified transport or conjugacy quotient, coordinate nonradiality is gauge/basis ambiguous.
- Orthogonal conjugation preserves spectrum; spectral ratios distinguish pure basis rotation from changed eigenvalue shape.
- Degenerate spectrum is rotation-blind and cannot identify orientation.
- Even genuine spectral evolution identifies geometry only; `ell0` is absent without theory-fixed map.
- Nonorthogonal channel calibration/transport can alter singular/eigenvalue structure and requires stronger nuisance model.

## Decision

Status `TRANSPORT_GAUGE_QUOTIENT_REQUIRED_FOR_NONRADIALITY`. No reformulation: physical transport, boundary and exact-geometry cross-channel maps remain open. `UNPROVEN`; `NO_POSITIVE_DETECTION_CLAIM`.
