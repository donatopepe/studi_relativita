# Axisymmetric orientation-moment theorem

## Question

For Schwarzschild algebraic pattern `E(n)=I-3nn^T`, what information from a general axisymmetric orientation measure controls averaged operator shape?

## Derivation

Let probability measure be invariant under rotations about z and define `mu2=<cos^2 theta>`. Then

`<nn^T>=diag((1-mu2)/2,(1-mu2)/2,mu2)`

and

`<E>=diag((3mu2-1)/2,(3mu2-1)/2,1-3mu2)`.

Thus every nonzero axisymmetric average is proportional to same axial pattern `diag(1/2,1/2,-1)`. Entire measure enters only through scalar second moment. At `mu2=1/3`, average vanishes; crossing this value reverses signed ray. Higher moments and detailed profile are invisible to averaged operator.

## Identifiability gates

- Different measures with same `mu2` are exactly observationally equivalent under this average.
- Zero/sign reversal can be placed by changing orientation measure moment.
- Unsigned projectivization erases sign reversal; signed convention must be fixed.
- Fixed covariant measure yields geometric orientation moment only.
- `ell0` is absent.

This extends uniform-cap exact angular result, still under assumed common tangent-space alignment and without Schwarzschild parallel transport/radial amplitude.

## Decision

Status `AXISYMMETRIC_ORIENTATION_AVERAGE_SECOND_MOMENT_ONLY_NOT_ELL0`. No reformulation: covariant spacetime measure/transport remains open. `UNPROVEN`; `NO_POSITIVE_DETECTION_CLAIM`.
