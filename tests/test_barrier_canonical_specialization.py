import importlib.util
import json
import math
import pathlib
import subprocess
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
STUDY = ROOT / "studies" / "classical-dynamics"
TOOL = STUDY / "barrier_canonical_check.py"
INPUT = STUDY / "barrier-canonical-cases.json"
OUTPUT = STUDY / "barrier-canonical-results.json"


def module():
    spec = importlib.util.spec_from_file_location("canonical", TOOL)
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


class BarrierCanonicalSpecializationTests(unittest.TestCase):
    def test_dimensionless_lagrangian_derivatives(self):
        canonical = module()
        epsilon = 0.5
        self.assertAlmostEqual(-0.5, canonical.ell(2.0, epsilon))
        self.assertAlmostEqual(-0.5, canonical.ell_z(2.0, epsilon))
        self.assertAlmostEqual(1.0, canonical.ell_zz(2.0, epsilon))
        self.assertLess(canonical.ell_z(3.0, epsilon), 0)
        self.assertGreater(canonical.ell_zz(3.0, epsilon), 0)

    def test_legendre_map_is_strictly_monotone_on_domain(self):
        canonical = module()
        for z in [1.01, 1.1, 2.0, 10.0]:
            self.assertGreater(canonical.ell_zz(z, 0.2), 0)
        for p in [-2000.0, -2.0, -0.02]:
            z = canonical.inverse_momentum(p, 0.2)
            self.assertGreater(z, 1.0)
            self.assertAlmostEqual(p, canonical.ell_z(z, 0.2))
        with self.assertRaises(ValueError):
            canonical.inverse_momentum(0.0, 0.2)

    def test_hessian_eigenvalue_factors_are_nonzero_except_tangent(self):
        canonical = module()
        factors = canonical.hessian_factors(2.0, 0.5)
        self.assertNotEqual(0.0, factors["radial"])
        self.assertNotEqual(0.0, factors["transverse_normal"])
        self.assertEqual(0.0, factors["tangent"])
        self.assertEqual("ONE_TANGENT_NULL_DIRECTION", factors["classification"])

    def test_legendre_potential_specialization(self):
        canonical = module()
        # dimensionless v=z*l_z-l = 1 - eps*(2z-1)/(z-1)^2
        self.assertAlmostEqual(1.0 - 0.5 * 3.0, canonical.legendre_potential(2.0, 0.5))

    def test_output_is_deterministic_and_records_source_ids(self):
        run = subprocess.run(["python3", str(TOOL), "--check"], cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(0, run.returncode, run.stderr or run.stdout)
        result = json.loads(OUTPUT.read_text(encoding="utf-8"))
        self.assertEqual("paper-ii-b-canonical-specialization-v1", result["study_id"])
        self.assertEqual(["CGR2002-E19", "CGR2002-E26", "CGR2002-E29"], result["source_formula_ids"])
        self.assertEqual("GENERIC_LKK_NONZERO", result["legendre_sector"])
        self.assertIn("does not prove", result["warning"])


if __name__ == "__main__":
    unittest.main()
