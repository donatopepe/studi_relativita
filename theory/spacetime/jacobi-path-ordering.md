# Noncommuting Jacobi path ordering

Classification: `TOY_CONTROL_AND_NEGATIVE_RESULT`.

Status: `JACOBI_PATH_ORDER_REQUIRED_LOCAL_SPECTRA_INSUFFICIENT`; `NO_POSITIVE_DETECTION_CLAIM`.

For piecewise constant screen matrix `K`, first-order generator is `G(K)=[[0,I],[-K,0]]`. Finite propagation is ordered product of segment maps. Reversing two noncommuting segments changes endpoint map although unordered collection of local spectra and integrated trace is unchanged. Therefore instantaneous eigenvalue histogram or average is not sufficient statistic for finite-path Jacobi response.

Important nuance: commuting optical matrices alone do not generally imply commuting first-order generators; safe order independence requires generator commutation (identical-segment control is used). Ordered matrix history, covariant screen transport, affine normalization and source/observer boundary data must be retained.

Commutator/order sensitivity is geometric and path-dependent, not an `ell0` observable. `ell0` is absent unless theory supplies injective nuisance-quotiented dependence on `ell/ell0` or fixed landmark relation.

Computation uses second-order segment propagator only, not exact Sachs integration. Exact varying-matrix geometries remain open; no core reformulation is triggered.
