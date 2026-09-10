# Kerr finite-boundary parallel-screen gate

## Construction

`GrallaLupsasca2020KerrNullGeodesics` supplies the finite Kerr path. `Dolan2018GeometricalOptics` supplies transversality and parallel transport of screen/polarization vectors in leading geometrical optics.

At the source ZAMO endpoint, with local ray direction `(n_r,0,n_phi)`, screen order is

```text
s_1=e_theta
s_2=n_phi e_r-n_r e_phi
```

Both screen vectors and tangent are integrated through the turning point with `k^nu nabla_nu s_A=0`. At observer, the quotient map is `Q_AB=g(s_A^transported,s_B^observer)`.

## Negative quotient result

Connection compatibility, tangent transport, screen orthonormality/transversality, endpoint map, path reversal, orientation convention, Schwarzschild reflection, and scale gate all pass: `8/8`.

For equal and unequal endpoint radii,

```text
equal_Q=[[1.0,0.0],[0.0,1.0]]
unequal_Q=[[1.0,0.0],[0.0,1.0]]
screen_quotient_rank=0
path_orientation_difference=7.7337185
geodesic_residual=0.0
screen_residual=0.0
scale_residual=0.0
scale_null_direction=[1.0,0.0,0.0,0.0,0.0]
```

The equatorial symmetry and the endpoint basis constructed directly from each local ray make the parallel-screen quotient collide, despite distinct oriented Kerr path labels. `Q` is not a detector Jones matrix. Raw transported vectors remain nontrivial coordinate records, but no independent quotient shape survives this protocol.

## Result and next solution

```text
KERR_EQUATORIAL_FINITE_BOUNDARY_PARALLEL_SCREEN_TRANSPORT_IS_METRIC_COMPATIBLE_BUT_ENDPOINT_SCREEN_QUOTIENT_COLLIDES_UNDER_EQUATORIAL_SYMMETRY_WHILE_JOINT_DILATION_RETAINS_SCALE_BLINDNESS_NOT_ELL0
MODEL_LEVEL_KERR_PARALLEL_SCREEN_CONFORMANCE_NOT_EVIDENCE
PHYSICAL_KERR_SCREEN_PREPARATION_POLARIZATION_SOURCE_ANALYZER_JACOBI_TIDAL_MAP_CAUSTICS_RECEIVER_NOISE_JOINT_COVARIANCE_DATA_5D_COMPARATOR_AND_ELL0_LAW_NOT_DERIVED
```

Next useful solution is Jacobi tidal map evolution on this verified transported screen, not more endpoint-basis tuning. That can test focusing/shear beyond the rank-zero screen quotient. Physical preparation, analyzer, receiver, covariance, data, 5D comparator, and `ell0` remain separate.
