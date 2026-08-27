# Admissible regions

Define survey domain `D_survey` before fitting: region construction, physical scales `ell`, scale estimator, circuit/window family, comparator, and exclusion rules are preregistered independently of response values and unknown `ell0`. Regions must be causally testable in principle and regular for selected calculation. Technology today is not definition.

For models defined only at `x=ell/ell0>=1`, every candidate parameter value must satisfy `ell0<=ell_min`, where `ell_min` is smallest preregistered scale in `D_survey`. Never discard a sample after fitting because inferred `ell0` exceeds its scale. Violation gives `DOMAIN_INCONSISTENT`, not evidence and not confirmation.

Physical frame must be resolved for confirmatory use. `FRAME_UNRESOLVED` regions cannot confirm. This protocol removes data-selection circularity; it does not identify `ell0` or establish a positive floor.
