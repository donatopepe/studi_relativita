import importlib.util
import json
import pathlib
import subprocess
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PROGRAM = ROOT / "studies/spacetime/plane_wave_canonical_reduction.py"
ARTIFACT = ROOT / "studies/spacetime/plane-wave-canonical-reduction-results.json"


def load_module():
    spec = importlib.util.spec_from_file_location("plane_wave_canonical_reduction", PROGRAM)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PlaneWaveCanonicalReductionTests(unittest.TestCase):
    def setUp(self):
        self.module = load_module()

    def test_two_profile_maps_and_calibration_are_symplectic(self):
        result = self.module.symplectic_family_control(6000)
        for key in ("first_map_residual", "second_map_residual", "observer_calibration_residual"):
            self.assertLess(result[key], 3e-12, key)

    def test_independent_endpoint_action_maps_first_profile_to_second(self):
        result = self.module.transitive_collision_control(6000)
        self.assertLess(result["collision_residual"], 3e-12)
        self.assertEqual(result["source_calibration"], "IDENTITY")
        self.assertGreater(result["raw_map_difference"], 1e-3)

    def test_common_conjugation_cannot_create_same_collision(self):
        result = self.module.common_conjugation_obstruction_control(6000)
        self.assertGreater(result["trace_difference"], 1e-4)
        self.assertEqual(result["gate"], "DISTINCT_TRACE_FORBIDS_COMMON_CONJUGATION_COLLISION")

    def test_endpoint_group_choice_changes_identifiability(self):
        result = self.module.group_comparison_control(6000)
        self.assertEqual(result["independent_endpoint_action"], "TRANSITIVE_ON_SYMPLECTIC_PROPAGATORS")
        self.assertEqual(result["common_endpoint_action"], "CONJUGACY_INVARIANTS_REMAIN")
        self.assertEqual(result["lower_shear_action"], "B_BLOCK_REMAINS_INVARIANT")

    def test_affine_scale_and_ell0_remain_unidentified(self):
        result = self.module.affine_rescaling_control(6000)
        self.assertLess(result["dimensionless_full_map_residual"], 5e-11)
        self.assertEqual(
            self.module.ell0_gate(["P1", "P2", "Gs", "Go", "L"]),
            "FULL_MAP_CANONICAL_ENDPOINT_QUOTIENT_AFFINE_SCALE_NOT_ELL0",
        )

    def test_artifact_is_deterministic_and_scoped(self):
        subprocess.run(["python3", str(PROGRAM), "--check"], check=True)
        data = json.loads(ARTIFACT.read_text())
        self.assertEqual(data["status"], "EXACT_PLANE_WAVE_FULL_MAP_TRANSITIVE_UNDER_INDEPENDENT_CANONICAL_ENDPOINT_CALIBRATION_NOT_ELL0")
        self.assertEqual(data["open_gate"], "PHYSICAL_CANONICAL_ENDPOINT_CALIBRATION_GROUP_NOT_DERIVED")
        self.assertEqual(data["conclusion"], "NO_POSITIVE_DETECTION_CLAIM")
        self.assertFalse(data["structural_dead_end"])


if __name__ == "__main__":
    unittest.main()
