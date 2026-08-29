# Audit della mappa Jacobi completa nell'onda piana esatta — Italiano

## Ledger

- Classificazione: `EXACT_SPACETIME_CROSS_CHANNEL_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.
- Stato: `EXACT_PLANE_WAVE_FULL_JACOBI_LABELLED_ENDPOINT_ORDER_CONDITIONAL_SWAP_AND_AFFINE_SCALE_NONIDENTIFIABLE_NOT_ELL0`.
- Gate aperto: `PHYSICAL_ENDPOINT_LABELS_AND_CALIBRATION_NOT_DERIVED`.
- UMCH remains `UNPROVEN`.
- Conclusione: `NO_POSITIVE_DETECTION_CLAIM`.

## Risultato counterexample-first

Il controllo esatto conserva i blocchi phase-space raw `A`, `B`, `C`, `D` e verifica la simpletticità. Per il profilo ottico simmetrico invertito,

`P_rev=E P^T E`,

che dà `A_rev=D^T`, `B_rev=B^T`, `C_rev=C^T` e `D_rev=A^T`.

Quando `B` è invertibile, le matrici ottiche source e observer `B^{-1}A` e `DB^{-1}` hanno genericamente spettri diversi. Il reversal scambia tali spettri. I blocchi derivativi conservano quindi l'orientazione del profilo solo con label fisiche source/observer, normalizzazione affine, screen transport e calibrazione endpoint fissati prospetticamente.

Se endpoint swap appartiene al nuisance quotient, `P` e `P_rev` sono esattamente equivalenti. Nel rescaling affine/del profilo, `A` e `D` restano invariati, `B` scala con `s` e `C` con `1/s`; la mappa completa adimensionale resta invariata. Scala assoluta del supporto ed `ell0` restano non identificati.

## Scope

Coley–McNutt–Milson (2012), DOI `10.1088/0264-9381/29/23/235023`, supporta onde piane di Brinkmann esatte nel vuoto e deviazione geodetica guidata dalla curvatura. Protocollo full-map, boundary scelto, label endpoint, endpoint swap, calibrazione detector, UMCH, `ell0` e detection sono scelte o claim progettuali, non stabiliti dalla fonte.

I blocchi raw restano primari; gli spettri endpoint sono diagnostiche dipendenti. Nessun osservabile derivativo fisico o calibrazione è derivato. Restano route con endpoint fisicamente etichettati, osservabili Sachs completi, finestre causali, transport e altre geometrie esatte; non è un vicolo cieco strutturale. Nessun dato o claim di detection.
