# Audit mareale a finestra finita Kaluza–Klein compatto linearizzato

## Stato

```text
HIGHER_DIMENSIONAL_GRAVITY_CORE=REFORMULATION_CANDIDATE_UNRATIFIED
UMCH=UNPROVEN_SECONDARY_CANDIDATE
L_identified=false
ell0_identified=false
L_equals_ell0=NOT_DERIVED
extra_dimension_detected=false
structural_dead_end=NOT_DECLARED
NO_POSITIVE_DETECTION_CLAIM
MODEL_LEVEL_DIMENSIONLESS_KK_SHAPE_DERIVED_NOT_EVIDENCE
```

Record di chiusura diretto: `DIRECT_REVIEW_NO_SUBAGENT`. Non è revisione indipendente.

## Modello e record primario

Il background toy limitato è `M5=R1,3 x S1`, con `y~y+2*pi*L`. Il potenziale scalare statico supportato dalle fonti viene differenziato per formare la Hessiana mareale debole di progetto `T_ij=partial_i partial_j Phi`. Sono preservati matrici raw complete, autovalori radiale/trasversale, profili circolari di sorgente/probe, profilo tridimensionale della sorgente e geometria della finestra finita. La Hessiana non è una perturbazione tensoriale cinque-dimensionale completa con gauge fissato.

Scope canonico: `Liu2003CompactifiedPotential` supporta il potenziale puntiforme esatto sul cerchio compatto; `FloratosLeontaris1999` supporta la somma KK e i limiti corto/lungo; `KehagiasSfetsos2000` supporta automodi KK e range/degenerazione Yukawa leading. Nessuna fonte stabilisce questo protocollo a finestra finita, identificabilità, `ell0`, UMCH o detection.

## Baseline deterministica

```text
L=1.0
r=2.0
source_size=0.25
shell_width=0.3
T_parallel=-0.74695386
T_perpendicular=0.25463712
n_used=123
rank=2
scale_null_direction=[1.0,0.0,0.0]
dimensionless_point_matrix_residual=0.0
dimensionless_shell_matrix_residual=0.0
```

Sorgenti puntiforme, sfera uniforme e gaussiana sono incrociate con profili circolari localizzati/uniformi. Finestre a guscio radiale e box orientato preservano matrici raw. Profili uniformi di sorgente o probe proiettano via i modi Fourier non nulli; è proiezione del protocollo, non assenza di dimensione extra.

## Controesempi e risultato

```text
UNIFORM_S1_SOURCE_OR_PROBE_PROJECTS_NONZERO_KK_MODES_NOT_ABSENCE_OF_EXTRA_DIMENSION
SOURCE_PROFILE_AND_WINDOW_SHAPE_ARE_PREPARATION_NUISANCES_NOT_INTRINSIC_GEOMETRY
JOINT_5D_GEOMETRIC_DILATION_NOT_INTERIOR_ABSOLUTE_SCALE
L_NOT_IDENTIFIABLE_WITHOUT_SOURCE_PROBE_AND_WINDOW_CALIBRATION
DEPENDENCE_UNRESOLVED_WITHOUT_JOINT_COVARIANCE
```

Risultato bounded primario:

```text
LOCALIZED_SOURCE_PROBE_KK_TOWER_ADDS_DIMENSIONLESS_FINITE_WINDOW_TIDAL_SHAPE_BUT_UNIFORM_PROFILE_PROJECTION_SOURCE_WINDOW_DEGENERACY_AND_JOINT_5D_DILATION_PREVENT_ABSOLUTE_SCALE_OR_ELL0_IDENTIFICATION
```

La forma a livello di modello non è evidenza per una dimensione extra. Più modi, sorgenti, finestre o entry di matrice non stabiliscono indipendenza fisica o identificabilità globale.

Gate fisico:

```text
NONLINEAR_5D_DYNAMICS_RADION_STABILIZATION_MATTER_LOCALIZATION_SOURCE_PROBE_PREPARATION_ABSOLUTE_COUPLING_CLOCK_RECEIVER_CALIBRATED_NOISE_JOINT_COVARIANCE_DATA_AND_ELL0_LAW_NOT_DERIVED
```
