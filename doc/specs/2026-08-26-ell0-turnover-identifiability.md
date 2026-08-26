# Mathematical unlock candidate for ell0

## Problem

Current monotone families absorb `ell0` into free amplitude/shape combinations. Seek a family whose scale dependence contains an amplitude-independent landmark.

## Candidate family

For `x=ell/ell0>=1`, preregister

`F_T(x)=A x^p exp[-q(x-1)]`, with `A>0` and fixed theory-derived `p>q>0`.

This is not adopted as physical UMCH law. It is a mathematical candidate requiring independent derivation before data use.

## Identifiability

For two distinct scales with positive exact responses,

`log[y1/y2]=p log(ell1/ell2)-q(ell1-ell2)/ell0`,

so

`ell0=q(ell1-ell2)/(p log(ell1/ell2)-log[y1/y2])`,

when denominator is nonzero and signs/domain are consistent. Amplitude cancels. Then `A` follows from either response.

Equivalent landmark: logarithmic elasticity

`d log F_T / d log ell = p-q ell/ell0`

vanishes at `ell_peak=(p/q)ell0`; hence `ell0=(q/p)ell_peak`.

## Necessary restrictions

- `p,q` fixed before data by independent theory, not fitted jointly with `ell0`.
- observed scale interval spans enough shape/turnover information;
- positive response and resolved frame;
- raw vector, norm, channel, regions, uncertainty, and null comparison preregistered;
- `ell>=ell0` checked after inference without discarding unfavorable samples;
- compare `F_T` against `F_0` and existing families without post-data selection.

If `p,q` are free, degeneracy returns through `q/ell0`. If turnover lies outside observed interval, practical identifiability may fail despite structural identifiability.

## Scientific status

`MATHEMATICAL_IDENTIFIABILITY_CANDIDATE_ONLY`. No physical derivation, data, ell0 value, floor, or detection. Current UMCH remains `UNPROVEN`; existing families remain structurally non-identifiable.
