# Operational response vector

Preserve raw vector

`R=(R_tidal,R_mag,R_hol,R_clock,R_null,R_cong)`.

Candidate dimensionless responses include `R_tidal=ell^2 RMS(E_mn)`, `R_mag=ell^2 RMS(B_mn)`, normalized finite-loop holonomy, differential clock response, null-bundle distortion, and congruence deformation.

Preregister `C_2=||R||_2` and `C_infinity=||R||_infinity` as descriptive summaries. Never switch norm after data. Raw vector remains primary and public.

Channels can encode correlated aspects of same geometry. Norms are not six independent evidences and do not define likelihood factorization. Positive inference requires preregistered joint covariance/dependence model. Without it status is `DEPENDENCE_UNRESOLVED`; `C_2`/`C_infinity` may be reported but cannot confirm.

Exact loop/kernel/subtraction/uncertainty protocols remain required before observational use. This correction removes hidden independence assumption; it does not prove channel completeness or a floor.
