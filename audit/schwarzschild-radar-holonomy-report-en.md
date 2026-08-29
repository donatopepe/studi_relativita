# Audit — Schwarzschild static-radar holonomy

## Decision

`SCHWARZSCHILD_STATIC_RADAR_CAUSAL_BOUNDARY_HOLONOMY_PROTOCOL_DEPENDENT_AND_GEOMETRIC_SCALE_BLIND_NOT_ELL0`

Scope: `FOUR_DIMENSIONAL_SCHWARZSCHILD_LEVI_CIVITA_CONNECTION_ON_IDEAL_STATIC_OBSERVER_RADAR_BOUNDARY_WITH_UNDERIVED_MIRROR_AND_READOUT`.

Gate: `PHYSICAL_FREELY_FALLING_ENDPOINTS_MIRROR_ACTION_VECTOR_READOUT_COMMON_STANDARD_AND_ELL0_LAW_NOT_DERIVED`.

UMCH: `UNPROVEN`. Inference: `NO_POSITIVE_DETECTION_CLAIM`. `ell0_identified=false`; `positive_detection_claim=false`; `structural_dead_end=NOT_DECLARED` (`NOT_DECLARED`).

## Protocol and results

Static observer at `r_o=7M` emits inward to ideal mirror `r_m=4M`; return is future radial null; comparison closes backward on observer worldline. With `r_*=r+2M log(r/(2M)-1)`, `Delta tau=2 sqrt(f(r_o))[r_*(r_o)-r_*(r_m)]`.

| Check | Result |
|---|---:|
| `Delta tau` | `8.168553570818094` |
| maximum null residual | `3.552713678800501e-15` |
| Lorentz residual | `7.338356754219182e-12` |
| `||H_radar-I||` | `0.22713493607514745` |
| causal/matched-rectangle raw difference | `0.8239284342654838` |
| scale-orbit holonomy residual | `1.798766884999431e-16` |

Fixed `Delta tau/M` collides for different observer/mirror boundaries: `duration_only_identifies_boundary=false`. Anchored raw matrices separate tested toy pair only under declared static-family frame identification. Reversal remains raw-visible but characteristic coefficients collide. Common tetrad rotations conjugate raw matrix. Spectrum does not derive orientation or physical anchor.

Scaling `(M,r_o,r_m)->s(M,r_o,r_m)` preserves dimensionless radar time and tetrad holonomy while changing proper time. No `ell/ell0` law appears.

Cross-channel gate: `TRAVEL_TIME_CURVATURE_AND_HOLONOMY_SHARE_DECLARED_GEOMETRY_AND_ARE_NOT_ASSUMED_INDEPENDENT`. non-Abelianity does not imply independent rank.

## Source and limitations

Lin 2020, DOI `10.1103/PhysRevD.101.124001`, supports radar coordinates for localized observers and Schwarzschild-like cases only. Ideal static mirror, finite Levi-Civita loop, closure, vector readout and identifiability tests are project choices/derivations. Static endpoints are accelerated; mirror action, common standard, detector readout, covariance and `ell0` law remain underived. No mechanism, data, bound or detection is claimed.
