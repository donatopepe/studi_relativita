import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
FILES = [
    "theory/spacetime/plane-wave-joint-quotient.md",
    "audit/plane-wave-joint-quotient-report-en.md",
    "audit/plane-wave-joint-quotient-report-it.md",
]
STATUS = "EXACT_PLANE_WAVE_JOINT_QUOTIENT_REVERSAL_AND_AFFINE_SCALE_NONIDENTIFIABLE_NOT_ELL0"
CLASSIFICATION = "EXACT_SPACETIME_CROSS_CHANNEL_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT"


class PlaneWaveJointQuotientReportTests(unittest.TestCase):
    def test_authoritative_statuses_match(self):
        for relative in FILES:
            text = (ROOT / relative).read_text()
            self.assertIn(STATUS, text)
            self.assertIn(CLASSIFICATION, text)
            self.assertIn("NO_POSITIVE_DETECTION_CLAIM", text)

    def test_bilingual_reports_preserve_anchor_and_raw_scope(self):
        english = (ROOT / FILES[1]).read_text()
        italian = (ROOT / FILES[2]).read_text()
        self.assertIn("COMMON_ENDPOINT_ANCHOR_REMAINS_OPEN", english)
        self.assertIn("COMMON_ENDPOINT_ANCHOR_REMAINS_OPEN", italian)
        self.assertIn("raw B", english)
        self.assertIn("raw B", italian)
        self.assertIn("not a structural dead end", english)
        self.assertIn("non è un vicolo cieco strutturale", italian)


if __name__ == "__main__":
    unittest.main()
