#!/usr/bin/env python3
"""Canonical versus coordinate-velocity phase maps in a rotating screen."""
import argparse, importlib.util, json, math, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
OUTPUT = HERE / "plane-wave-canonical-screen-phase-results.json"

def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module); return module

cov = load("plane_wave_covariant_for_canonical", "plane_wave_covariant_screen_phase.py")
screen, base, full, spectrum = cov.screen, cov.base, cov.full, cov.spectrum
J = cov.J

def transpose(a): return cov.transpose(a)
def matrix_residual(a, b): return cov.matrix_residual(a, b)
def characteristic_residual(a, b): return cov.vector_residual(spectrum.characteristic_coefficients(a), spectrum.characteristic_coefficients(b))
def diagonal_phase(q): return full.assemble(q, base.zero(), base.zero(), q)
def h_velocity_to_canonical(a): return full.assemble(base.eye(), base.zero(), a, base.eye())
def symplectic_form(): return full.assemble(base.zero(), base.eye(), base.scale(base.eye(), -1.0), base.zero())

def canonical_generator(u, kfun=base.base_k, qfun=screen.transport, afun=cov.connection_a):
    q, a = qfun(u), afun(u)
    kt = base.mm(base.mm(transpose(q), kfun(u)), q)
    return full.assemble(base.scale(a, -1.0), base.eye(), base.scale(kt, -1.0), base.scale(a, -1.0))

def canonical_map(length=0.94, n=5000, kfun=base.base_k, qfun=screen.transport, afun=cov.connection_a):
    step, u, p = length / n, -length / 2.0, cov.identity4()
    gfun = lambda x: canonical_generator(x, kfun, qfun, afun)
    for _ in range(n): p, u = cov.rk4_matrix(u, p, step, gfun), u + step
    return p

def canonical_graph_map(length=0.94, n=5000, kfun=base.base_k, qfun=screen.transport):
    source, observer = -length / 2.0, length / 2.0
    cs, co = diagonal_phase(qfun(source)), diagonal_phase(qfun(observer))
    inertial = full.full_map(kfun, length, n)
    return base.mm(base.mm(cov.inverse4(co), inertial), cs)

def velocity_from_canonical(canonical, a_source, a_observer):
    return base.mm(base.mm(cov.inverse4(h_velocity_to_canonical(a_observer)), canonical), h_velocity_to_canonical(a_source))

def zero_connection_control(length=0.94, n=5000):
    qfun, afun, aprime = lambda u: base.eye(), lambda u: base.zero(), lambda u: base.zero()
    canonical = canonical_map(length, n, qfun=qfun, afun=afun)
    velocity = cov.covariant_map(length, n, qfun=qfun, afun=afun, aprimefun=aprime)
    inertial = full.full_map(base.base_k, length, n)
    return {"velocity_canonical_residual": matrix_residual(velocity, canonical), "canonical_inertial_residual": matrix_residual(canonical, inertial)}

def canonical_equivalence_control(length=0.94, n=5000):
    source, observer = -length / 2.0, length / 2.0
    direct, endpoint, velocity = canonical_map(length, n), canonical_graph_map(length, n), cov.covariant_map(length, n)
    converted = base.mm(base.mm(h_velocity_to_canonical(cov.connection_a(observer)), velocity), cov.inverse4(h_velocity_to_canonical(cov.connection_a(source))))
    return {"direct_endpoint_residual": matrix_residual(direct, endpoint), "velocity_conversion_residual": matrix_residual(direct, converted), "direct_canonical_map": direct, "endpoint_canonical_map": endpoint}

def symplectic_residual(p, omega_source, omega_observer):
    return matrix_residual(base.mm(base.mm(transpose(p), omega_observer), p), omega_source)

def symplectic_structure_control(length=0.94, n=5000):
    source, observer = -length / 2.0, length / 2.0
    canonical, velocity, omega = canonical_map(length, n), cov.covariant_map(length, n), symplectic_form()
    hs, ho = h_velocity_to_canonical(cov.connection_a(source)), h_velocity_to_canonical(cov.connection_a(observer))
    pulled_source = base.mm(base.mm(transpose(hs), omega), hs)
    pulled_observer = base.mm(base.mm(transpose(ho), omega), ho)
    return {"canonical_standard_residual": symplectic_residual(canonical, omega, omega), "velocity_standard_residual": symplectic_residual(velocity, omega, omega), "velocity_pulled_back_residual": symplectic_residual(velocity, pulled_source, pulled_observer), "source_pulled_form": pulled_source, "observer_pulled_form": pulled_observer}

def spectral_counterexample(length=0.94, n=5000):
    canonical, velocity = canonical_map(length, n), cov.covariant_map(length, n)
    return {"canonical_characteristic": spectrum.characteristic_coefficients(canonical), "velocity_characteristic": spectrum.characteristic_coefficients(velocity), "characteristic_difference": characteristic_residual(canonical, velocity), "disposition": "VELOCITY_CHARACTERISTIC_NOT_CANONICAL_SCREEN_INVARIANT"}

def endpoint_calibration_mobility_control(length=0.94, n=5000):
    source, observer = -length / 2.0, length / 2.0
    canonical = canonical_graph_map(length, n)
    a_s, a_o = cov.connection_a(source), cov.connection_a(observer)
    velocity = velocity_from_canonical(canonical, a_s, a_o)
    alt_s, alt_o = base.add(a_s, base.scale(J, -0.19)), base.add(a_o, base.scale(J, 0.27))
    velocity_alt = velocity_from_canonical(canonical, alt_s, alt_o)
    return {"canonical_map_difference": matrix_residual(canonical, canonical), "velocity_map_difference": matrix_residual(velocity, velocity_alt), "velocity_characteristic_difference": characteristic_residual(velocity, velocity_alt), "scope": "ENDPOINT_PHASE_VARIABLE_CALIBRATION_COUNTEREXAMPLE_NOT_ALTERNATE_CONNECTION_SOLUTION"}

def common_basis_control(length=0.94, n=5000, angle=0.39):
    first, r = canonical_map(length, n), screen.rotation(angle)
    qfun = lambda u: base.mm(screen.transport(u), r)
    afun = lambda u: base.mm(base.mm(transpose(r), cov.connection_a(u)), r)
    second, c = canonical_map(length, n, qfun=qfun, afun=afun), diagonal_phase(r)
    predicted = base.mm(base.mm(cov.inverse4(c), first), c)
    return {"map_similarity_residual": matrix_residual(second, predicted), "characteristic_residual": characteristic_residual(second, first)}

def affine_orbit_control(length=0.94, n=5000, scale_factor=1.47):
    first = canonical_map(length, n)
    kfun, qfun, afun, _ = cov.scaled_functions(scale_factor)
    second = canonical_map(scale_factor * length, n, kfun, qfun, afun)
    d = spectrum.diagonal4(1.0 / math.sqrt(scale_factor), math.sqrt(scale_factor))
    predicted = base.mm(base.mm(cov.inverse4(d), first), d)
    return {"scale_factor": scale_factor, "map_scaling_residual": matrix_residual(second, predicted), "characteristic_residual": characteristic_residual(second, first)}

def ell0_gate(raw_fields): return "CANONICAL_SCREEN_PHASE_AFFINE_ORBIT_NOT_ELL0" if "ell0" not in raw_fields else "REQUIRES_INJECTIVITY_TEST"
def build_artifact(n=5000):
    raw = ["K","omega","Q","A","x","x_prime","p","P_inertial","P_velocity","P_canonical","H_source","H_observer","L"]
    return {"classification":"EXACT_SPACETIME_CANONICAL_SCREEN_PHASE_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT","status":"EXACT_PLANE_WAVE_ROTATING_SCREEN_VELOCITY_SPECTRUM_ENDPOINT_CALIBRATION_DEPENDENT_CANONICAL_MAP_AFFINE_SCALE_BLIND_NOT_ELL0","open_gate":"PHYSICAL_SCREEN_CANONICAL_MOMENTUM_ENDPOINT_ANGULAR_VELOCITY_AND_UNIT_CALIBRATION_NOT_DERIVED","raw_fields":raw,"zero_connection":zero_connection_control(n=n),"canonical_equivalence":canonical_equivalence_control(n=n),"symplectic_structure":symplectic_structure_control(n=n),"spectral_counterexample":spectral_counterexample(n=n),"endpoint_calibration_mobility":endpoint_calibration_mobility_control(n=n),"common_basis":common_basis_control(n=n),"affine_orbit":affine_orbit_control(n=n),"ell0_gate":ell0_gate(raw),"correction_disposition":"PR77_VELOCITY_MAP_RETAINED_ORDINARY_CHARACTERISTIC_RELABELED_COORDINATE_DIAGNOSTIC_CANONICAL_MAP_ADDED","source_scope":"COLEY_MCNUTT_MILSON_2012_SUPPORTS_EXACT_BRINKMANN_PLANE_WAVES_AND_GEODESIC_DEVIATION_NOT_ROTATING_DETECTOR_CANONICAL_VARIABLES_ENDPOINT_CALIBRATION_WINDOW_AFFINE_NUISANCE_ELL0_UMCH_OR_DETECTION","structural_dead_end":False,"hypothesis_status":"UNPROVEN","conclusion":"NO_POSITIVE_DETECTION_CLAIM"}
def render(data): return json.dumps(data, indent=2, sort_keys=True)+"\n"
def main(argv=None):
    parser=argparse.ArgumentParser(); parser.add_argument("--check",action="store_true"); args=parser.parse_args(argv); text=render(build_artifact())
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text()!=text: print(f"stale artifact: {OUTPUT}",file=sys.stderr); return 1
        return 0
    OUTPUT.write_text(text); return 0
if __name__=="__main__": raise SystemExit(main())
