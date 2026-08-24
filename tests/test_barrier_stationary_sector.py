import importlib.util
import json
import math
import pathlib
import subprocess
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
STUDY = ROOT / "studies" / "classical-dynamics"
TOOL = STUDY / "barrier_stationary_check.py"
INPUT = STUDY / "barrier-stationary-cases.json"
OUTPUT = STUDY / "barrier-stationary-results.json"


def module():
    spec = importlib.util.spec_from_file_location("stationary", TOOL)
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


class BarrierStationarySectorTests(unittest.TestCase):
    def test_unique_physical_root_for_positive_epsilon(self):
        stationary = module()
        for epsilon in [0.01, 0.1, 0.5, 1.0, 10.0]:
            roots = stationary.constant_curvature_roots(epsilon)
            self.assertEqual(1, len(roots["physical"]))
            z = roots["physical"][0]
            self.assertGreater(z, 1.0)
            self.assertAlmostEqual(0.0, stationary.stationary_equation(z, epsilon), places=10)
            self.assertLessEqual(roots["discarded"][0], 1.0)

    def test_closed_form_root(self):
        stationary = module()
        epsilon = 0.5
        expected = 1 + epsilon + math.sqrt(epsilon * epsilon + epsilon)
        self.assertAlmostEqual(expected, stationary.physical_root(epsilon))

    def test_planar_linearization_has_exponential_modes(self):
        stationary = module()
        z = stationary.physical_root(0.5)
        result = stationary.planar_linearization(z, kappa0=2.0)
        self.assertEqual("DELTA_Z_DOUBLE_PRIME_MINUS_OMEGA2_DELTA_Z_EQUALS_ZERO", result["equation"])
        self.assertAlmostEqual((2.0 * z) ** 2, result["omega_squared"])
        self.assertGreater(result["growth_rate_per_length"], 0)
        self.assertEqual("LOCALLY_HYPERBOLIC_REDUCED_PLANAR_MODE", result["classification"])
        self.assertFalse(result["full_phase_space_stability_claim"])

    def test_output_preregisters_scope_and_sources(self):
        run = subprocess.run(["python3", str(TOOL), "--check"], cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(0, run.returncode, run.stderr or run.stdout)
        result = json.loads(OUTPUT.read_text(encoding="utf-8"))
        self.assertEqual(["ACG2001-E45", "ACG2001-E46"], result["source_formula_ids"])
        self.assertEqual("PLANAR_CONSTANT_CURVATURE_ONLY", result["scope"])
        self.assertIn("does not establish full constrained stability", result["warning"])
        self.assertTrue(all(case["local_reduced_mode"]["classification"] == "LOCALLY_HYPERBOLIC_REDUCED_PLANAR_MODE" for case in result["cases"]))


if __name__ == "__main__":
    unittest.main()
