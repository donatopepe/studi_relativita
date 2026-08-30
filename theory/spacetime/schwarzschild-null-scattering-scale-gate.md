# Schwarzschild finite-boundary null-scattering scale gate

Status: `SCHWARZSCHILD_NONRADIAL_NULL_SCATTERING_FINITE_WINDOW_OPEN_TRANSPORT_HAS_TURNING_AND_BOUNDARY_SHAPE_DIRECTIONS_BUT_RETAINS_GEOMETRIC_SCALE_BLINDNESS_NOT_ELL0`.

Scope: `FOUR_DIMENSIONAL_SCHWARZSCHILD_EQUATORIAL_FUTURE_NULL_FINITE_BOUNDARY_SCATTERING_WITH_ONE_TURNING_POINT_STATIC_ENDPOINT_TETRADS_UNIT_KILLING_ENERGY_PROJECT_NORMALIZATION_AND_NO_DETECTOR_READOUT`.

Gate: `PHYSICAL_SCATTERING_WINDOW_EMITTER_ABSORBER_TETRADS_AFFINE_FREQUENCY_STANDARD_SCREEN_JACOBI_PREPARATION_CAUSTIC_CONTINUATION_VECTOR_READOUT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED`.

For `R>rho>3`, `r_b=MR`, `r_p=M rho`, unit Killing-energy normalization fixes `beta=b/M=rho/sqrt(1-2/rho)`. The substitution `r/M=rho+y^2` regularizes the turning endpoint. Incoming and outgoing branches are matched there and integrated to the same finite static boundary.

Primary records remain the ordered path samples, coordinate connection map `T_coordinate`, endpoint-static-tetrad map `T_tetrad`, and boundary ray record. `T_tetrad` is `OPEN_PATH_ENDPOINT_TRANSPORT_NOT_HOLONOMY`. Scalar norms and characteristic summaries cannot replace either raw map.

Direct controls give null and first-integral residuals near machine precision. Endpoint-tetrad metric residuals for displayed records are at most `7.936539086169608e-11`; reverse inverse residuals are at most `2.5981380717454544e-12`. Finite boundary changes both flight time and transport: `FINITE_BOUNDARY_PROTOCOL_DIRECTION`. Orientation reversal preserves time, reverses azimuth and changes raw transport while its norm aliases: `PROJECTED_NORM_ALIAS_NOT_RAW_MAP_EQUALITY`.

Under `(M,r_p,r_b,b)->s(M,r_p,r_b,b)`, dimensionless path, `delta_t/M` and `T_tetrad` agree within numerical tolerance while coordinate-basis transport changes. Classification: `GEOMETRIC_SCALE_BLIND_AFTER_DECLARED_ENDPOINT_CONVERSION`. This differs from affine-frequency rescaling.

The feature Jacobian in `(rho,R,log M)` has `rank_shape_boundary = 2`, `rank_with_log_M = 2`, `log_M_column_norm = 1.7391780828932144e-10`, and `scale_null_direction = [0, 0, 1]`. The `R` direction is boundary/protocol dependence. Shared geometry/path and absent covariance imply `independent_channels=false`. Bounded collision search found no grid collision, but global injectivity remains `NOT_ESTABLISHED`.

`rho`, `R`, `beta`, deflection and dwell time are not `ell/ell0` or `ell0`. No detector readout, covariance, physical endpoint calibration, `ell0` law, UMCH evidence or detection is derived. UMCH remains `UNPROVEN`; structural dead end is `NOT_DECLARED` because generic scattering Sachs/Jacobi propagation and detector-derived readout remain open.
