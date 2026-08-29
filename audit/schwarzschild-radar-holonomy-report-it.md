# Audit — olonomia radar statica in Schwarzschild

## Decisione

`SCHWARZSCHILD_STATIC_RADAR_CAUSAL_BOUNDARY_HOLONOMY_PROTOCOL_DEPENDENT_AND_GEOMETRIC_SCALE_BLIND_NOT_ELL0`

Ambito: `FOUR_DIMENSIONAL_SCHWARZSCHILD_LEVI_CIVITA_CONNECTION_ON_IDEAL_STATIC_OBSERVER_RADAR_BOUNDARY_WITH_UNDERIVED_MIRROR_AND_READOUT`.

Gate: `PHYSICAL_FREELY_FALLING_ENDPOINTS_MIRROR_ACTION_VECTOR_READOUT_COMMON_STANDARD_AND_ELL0_LAW_NOT_DERIVED`.

UMCH: `UNPROVEN`. Inferenza: `NO_POSITIVE_DETECTION_CLAIM`. `ell0_identified=false`; `positive_detection_claim=false`; `structural_dead_end=NOT_DECLARED` (`NOT_DECLARED`).

## Protocollo e risultati

L'osservatore statico a `r_o=7M` emette verso lo specchio ideale `r_m=4M`; il ritorno e radiale nullo futuro; il confronto si chiude all'indietro sulla worldline dell'osservatore. Con `r_*=r+2M log(r/(2M)-1)`, `Delta tau=2 sqrt(f(r_o))[r_*(r_o)-r_*(r_m)]`.

| Controllo | Risultato |
|---|---:|
| `Delta tau` | `8.168553570818094` |
| residuo nullo massimo | `3.552713678800501e-15` |
| residuo di Lorentz | `7.338356754219182e-12` |
| `||H_radar-I||` | `0.22713493607514745` |
| differenza raw causale/rettangolo matched | `0.8239284342654838` |
| residuo olonomia sull'orbita di scala | `1.798766884999431e-16` |

Lo stesso `Delta tau/M` collide per boundary osservatore/specchio differenti: `duration_only_identifies_boundary=false`. Le matrici raw ancorate separano la coppia toy testata solo sotto l'identificazione di frame dichiarata per la famiglia statica. Il reversal resta visibile nel raw, ma i coefficienti caratteristici collidono. Rotazioni comuni della tetrade coniugano la matrice raw. Lo spettro non deriva orientazione o anchor fisico.

La trasformazione `(M,r_o,r_m)->s(M,r_o,r_m)` conserva tempo radar adimensionale e olonomia tetradica mentre cambia il tempo proprio. Non compare alcuna legge in `ell/ell0`.

Gate cross-channel: `TRAVEL_TIME_CURVATURE_AND_HOLONOMY_SHARE_DECLARED_GEOMETRY_AND_ARE_NOT_ASSUMED_INDEPENDENT`. non-Abelianity does not imply independent rank.

## Fonte e limiti

Lin 2020, DOI `10.1103/PhysRevD.101.124001`, supporta solo coordinate radar per osservatori localizzati e casi Schwarzschild-like. Specchio statico ideale, loop Levi-Civita finito, chiusura, readout vettoriale e test di identificabilita sono scelte/derivazioni del progetto. Gli endpoint statici sono accelerati; azione dello specchio, standard comune, readout del detector, covarianza e legge di `ell0` non sono derivati. Non si rivendicano meccanismo, dati, bound o detection.
