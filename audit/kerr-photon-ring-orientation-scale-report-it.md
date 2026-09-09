# Audit di orientazione e scala dell'anello fotonico equatoriale di Kerr

## Stato

```text
MODEL=KERR_EQUATORIAL_PHOTON_RING_4D_CONTROL
UMCH=UNPROVEN_SECONDARY_CANDIDATE
L_identified=false
ell0_identified=false
L_equals_ell0=NOT_DERIVED
extra_dimension_detected=false
structural_dead_end=NOT_DECLARED
NO_POSITIVE_DETECTION_CLAIM
MODEL_LEVEL_KERR_ORBIT_CONFORMANCE_NOT_EVIDENCE
```

Registro di chiusura diretta: `DIRECT_REVIEW_NO_SUBAGENT`. Non è revisione indipendente.

## Perimetro

Questo `4D_COMPARISON_BASELINE` controlla orbite nulle circolari equatoriali esatte nel Kerr subestremale. `Teo2003SphericalPhotonOrbits` sostiene raggi, intervallo, equazione radiale e condizioni di raggio costante. Sostituzione del parametro d'impatto, frequenza/periodo coordinati, collisioni di segno, audit di scala e rango sono derivazioni del progetto.

Nell'MVP non entrano schermo trasportato, mappa Jacobi/Sachs, frontiera finita, emettitore/assorbitore, orologio fisico, ricevitore, covarianza o dati.

## Ancora deterministica

```text
chi=0.6
x_pro=2.188914
x_retro=3.6298497
xi_pro/M=3.8384937
xi_retro/M=-6.3156493
Omega_pro*M=0.26051886
Omega_retro*M=-0.15833685
branch_minimum_gap=0.46362086
radial_residual=0.0
dimensionless_scale_residual=0.0
rank=1
scale_null_direction=[1.0,0.0]
```

`Omega_phi` e periodo sono registri coordinati di Boyer-Lindquist, non osservabili di un orologio rivelatore.

## Otto controlli

Tutti gli `8/8` controlli preregistrati passano:

1. formula e intervallo dei raggi;
2. ordinamento stretto dei rami a spin non nullo;
3. collisione Schwarzschild a `3M`;
4. conformità indipendente del potenziale radiale e della frequenza angolare;
5. collisione convenzionale sotto inversione simultanea spin/orientazione;
6. dilatazione geometrica congiunta esatta;
7. forma di spin a rango uno con direzione nulla di scala esatta;
8. gate fail-closed di mancata identificazione di `ell0`.

## Risultato limitato

```text
KERR_FRAME_DRAGGING_ADDS_PROGRADE_RETROGRADE_DIMENSIONLESS_ORBIT_SHAPE_BUT_JOINT_MA_DILATION_RETAINS_ABSOLUTE_SCALE_BLINDNESS_NOT_ELL0
PHYSICAL_KERR_SOURCE_ABSORBER_ENDPOINT_TETRAD_SCREEN_TRANSPORT_AFFINE_FREQUENCY_CLOCK_RECEIVER_NOISE_JOINT_COVARIANCE_DATA_AND_ELL0_LAW_NOT_DERIVED
```

Il trascinamento di Kerr aggiunge forma adimensionale sensibile all'orientazione. Non fornisce uno standard dimensionale interno. Quindi `M`, `a`, periodo assoluto ed `ell0` non sono identificati. Il risultato non conferma né confuta dimensioni extra o UMCH. Conformità tensoriale 5D, localizzazione finita su `S1`, risultati Schwarzschild e `F_0` restano invariati.
