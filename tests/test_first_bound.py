import importlib.util
import json
import pathlib
import subprocess
import tempfile
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
STUDY = ROOT / "studies" / "free-fall-identifiability"
ANALYSIS = STUDY / "analysis.py"
INPUTS = STUDY / "inputs.json"
RESULTS = STUDY / "results.json"


def load_analysis():
    spec = importlib.util.spec_from_file_location("bound_analysis", ANALYSIS)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class FirstBoundStudyTests(unittest.TestCase):
    def test_synthetic_direct_acceleration_mapping_has_correct_units(self):
        module = load_analysis()
        result = module.evaluate({
            "study_id": "synthetic",
            "observable": "proper_acceleration_upper_bound",
            "observable_value": 1.0,
            "observable_unit": "m s^-2",
            "confidence_level": 0.95,
            "mapping": "direct_timelike_curvature",
            "speed_of_light_m_s": 299792458.0,
            "sources": [{"citation_key": "TiesingaEtAl2021", "canonical_url": "https://doi.org/10.1103/RevModPhys.93.025010"}],
        })
        self.assertEqual("BOUND_DERIVABLE_UNDER_DECLARED_MAPPING", result["status"])
        self.assertEqual("m^-1", result["kappa0_upper_bound_unit"])
        self.assertAlmostEqual(1.0 / 299792458.0**2, result["kappa0_upper_bound_value"], places=32)
        self.assertEqual(0.95, result["confidence_level"])

    def test_real_study_reports_no_bound_without_observable_mapping(self):
        module = load_analysis()
        data = json.loads(INPUTS.read_text(encoding="utf-8"))
        result = module.evaluate(data)
        self.assertEqual("NO_BOUND_DERIVABLE", result["status"])
        self.assertIsNone(result["kappa0_upper_bound_value"])
        self.assertIn("mapping", result["blocking_reason"].lower())
        self.assertFalse(result["positive_detection"])

    def test_inputs_have_source_metadata_and_uncertainty_semantics(self):
        data = json.loads(INPUTS.read_text(encoding="utf-8"))
        self.assertEqual("not_applicable_without_mapping", data["uncertainty_model"])
        self.assertGreaterEqual(len(data["sources"]), 2)
        for source in data["sources"]:
            self.assertTrue(source["citation_key"])
            self.assertRegex(source["canonical_url"], r"^https://")
            self.assertEqual("2026-08-21", source["access_date"])

    def test_committed_result_is_deterministic(self):
        run = subprocess.run(["python3", str(ANALYSIS), "--check"], cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(0, run.returncode, run.stderr or run.stdout)
        result = json.loads(RESULTS.read_text(encoding="utf-8"))
        self.assertEqual("free-fall-identifiability-v1", result["study_id"])
        self.assertEqual("NO_BOUND_DERIVABLE", result["status"])

    def test_bilingual_reports_state_same_result(self):
        italian = (STUDY / "report-it.md").read_text(encoding="utf-8")
        english = (STUDY / "report-en.md").read_text(encoding="utf-8")
        for text in (italian, english):
            self.assertIn("NO_BOUND_DERIVABLE", text)
            self.assertIn("κ₀", text)
            self.assertRegex(text, r"a/(?:c²|c\^2)")


if __name__ == "__main__":
    unittest.main()
