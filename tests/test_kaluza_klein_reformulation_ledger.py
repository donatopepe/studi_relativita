import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = ROOT / "doc/specs/2026-08-30-kaluza-klein-linearized-reformulation.md"
LEDGER = ROOT / "audit/kaluza-klein-reformulation-change-ledger.md"
AUTHORITY = (
    ROOT / "README.md",
    ROOT / "README.en.md",
    ROOT / "docs/roadmap.md",
    ROOT / "papers/umch/it/main.tex",
    ROOT / "papers/umch/en/main.tex",
)

STATUSES = (
    "HIGHER_DIMENSIONAL_GRAVITY_CORE=REFORMULATION_CANDIDATE_UNRATIFIED",
    "MODEL=LINEARIZED_5D_COMPACT_KK_TOY_CONTROL",
    "UMCH=UNPROVEN_SECONDARY_CANDIDATE",
    "L_identified=false",
    "ell0_identified=false",
    "L_equals_ell0=NOT_DERIVED",
    "extra_dimension_detected=false",
    "structural_dead_end=NOT_DECLARED",
    "NO_POSITIVE_DETECTION_CLAIM",
    "MODEL_LEVEL_DIMENSIONLESS_KK_SHAPE_DERIVED_NOT_EVIDENCE",
)

PRESERVED = (
    "RATIFIED_PRIMARY_RESEARCH_OBJECT",
    "F_0",
    "CONDITIONAL_POINTWISE_NO_GO_FOR_FIXED_A_AND_B",
    "ELL0_STRUCTURALLY_NON_IDENTIFIABLE_UNDER_CURRENT_FAMILIES",
    "PROJECTIVE_SCALE_NON_IDENTIFIABLE_IN_CURRENT_EXACT_CONTROLS",
    "REISSNER_NORDSTROM_CHARGE_ADDS_DIMENSIONLESS_RICCI_WEYL_OPTICAL_SHAPE",
    "KOTTLER_LAMBDA_ADDS_STATIC_BOUNDARY_NORMALIZATION",
    "HISTORICAL_WORLDLINE_FORMULATION",
    "SUPERSEDED_AS_CORE",
)


class KaluzaKleinReformulationLedgerTests(unittest.TestCase):
    def test_ratified_spec_preserves_global_guardrails(self):
        text = SPEC.read_text()
        self.assertIn("RATIFIED_FOR_IMPLEMENTATION_PLANNING", text)
        for token in STATUSES:
            self.assertIn(token, text)

    def test_complete_change_ledger_exists_and_preserves_history(self):
        text = LEDGER.read_text()
        for heading in (
            "Frozen prior core",
            "Retained results",
            "Changed authority",
            "Deferred routes",
            "Unresolved physical dependencies",
            "No structural dead end",
            "Rollback",
        ):
            self.assertIn(heading, text)
        for token in STATUSES + PRESERVED:
            self.assertIn(token, text)

    def test_public_authority_marks_candidate_unratified(self):
        for path in AUTHORITY:
            text = path.read_text()
            for token in STATUSES:
                self.assertIn(token, text, str(path))
            self.assertIn("REFORMULATION_CANDIDATE_UNRATIFIED", text)
            self.assertIn("DO NOT MERGE WITHOUT HUMAN SCIENTIFIC RATIFICATION", text)


if __name__ == "__main__":
    unittest.main()
