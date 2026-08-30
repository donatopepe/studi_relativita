import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
EN = ROOT / "audit/schwarzschild-photon-sphere-riemann-conformance-report-en.md"
IT = ROOT / "audit/schwarzschild-photon-sphere-riemann-conformance-report-it.md"
THEORY = ROOT / "theory/spacetime/schwarzschild-photon-sphere-riemann-conformance.md"
STATUS = "SCHWARZSCHILD_PHOTON_SPHERE_FULL_RIEMANN_CONFIRMS_LEGACY_PROFILE_AFTER_SCREEN_ORDER_AND_AFFINE_NORMALIZATION_NOT_ELL0"
GATE = "PHYSICAL_SOURCE_OBSERVER_SCREEN_PREPARATION_ABSOLUTE_AFFINE_FREQUENCY_STANDARD_CAUSTIC_CONTINUATION_VECTOR_READOUT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED"


class SchwarzschildPhotonSphereRiemannConformanceReportTests(unittest.TestCase):
    def test_bilingual_reports_preserve_same_authoritative_labels(self):
        for path in (EN, IT):
            text = path.read_text()
            for token in (STATUS, GATE, "FALSIFIED_UNCONVERTED_AFFINE_NORMALIZATION_COMPARISON", "DIRECT_REVIEW_NO_SUBAGENT", "UMCH", "UNPROVEN", "NO_POSITIVE_DETECTION_CLAIM"):
                self.assertIn(token, text)
            self.assertIn("diag(-1,+1)/(9M^2)", text)
            self.assertIn("diag(-1,+1)/(3M^2)", text)
            self.assertIn("sqrt(3)", text)
            self.assertIn("1.962615573354719e-17", text)

    def test_theory_preserves_raw_object_and_negative_scope(self):
        text = THEORY.read_text()
        for token in (STATUS, GATE, "FULL_SCREEN_PHASE_MAP_REMAINS_PRIMARY", "ell0_identified=false", "structural_dead_end=NOT_DECLARED", "CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE"):
            self.assertIn(token, text)
        self.assertIn("not falsified", text.lower())
        self.assertIn("affine", text.lower())


if __name__ == "__main__":
    unittest.main()
