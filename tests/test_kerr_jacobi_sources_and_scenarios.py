import json
import pathlib
import subprocess
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
BIB = ROOT / "references/library.bib"
LOG = ROOT / "references/verification-log.md"
MANIFEST = ROOT / "studies/spacetime/kerr-jacobi-scenarios.json"
RUNNER = ROOT / "tools/run_kerr_jacobi_scenarios.py"


class KerrJacobiSourcesAndScenarios(unittest.TestCase):
    def test_boero_moreschi_source_is_narrowly_registered(self):
        bib, log = BIB.read_text(), LOG.read_text()
        self.assertIn("@article{BoeroMoreschi2020KerrOpticalScalars", bib)
        self.assertIn("10.1093/mnras/stz3615", bib)
        self.assertIn("1910.01984", bib)
        section = log.split("## BoeroMoreschi2020KerrOpticalScalars", 1)[1]
        for token in ("equations (1)-(12)", "equations (106)-(127)", "equation (119)", "equation (126)", "exact Kerr", "geodesic deviation", "does not establish this project's scenario matrix", "5D Kerr comparator", "ell0", "detection"):
            self.assertIn(token, section)

    def test_manifest_covers_all_preregistered_scenarios_and_categories(self):
        data = json.loads(MANIFEST.read_text())
        self.assertEqual([item["id"] for item in data["scenarios"]], ["J01", "J02", "J03", "J04", "J05", "J06"])
        self.assertEqual(set(item["category"] for item in data["scenarios"]), {"conformance", "orientation", "scale"})
        self.assertEqual(len(data["scenarios"]), len(set(item["id"] for item in data["scenarios"])))

    def test_runner_supports_total_granular_category_and_json_report(self):
        with tempfile.TemporaryDirectory() as directory:
            report = pathlib.Path(directory) / "report.json"
            total = subprocess.run(["python", str(RUNNER), "--mode", "total", "--report-json", str(report)], text=True, capture_output=True)
            self.assertEqual(total.returncode, 0, total.stdout + total.stderr)
            payload = json.loads(report.read_text())
            self.assertEqual(payload["summary"], {"PASS": 6, "FAIL": 0, "SKIP": 0, "BLOCKED": 0})
            granular = subprocess.run(["python", str(RUNNER), "--mode", "granular", "--scenario", "J01"], text=True, capture_output=True)
            self.assertEqual(granular.returncode, 0, granular.stdout + granular.stderr)
            self.assertEqual(len(json.loads(granular.stdout)["results"]), 1)
            category = subprocess.run(["python", str(RUNNER), "--mode", "granular", "--category", "orientation"], text=True, capture_output=True)
            self.assertEqual(category.returncode, 0, category.stdout + category.stderr)
            self.assertTrue(all(item["category"] == "orientation" for item in json.loads(category.stdout)["results"]))


if __name__ == "__main__":
    unittest.main()
