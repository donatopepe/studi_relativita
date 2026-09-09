import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
EN = ROOT / "audit/kerr-photon-ring-orientation-scale-report-en.md"
IT = ROOT / "audit/kerr-photon-ring-orientation-scale-report-it.md"
THEORY = ROOT / "theory/spacetime/kerr-photon-ring-orientation-scale.md"
ROADMAP = ROOT / "docs/roadmap.md"
LEDGER = ROOT / "audit/kaluza-klein-reformulation-change-ledger.md"
ARTIFACT = ROOT / "studies/spacetime/kerr-photon-ring-orientation-scale-results.json"

RESULT = "KERR_FRAME_DRAGGING_ADDS_PROGRADE_RETROGRADE_DIMENSIONLESS_ORBIT_SHAPE_BUT_JOINT_MA_DILATION_RETAINS_ABSOLUTE_SCALE_BLINDNESS_NOT_ELL0"
GATE = "PHYSICAL_KERR_SOURCE_ABSORBER_ENDPOINT_TETRAD_SCREEN_TRANSPORT_AFFINE_FREQUENCY_CLOCK_RECEIVER_NOISE_JOINT_COVARIANCE_DATA_AND_ELL0_LAW_NOT_DERIVED"


class KerrPhotonRingReportTests(unittest.TestCase):
    def test_bilingual_reports_share_authoritative_status(self):
        for text in (EN.read_text(), IT.read_text()):
            for token in (
                RESULT, GATE, "8/8", "DIRECT_REVIEW_NO_SUBAGENT",
                "MODEL=KERR_EQUATORIAL_PHOTON_RING_4D_CONTROL",
                "UMCH=UNPROVEN_SECONDARY_CANDIDATE", "L_identified=false",
                "ell0_identified=false", "L_equals_ell0=NOT_DERIVED",
                "extra_dimension_detected=false", "structural_dead_end=NOT_DECLARED",
                "NO_POSITIVE_DETECTION_CLAIM", "MODEL_LEVEL_KERR_ORBIT_CONFORMANCE_NOT_EVIDENCE",
            ):
                self.assertIn(token, text)

    def test_reports_match_deterministic_anchor(self):
        artifact = json.loads(ARTIFACT.read_text())
        self.assertEqual(artifact["control_summary"]["controls_passed"], 8)
        for text in (EN.read_text(), IT.read_text()):
            for token in (
                "chi=0.6", "x_pro=2.188914", "x_retro=3.6298497",
                "xi_pro/M=3.8384937", "xi_retro/M=-6.3156493",
                "Omega_pro*M=0.26051886", "Omega_retro*M=-0.15833685",
                "branch_minimum_gap=0.46362086", "radial_residual=0.0",
                "dimensionless_scale_residual=0.0", "rank=1",
                "scale_null_direction=[1.0,0.0]",
            ):
                self.assertIn(token, text)

    def test_theory_note_preserves_coordinate_and_source_limits(self):
        text = THEORY.read_text()
        for token in (
            "Teo2003SphericalPhotonOrbits", "R=0", "dR/dr=0",
            "Boyer-Lindquist coordinate period", "not a physical clock",
            "SIMULTANEOUS_SPIN_ORIENTATION_REVERSAL_IS_CONVENTION_COLLISION_NOT_ELL0",
            "JOINT_MA_GEOMETRIC_DILATION_NOT_INTERIOR_SCALE", RESULT, GATE,
        ):
            self.assertIn(token, text)

    def test_roadmap_and_ledger_preserve_5d_and_prior_results(self):
        for text in (ROADMAP.read_text(), LEDGER.read_text()):
            for token in (
                RESULT, GATE, "8/8", "4D_COMPARISON_BASELINE",
                "DECLARED_STATIC_5D_DUST_METRIC_RECOVERS_SCALAR_HESSIAN_AS_R0I0J",
                "FINITE_S1_SOURCE_PROBE_LOCALIZATION_SUPPRESSES_KK_TIDAL_SHAPE", "F_0",
                "L_identified=false", "ell0_identified=false", "L_equals_ell0=NOT_DERIVED",
                "extra_dimension_detected=false", "NO_POSITIVE_DETECTION_CLAIM",
            ):
                self.assertIn(token, text)


if __name__ == "__main__":
    unittest.main()
