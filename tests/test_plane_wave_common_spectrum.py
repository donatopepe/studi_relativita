import importlib.util
import json
import pathlib
import subprocess
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PROGRAM = ROOT / "studies/spacetime/plane_wave_common_spectrum.py"
ARTIFACT = ROOT / "studies/spacetime/plane-wave-common-spectrum-results.json"


def load_module():
    spec = importlib.util.spec_from_file_location("plane_wave_common_spectrum", PROGRAM)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PlaneWaveCommonSpectrumTests(unittest.TestCase):
    def setUp(self):
        self.module = load_module()

    def test_characteristic_coefficients_obey_symplectic_constraints(self):
        result = self.module.symplectic_characteristic_control(6000)
        self.assertLess(result["determinant_residual"], 3e-12)
        self.assertLess(result["palindromic_residual"], 3e-12)

    def test_common_canonical_conjugation_preserves_characteristic_polynomial(self):
        result = self.module.common_conjugation_control(6000)
        self.assertLess(result["characteristic_residual"], 3e-12)
        self.assertGreater(result["raw_map_difference"], 1e-3)

    def test_profile_reversal_is_spectrally_blind(self):
        result = self.module.reversal_spectrum_control(6000)
        self.assertLess(result["characteristic_residual"], 3e-11)
        self.assertGreater(result["raw_map_difference"], 1e-3)

    def test_affine_rescaling_is_canonical_similarity(self):
        result = self.module.affine_similarity_control(6000)
        self.assertLess(result["similarity_residual"], 5e-11)
        self.assertLess(result["characteristic_residual"], 5e-11)

    def test_spectrum_retains_profile_but_not_absolute_scale(self):
        result = self.module.profile_sensitivity_control(6000)
        self.assertGreater(result["characteristic_difference"], 1e-3)
        self.assertEqual(result["interpretation"], "PROFILE_GEOMETRY_CONDITIONAL_NOT_ABSOLUTE_SCALE")

    def test_ell0_is_absent_and_artifact_is_deterministic(self):
        self.assertEqual(
            self.module.ell0_gate(["P", "K", "L", "G"]),
            "COMMON_CANONICAL_SPECTRUM_AFFINE_SCALE_NOT_ELL0",
        )
        subprocess.run(["python3", str(PROGRAM), "--check"], check=True)
        data = json.loads(ARTIFACT.read_text())
        self.assertEqual(data["status"], "EXACT_PLANE_WAVE_COMMON_CANONICAL_SPECTRUM_PROFILE_INFORMATIVE_REVERSAL_AND_AFFINE_SCALE_BLIND_NOT_ELL0")
        self.assertEqual(data["open_gate"], "PHYSICAL_COMMON_CANONICAL_STANDARD_AND_ELL0_LAW_NOT_DERIVED")
        self.assertEqual(data["conclusion"], "NO_POSITIVE_DETECTION_CLAIM")
        self.assertFalse(data["structural_dead_end"])


if __name__ == "__main__":
    unittest.main()
