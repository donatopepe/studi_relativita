# Holonomy orientation tomography control

## Question

Can preregistered loop orientations recover operator shape or a universal scale?

## Leading model

In a fixed bivector basis, leading small-loop responses satisfy `h = ell^2 M k`, where `k` is a finite-dimensional curvature-operator coordinate vector and rows of `M` encode loop area-bivector orientations. This is a deterministic linearized protocol control, not an exact finite-loop GR solution.

## Counterexamples

- Rank-deficient `M` leaves a null space: distinct curvature operators yield identical holonomy records.
- Full-column-rank `M` recovers `ell^2 k` at a fixed known `ell`.
- Joint rescaling `ell -> alpha ell`, `k -> k/alpha^2` leaves `h` unchanged if curvature amplitude is not independently fixed.
- Multi-scale records can show profile changes, but no `ell0` is present unless theory supplies an independently fixed landmark/map.

## Decision

Orientation diversity solves operator tomography only under a rank gate. It does not solve universal-scale identification. Status `HOLONOMY_TOMOGRAPHY_RANK_CONDITIONAL_ELL0_ABSENT` and `NO_POSITIVE_DETECTION_CLAIM`.

No reformulation gate: Jacobi spectra, transport beyond leading order, boundaries and cross-channel maps remain open.
