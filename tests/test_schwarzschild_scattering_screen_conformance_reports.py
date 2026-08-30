import importlib.util
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
MODULE = ROOT / "studies/spacetime/schwarzschild_scattering_screen_conformance.py"
SPEC = importlib.util.spec_from_file_location("screen_conformance_reports", MODULE)
ssc = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ssc)
STATUS = "SCHWARZSCHILD_SCATTERING_SCREEN_IS_PARALLEL_MODULO_NULL_GAUGE_BUT_FULL_RIEMANN_RECONSTRUCTION_FALSIFIES_PRIOR_OPTICAL_PROFILE_AND_REQUIRES_CORRECTED_PHASE_MAP_NOT_ELL0"
GATE = "PHYSICAL_SCATTERING_SOURCE_PROFILE_EMITTER_ABSORBER_TETRADS_ABSOLUTE_FREQUENCY_STANDARD_SCREEN_PREPARATION_CAUSTIC_CONTINUATION_VECTOR_READOUT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED"
FILES = [
    ROOT / "theory/spacetime/schwarzschild-scattering-screen-conformance.md",
    ROOT / "audit/schwarzschild-scattering-screen-conformance-report-en.md",
    ROOT / "audit/schwarzschild-scattering-screen-conformance-report-it.md",
]


class SchwarzschildScatteringScreenConformanceReportTests(unittest.TestCase):
    def test_artifact_is_deterministic_and_preserves_negative_status(self):
        artifact = ROOT / "studies/spacetime/schwarzschild-scattering-screen-conformance-results.json"
        self.assertEqual(artifact.read_text(), ssc.render())
        data = json.loads(artifact.read_text())
        self.assertEqual(data["status"], STATUS)
        self.assertEqual(data["gate"], GATE)
        self.assertEqual(data["prior_profile_status"], "FALSIFIED_BY_INDEPENDENT_FOUR_DIMENSIONAL_RIEMANN_RECONSTRUCTION")
        self.assertFalse(data["ell0_identified"])
        self.assertEqual(data["UMCH"], "UNPROVEN")
        self.assertEqual(data["detection"], "NO_POSITIVE_DETECTION_CLAIM")

    def test_theory_and_bilingual_audits_align(self):
        for path in FILES:
            text = path.read_text()
            self.assertIn(STATUS, text)
            self.assertIn(GATE, text)
            self.assertIn("diag(-1,+1) 3 M b^2/r^5", text)
            self.assertIn("diag(+1,-1) M b^2/r^5", text)
            self.assertIn("DIRECT_REVIEW_NO_SUBAGENT", text)
            self.assertIn("CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE", text)
            self.assertIn("NO_POSITIVE_DETECTION_CLAIM", text)
            self.assertIn("NOT_DECLARED", text)


if __name__ == "__main__":
    unittest.main()
