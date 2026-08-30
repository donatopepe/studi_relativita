# Audit: rango cross-channel del radar Schwarzschild

## Verdetto

`ANCHORED_RADAR_TIME_AND_BOOST_RAPIDITY_LOCALLY_FULL_RANK_IN_DIMENSIONLESS_ENDPOINT_TOY_MAP_BUT_ORIENTATION_QUOTIENT_GLOBAL_COLLISION_AND_ABSOLUTE_SCALE_BLIND_NOT_ELL0`

Scope: `SCHWARZSCHILD_STATIC_RADAR_TIMING_AND_LEVI_CIVITA_BOOST_MAP_WITH_IDEAL_MIRROR_COMMON_STATIC_TETRAD_FAMILY_AND_NO_DETECTOR_COVARIANCE`.

Gate: `PHYSICAL_CHANNEL_COVARIANCE_ORIENTED_TETRAD_CALIBRATION_FREELY_FALLING_ENDPOINTS_MIRROR_READOUT_ABSOLUTE_STANDARD_AND_ELL0_LAW_NOT_DERIVED`.

UMCH: `UNPROVEN`. Detection: `NO_POSITIVE_DETECTION_CLAIM`. Vicolo cieco strutturale: `NOT_DECLARED`.

## Risultato riproducibile

Per `M=1,r_o=7,r_m=4`, il residuo di ricostruzione del boost è `4.76247466510716e-12`. Il determinante Jacobiano congiunto è `0.24720445606033067`; il valore singolare raw minore è `0.05792048249378249`. La tangente a durata fissata cambia la rapidità con segno di `-0.05796531852116355` per unità del parametro tangente.

Il quotient pari di orientazione resta localmente di rango due, con valore singolare minore `0.009280233527716465`, ma il reversal produce una collisione globale tra `eta` e `-eta`. La coniugazione comune preserva i dati caratteristici. La dilatazione di scala preserva l'output congiunto adimensionale mentre cambia la durata propria. Il minimo della scansione interna è `0.00017366826156943785`; la griglia finita non dimostra un teorema globale.

## Limite interpretativo

Il rango locale non è indipendenza dei canali. Tempo e olonomia derivano dalla stessa geometria Schwarzschild e dallo stesso boundary selezionato; non sono derivati rumore/covarianza congiunti o readout vectoriale. Collisione globale, cecità alla scala assoluta, specchio ideale, endpoint statici accelerati e anchor di tetrade comune impediscono un'interpretazione in termini di `ell0`.

Le fonti `Schwarzschild2003Translation`, `AmbroseSinger1953` e `Lin2020RadarCoordinates` sostengono solo geometria, background dell'olonomia e contesto delle coordinate radar. Non stabiliscono rango degli endpoint, covarianza del detector, UMCH o detection.
