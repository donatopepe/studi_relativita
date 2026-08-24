import importlib.util
import json
import pathlib
import subprocess
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
STUDY = ROOT / "studies" / "classical-dynamics"
TOOL = STUDY / "barrier_gate_check.py"
INPUT = STUDY / "barrier-gate-cases.json"
OUTPUT = STUDY / "barrier-gate-results.json"
DOC = ROOT / "theory" / "classical-dynamics" / "candidate-b-gate-decision.md"


def module():
    spec = importlib.util.spec_from_file_location("gate", TOOL)
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


class BarrierGateDecisionTests(unittest.TestCase):
    def test_multipath_limits_are_distinct(self):
        gate = module()
        fixed = gate.limit_path("fixed-curvature", epsilon=0.5, ratio=2.0)
        boundary = gate.limit_path("stationary-root", epsilon=0.5, ratio=2.0)
        geodesic = gate.limit_path("geodesic", epsilon=0.5, ratio=2.0)
        self.assertEqual("FREE_LAGRANGIAN_DENSITY_POINTWISE", fixed["classification"])
        self.assertEqual("CURVATURE_COLLAPSES_BUT_BARRIER_REMAINS_FINITE", boundary["classification"])
        self.assertEqual("OUTSIDE_DOMAIN_FOR_ALL_POSITIVE_KAPPA0", geodesic["classification"])

    def test_stationary_growth_scale_vanishes_but_mode_remains_hyperbolic(self):
        gate = module()
        result = gate.stationary_limit(epsilon=0.5, kappa0=1e-6)
        self.assertGreater(result["z_star"], 1)
        self.assertGreater(result["growth_rate"], 0)
        self.assertAlmostEqual(result["growth_rate"], result["kappa_star"])
        self.assertEqual("TIMESCALE_DIVERGES_AS_KAPPA0_TO_ZERO", result["classification"])

    def test_gate_is_blocked_by_failed_required_checks(self):
        run = subprocess.run(["python3", str(TOOL), "--check"], cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(0, run.returncode, run.stderr or run.stdout)
        result = json.loads(OUTPUT.read_text(encoding="utf-8"))
        self.assertEqual("BLOCKED", result["paper_iii_gate"])
        self.assertEqual("CONTRADICTED_UNDER_ASSUMPTIONS", result["candidate_b_state"])
        self.assertIn("reduced_planar_local_stability", result["failed_required_checks"])
        self.assertIn("standard_limit_full_solution_space", result["failed_required_checks"])
        self.assertIn("observable_mapping", result["failed_required_checks"])
        self.assertFalse(result["full_phase_space_instability_proven"])
        self.assertFalse(result["bounded_energy_resolved"])

    def test_decision_document_states_conditional_scope(self):
        text = DOC.read_text(encoding="utf-8")
        for phrase in ["BLOCKED", "CONTRADICTED_UNDER_ASSUMPTIONS", "local planar", "not a full", "nonuniform", "observable", "UNPROVEN"]:
            self.assertIn(phrase, text)
        self.assertNotIn("UMCH is disproved", text)


if __name__ == "__main__":
    unittest.main()
