import importlib.util
import json
import pathlib
import subprocess
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
STUDY = ROOT / "studies" / "classical-dynamics"
TOOL = STUDY / "barrier_constraint_check.py"
INPUT = STUDY / "barrier-constraint-cases.json"
OUTPUT = STUDY / "barrier-constraint-results.json"
DOC = ROOT / "theory" / "classical-dynamics" / "candidate-b-canonical.md"


def module():
    spec = importlib.util.spec_from_file_location("constraints", TOOL)
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


class BarrierCanonicalStructureTests(unittest.TestCase):
    def test_specialized_momenta_coefficients(self):
        constraints = module()
        result = constraints.coefficients(z=2.0, epsilon=0.5, kappa0=3.0, mc=7.0, kappa2=0.4, z_prime=0.2)
        self.assertAlmostEqual(-7.0 * 0.5 / (3.0 * 1.0**2), result["L_kappa"])
        self.assertAlmostEqual(-7.0 * (2.0 * 0.5 / 1.0**3) * 0.2 / 3.0, result["minus_Lkappa_prime_eta1_coefficient"])
        self.assertAlmostEqual(result["L_kappa"] * 0.4, result["eta2_coefficient"])
        self.assertAlmostEqual(result["legendre_potential"], result["tangent_coefficient"])

    def test_constraint_count_is_sourced_generic_sector_only(self):
        data = json.loads(OUTPUT.read_text(encoding="utf-8"))
        self.assertEqual("ONE_PRIMARY_PLUS_ONE_SECONDARY", data["constraint_chain"])
        self.assertEqual("TWO_FIRST_CLASS_IN_SOURCE_GENERIC_SECTOR", data["class_status"])
        self.assertEqual("NO_OTHER_CONSTRAINTS_IN_SOURCE_GENERIC_SECTOR", data["closure"])
        self.assertTrue(data["barrier_meets_generic_assumption_Lkk_nonzero"])
        self.assertFalse(data["reduced_hamiltonian_boundedness_derived"])
        self.assertFalse(data["full_stability_derived"])

    def test_output_and_document_have_exact_provenance(self):
        run = subprocess.run(["python3", str(TOOL), "--check"], cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(0, run.returncode, run.stderr or run.stdout)
        data = json.loads(OUTPUT.read_text(encoding="utf-8"))
        self.assertEqual(["CGR2002-E19", "CGR2002-E24", "CGR2002-E25", "CGR2002-E26", "CGR2002-E27", "CGR2002-E28", "CGR2002-E29", "CGR2002-E30", "CGR2002-E31"], data["source_formula_ids"])
        text = DOC.read_text(encoding="utf-8")
        for token in ["CGR2002-E19", "CGR2002-E24", "CGR2002-E25", "CGR2002-E31", "two first-class", "2N", "UNPROVEN", "not prove bounded"]:
            self.assertIn(token, text)


if __name__ == "__main__":
    unittest.main()
