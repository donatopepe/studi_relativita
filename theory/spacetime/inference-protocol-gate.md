# Inference protocol gate

This gate operationalizes corrected assumptions; passing it is eligibility, not evidence.

Order:

1. resolved frame or `FRAME_UNRESOLVED`;
2. fixed survey domain and `ell0<=ell_min` or `DOMAIN_INCONSISTENT`;
3. prospectively fixed/derived family or `EXPLORATORY_FAMILY_SELECTION`;
4. joint channel dependence model or `DEPENDENCE_UNRESOLVED`;
5. calibrated uncertainty likelihood or `LIKELIHOOD_UNRESOLVED`;
6. bounded nuisance model or `NUISANCE_UNBOUNDED`;
7. structural/practical identifiability or `NON_IDENTIFIABLE`;
8. independent replication or `REPLICATION_MISSING`.

Passing every gate yields `CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE`, never a detection. Raw vector and F_0 remain mandatory. Current project has no eligible real-data analysis and retains `NO_POSITIVE_DETECTION_CLAIM`.
