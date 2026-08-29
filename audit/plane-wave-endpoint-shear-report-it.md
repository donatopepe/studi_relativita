# Audit della calibrazione shear endpoint nell'onda piana esatta — Italiano

## Ledger

- Classificazione: `EXACT_SPACETIME_CROSS_CHANNEL_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.
- Stato: `EXACT_PLANE_WAVE_LABELLED_ENDPOINT_OPTICAL_SPECTRA_NONIDENTIFIABLE_UNDER_CANONICAL_SHEAR_CALIBRATION_NOT_ELL0`.
- Gate aperto: `PHYSICAL_PHASE_SPACE_ENDPOINT_CALIBRATION_NOT_DERIVED`.
- UMCH remains `UNPROVEN`.
- Conclusione: `NO_POSITIVE_DETECTION_CLAIM`.

## Risultato counterexample-first

Manteniamo endpoint source/observer etichettati e blocchi raw `A`, `B`, `C`, `D`. Per matrici di calibrazione endpoint-local simmetriche, definiamo

`S(H)=[[I,0],[H,I]]`,

e

`P'=S(H_o)P S(H_s)^{-1}`.

Questi shear sono simplettici e conservano le label endpoint. L'algebra esatta dei blocchi dà `A'=A-BH_s`, `B'=B`, `D'=D+H_oB` e `C'=C+H_oA-(D+H_oB)H_s`. Di conseguenza le matrici ottiche endpoint trasformano come

`(B')^{-1}A'=B^{-1}A-H_s`,

`D'(B')^{-1}=DB^{-1}+H_o`.

Shear simmetrici liberi muovono spettri endpoint, gap fra autovalori ed eigenframe. Gli shear scalari muovono già gli autovalori assoluti conservando i gap. Le sole label endpoint non rendono quindi questi spettri ottici invarianti di calibrazione.

Il rescaling affine/del profilo resta esatto quando `H` scala come `1/L`; la full map calibrata adimensionale resta invariata. Scala assoluta del supporto ed `ell0` restano non identificati.

## Scope e limiti

Questo nuisance model bounded non elimina ogni invariante della full map: `B` resta invariato. Non stabilisce non-identificabilità sotto ogni gruppo di calibrazione fisico. Servono ancora derivazione indipendente delle variabili phase-space misurate, tetradi source/observer, transport, gain, leakage e risposta detector.

Coley–McNutt–Milson (2012), DOI `10.1088/0264-9381/29/23/235023`, supporta onde piane di Brinkmann esatte nel vuoto e deviazione geodetica guidata dalla curvatura. Calibrazione shear endpoint, protocollo finite-window, osservabilità detector, UMCH, `ell0` e detection sono scelte o claim progettuali, non stabiliti dalla fonte.

Osservabili Sachs completi, finestre causali, restrizioni fisiche di calibrazione e altre geometrie esatte restano aperti. Questo non è un vicolo cieco strutturale. Nessun dato o claim di detection.
