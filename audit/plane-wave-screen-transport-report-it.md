# Audit del trasporto screen nell'onda piana esatta — Italiano

- Classificazione: `EXACT_SPACETIME_TRANSPORT_WINDOW_JACOBI_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.
- Stato: `EXACT_PLANE_WAVE_SCREEN_TRANSPORT_AVERAGE_ORDER_OPERATOR_AND_JACOBI_PROTOCOL_DEPENDENT_AFFINE_SCALE_BLIND_NOT_ELL0`.
- Gate aperto: `PHYSICAL_SCREEN_CONNECTION_PATH_KERNEL_AND_COMMON_ENDPOINT_STANDARD_NOT_DERIVED`.
- UMCH: `UNPROVEN`.
- Conclusione: `NO_POSITIVE_DETECTION_CLAIM`.

## Controllo esatto

Gli oggetti raw `K`, `omega`, `Q`, `W_raw`, `W_transport`, medie degli invarianti locali, `P_raw` e `P_transport` restano primari. Con `Q'(u)=-omega(u)JQ(u)`, `Q(0)=I`, confrontiamo finestre top-hat e triangular prima/dopo il trasporto e le full Jacobi map generate da `K` rispetto a `Q^TKQ`.

La connessione nulla produce collisione esatta. Per connessione variabile, la differenza window top-hat è `0.05616345051019392`, la differenza map `0.07473073933120217` e quella characteristic `0.012131667057574784`. Gli invarianti pointwise e medi di coniugazione coincidono, con residui `1.2412670766236366e-16` e `0`, ma non ricostruiscono window/map trasportate; i gap del rappresentante trace-only dichiarato sono `0.35342449120250813` e `0.44116218625716597`.

I residui common-basis sono sotto `4.799092327304529e-14`. Lo scaling affine/profilo/connessione preserva window trasportata dimensionless e coefficienti characteristic per kernel top-hat e triangular, con residuo massimo `8.452290561089217e-15`. Cambiare profilo di trasporto a curvatura fissata cambia window e map. Quindi trasporto, media, media degli invarianti e propagazione non sono intercambiabili, e nessun `ell0` è identificato.

## Fonte e ambito

Coley–McNutt–Milson 2012, DOI `10.1088/0264-9381/29/23/235023`, supporta onde piane di Brinkmann esatte nel vuoto e deviazione geodetica guidata dalla curvatura. Connessione screen scelta, path/anchor, window/kernel, standard endpoint, legge affine, UMCH, `ell0` e detection sono non stabiliti dalla fonte.

`omega` è un input di protocollo progettuale. Tetradi source/observer fisiche, trasporto screen Fermi/parallelo, supporto causale, calibration comune indipendente e altre geometrie esatte restano aperti. Questo non è un vicolo cieco strutturale. Nessun dato o claim di detection.
