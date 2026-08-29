# Audit congiunto window/full-map dello spettro canonico comune nell'onda piana esatta — Italiano

## Ledger

- Classificazione: `EXACT_SPACETIME_CROSS_CHANNEL_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT`.
- Stato: `EXACT_PLANE_WAVE_WINDOW_FULL_MAP_COMMON_SPECTRUM_JOINT_AFFINE_ORBIT_NOT_ELL0`.
- Gate aperto: `PHYSICAL_PROFILE_SCALE_LAW_CAUSAL_WINDOW_AND_COMMON_STANDARD_NOT_DERIVED`.
- UMCH remains `UNPROVEN`.
- Conclusione: `NO_POSITIVE_DETECTION_CLAIM`.

## Risultato counterexample-first

`W`, `A`, `B`, `C`, `D` raw restano primari. Il characteristic polynomial è una diagnostica dipendente della full map sotto calibrazione canonica comune. Testiamo l'oggetto congiunto `(LW, chi_P)` per kernel top-hat e triangular centrati e scale-covariant.

Per

`K_s(u)=s^{-2}K(u/s)`, `L_s=sL`,

la sostituzione nella window dà `L_s W_s(L_s)=L W(L)`. Con `T_s=diag(s^{-1/2}I,s^{1/2}I)`, i blocchi raw soddisfano `A_s=A`, `B_s=sB`, `C_s=C/s`, `D_s=D`, e la full map soddisfa `P_s=T_s^{-1}PT_s`. Il characteristic polynomial resta quindi invariato.

Questa è una collisione esatta dell'intero oggetto congiunto, non un fit di gain scalare. Ogni landmark estratto solo da questo oggetto si sposta dalla coordinata `L_*` a `sL_*` mentre la risposta resta invariata. Profili diversi cambiano ancora matrice window e spettro, quindi l'oggetto resta condizionalmente informativo sul profilo. Non identifica scala assoluta del supporto o `ell0`.

## Fonte e limiti

Coley–McNutt–Milson (2012), DOI `10.1088/0264-9381/29/23/235023`, supporta onde piane di Brinkmann esatte nel vuoto e deviazione geodetica guidata dalla curvatura. Scelta finite-window, kernel, standard detector comune, dilatazione del profilo come nuisance osservativa, UMCH, `ell0` e detection non sono stabiliti dalla fonte; tali elementi sono non stabiliti dalla fonte canonica.

Standard dimensionali indipendenti, boundary causali non scale-covariant, leggi fisiche del profilo fissate, calibrazione detector e altre geometrie esatte restano aperti. Questo non è un vicolo cieco strutturale. Nessun dato o claim di detection.
