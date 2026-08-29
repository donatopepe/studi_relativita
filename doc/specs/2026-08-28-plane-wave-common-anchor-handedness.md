# Exact plane-wave common-anchor handedness gate

## Objective and classification

Test the remaining `COMMON_ENDPOINT_ANCHOR_REMAINS_OPEN` route for the exact plane-wave `(W,B)` control: determine precisely which anchor structure preserves raw profile-reversal information, and whether it restores absolute-scale or `ell0` identifiability.

Classification: `EXACT_SPACETIME_CROSS_CHANNEL_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.

## Candidate designs

1. **Independent endpoint frames.** Already tested; `B` and `B^T` share one `SO(2)xSO(2)` orbit and reversal is lost.
2. **Common oriented screen anchor (`SO(2)` conjugation).** Selected. Once source and observer screens are physically identified, `B -> Q B Q^T`. The antisymmetric coefficient
   `a(B)=(B21-B12)/2=-tr(JB)/2`, `J=[[0,-1],[1,0]]`,
   is invariant because `QJQ^T=J` for `Q in SO(2)`, and flips under `B -> B^T`.
3. **Common unoriented anchor (`O(2)` conjugation).** Selected as counterexample. Reflections obey `QJQ^T=det(Q)J`; therefore the sign of `a(B)` is not invariant unless handedness is physically fixed.

## Exact controls

Use the same exact vacuum Brinkmann plane-wave profile, centered affine interval, parallel screen, and Jacobi vertex boundary as the preceding cross-channel gates.

- Verify generic reversal has nonzero `a(B)` and `a(B_rev)=-a(B)`.
- Verify arbitrary common rotations preserve `a(B)`.
- Verify a common reflection flips `a(B)` and places the two signs in the same `O(2)` orbit.
- Verify independent endpoint rotations can reproduce transpose equivalence.
- Verify affine/profile rescaling preserves the dimensionless handed statistic `a(B)/L`; even a certified oriented common anchor does not restore absolute support scale.

## Interpretation and limits

This is a bounded conditional recovery of profile orientation, not a universal-scale landmark. The exact Brinkmann parallel screen supplies a mathematical common trivialization, but no detector, source/observer tetrad, parity convention, or observational calibration. A physical common oriented anchor therefore remains an external protocol requirement. `ell0` is absent. No data, mechanism, detection, structural dead end, or reformulation is declared.
