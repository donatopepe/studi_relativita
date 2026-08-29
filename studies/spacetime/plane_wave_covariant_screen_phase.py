#!/usr/bin/env python3
"""Covariant rotating-screen phase maps for an exact Brinkmann plane wave."""
import argparse
import importlib.util
import json
import math
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
OUTPUT = HERE / "plane-wave-covariant-screen-phase-results.json"


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


screen = load("plane_wave_screen_transport_covariant", "plane_wave_screen_transport.py")
base, full, spectrum = screen.base, screen.full, screen.spectrum
J = [[0.0, -1.0], [1.0, 0.0]]


def transpose(a):
    return [list(row) for row in zip(*a)]


def identity4():
    return full.assemble(base.eye(), base.zero(), base.zero(), base.eye())


def inverse2(a):
    determinant = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    return [[a[1][1] / determinant, -a[0][1] / determinant], [-a[1][0] / determinant, a[0][0] / determinant]]


def inverse4(a):
    n = len(a)
    work = [a[i][:] + [1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda row: abs(work[row][col]))
        if abs(work[pivot][col]) < 1e-14:
            raise ValueError("SINGULAR_PHASE_TRANSFORM")
        work[col], work[pivot] = work[pivot], work[col]
        value = work[col][col]
        work[col] = [entry / value for entry in work[col]]
        for row in range(n):
            if row != col:
                factor = work[row][col]
                work[row] = [work[row][j] - factor * work[col][j] for j in range(2 * n)]
    return [row[n:] for row in work]


def matrix_residual(a, b):
    return base.norm(base.add(a, b, -1.0))


def vector_residual(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def omega_prime(u):
    return 0.31 + 0.28 * u


def connection_a(u, omega_fun=screen.omega):
    return base.scale(J, -omega_fun(u))


def connection_a_prime(u, omega_prime_fun=omega_prime):
    return base.scale(J, -omega_prime_fun(u))


def state_map(q, a):
    return full.assemble(q, base.zero(), base.mm(q, a), q)


def generator(u, kfun=base.base_k, qfun=screen.transport, afun=connection_a, aprimefun=connection_a_prime):
    q, a, aprime = qfun(u), afun(u), aprimefun(u)
    kt = base.mm(base.mm(transpose(q), kfun(u)), q)
    potential = base.add(base.add(kt, aprime), base.mm(a, a))
    return full.assemble(base.zero(), base.eye(), base.scale(potential, -1.0), base.scale(a, -2.0))


def rk4_matrix(u, p, step, generator_fun):
    def rhs(x, y):
        return base.mm(generator_fun(x), y)
    k1 = rhs(u, p)
    k2 = rhs(u + step / 2.0, base.add(p, base.scale(k1, step / 2.0)))
    k3 = rhs(u + step / 2.0, base.add(p, base.scale(k2, step / 2.0)))
    k4 = rhs(u + step, base.add(p, base.scale(k3, step)))
    total = base.add(base.add(k1, base.scale(k2, 2.0)), base.add(base.scale(k3, 2.0), k4))
    return base.add(p, base.scale(total, step / 6.0))


def covariant_map(length=0.94, n=5000, kfun=base.base_k, qfun=screen.transport, afun=connection_a, aprimefun=connection_a_prime):
    step, u, p = length / n, -length / 2.0, identity4()
    gfun = lambda x: generator(x, kfun, qfun, afun, aprimefun)
    for _ in range(n):
        p = rk4_matrix(u, p, step, gfun)
        u += step
    return p


def graph_map(length=0.94, n=5000, kfun=base.base_k, qfun=screen.transport, afun=connection_a):
    source, observer = -length / 2.0, length / 2.0
    gs = state_map(qfun(source), afun(source))
    go = state_map(qfun(observer), afun(observer))
    inertial = full.full_map(kfun, length, n)
    return base.mm(base.mm(inverse4(go), inertial), gs)


def zero_connection_control(n=5000, length=0.94):
    qfun = lambda u: base.eye()
    afun = lambda u: base.zero()
    aprimefun = lambda u: base.zero()
    inertial = full.full_map(base.base_k, length, n)
    covariant = covariant_map(length, n, qfun=qfun, afun=afun, aprimefun=aprimefun)
    naive = full.full_map(base.base_k, length, n)
    return {
        "covariant_vs_inertial_residual": matrix_residual(covariant, inertial),
        "naive_vs_inertial_residual": matrix_residual(naive, inertial),
    }


def endpoint_graph_control(n=5000, length=0.94):
    direct, predicted = covariant_map(length, n), graph_map(length, n)
    return {
        "phase_map_residual": matrix_residual(direct, predicted),
        "direct_covariant_map": direct,
        "endpoint_graph_map": predicted,
    }


def naive_counterexample(n=5000, length=0.94):
    covariant = covariant_map(length, n)
    naive = full.full_map(screen.transported_profile(), length, n)
    return {
        "raw_map_difference": matrix_residual(covariant, naive),
        "characteristic_difference": vector_residual(spectrum.characteristic_coefficients(covariant), spectrum.characteristic_coefficients(naive)),
        "disposition": "NAIVE_CONJUGATED_PROFILE_MAP_NOT_ROTATING_COORDINATE_PROPAGATOR",
    }


def canonical_rotation(r):
    return full.assemble(r, base.zero(), base.zero(), r)


def common_basis_control(n=5000, length=0.94, angle=0.57):
    r = screen.rotation(angle)
    kfun = lambda u: base.mm(base.mm(transpose(r), base.base_k(u)), r)
    qfun = lambda u: base.mm(base.mm(transpose(r), screen.transport(u)), r)
    afun = lambda u: base.mm(base.mm(transpose(r), connection_a(u)), r)
    aprimefun = lambda u: base.mm(base.mm(transpose(r), connection_a_prime(u)), r)
    first = covariant_map(length, n)
    second = covariant_map(length, n, kfun, qfun, afun, aprimefun)
    g = canonical_rotation(r)
    predicted = base.mm(base.mm(transpose(g), first), g)
    return {
        "map_similarity_residual": matrix_residual(second, predicted),
        "characteristic_residual": vector_residual(spectrum.characteristic_coefficients(first), spectrum.characteristic_coefficients(second)),
    }


def right_anchor_control(n=5000, length=0.94, angle=-0.41):
    r = screen.rotation(angle)
    qfun = lambda u: base.mm(screen.transport(u), r)
    afun = lambda u: base.mm(base.mm(transpose(r), connection_a(u)), r)
    aprimefun = lambda u: base.mm(base.mm(transpose(r), connection_a_prime(u)), r)
    first = covariant_map(length, n)
    second = covariant_map(length, n, qfun=qfun, afun=afun, aprimefun=aprimefun)
    g = canonical_rotation(r)
    predicted = base.mm(base.mm(transpose(g), first), g)
    return {
        "map_similarity_residual": matrix_residual(second, predicted),
        "characteristic_residual": vector_residual(spectrum.characteristic_coefficients(first), spectrum.characteristic_coefficients(second)),
    }


def scaled_functions(factor):
    kfun = lambda u: base.scale(base.base_k(u / factor), 1.0 / factor ** 2)
    qfun = lambda u: screen.transport(u / factor)
    afun = lambda u: base.scale(connection_a(u / factor), 1.0 / factor)
    aprimefun = lambda u: base.scale(connection_a_prime(u / factor), 1.0 / factor ** 2)
    return kfun, qfun, afun, aprimefun


def affine_orbit_control(n=5000, length=0.94, factor=1.47):
    first = covariant_map(length, n)
    functions = scaled_functions(factor)
    second = covariant_map(factor * length, n, *functions)
    transform = spectrum.diagonal4(1.0 / math.sqrt(factor), math.sqrt(factor))
    predicted = base.mm(base.mm(inverse4(transform), first), transform)
    return {
        "scale_factor": factor,
        "endpoint_graph_scaling_residual": matrix_residual(second, predicted),
        "characteristic_residual": vector_residual(spectrum.characteristic_coefficients(first), spectrum.characteristic_coefficients(second)),
    }


def ell0_gate(symbols):
    return "ELL0_REQUIRES_PHYSICAL_PHASE_VARIABLES_AND_SCALE_LAW" if "ell0" in symbols else "COVARIANT_SCREEN_PHASE_MAP_AFFINE_ORBIT_NOT_ELL0"


def build_artifact(n=5000):
    return {
        "study_id": "plane-wave-covariant-screen-phase-map-v1",
        "classification": "EXACT_SPACETIME_COVARIANT_SCREEN_PHASE_MAP_CORRECTION_AND_NEGATIVE_IDENTIFIABILITY_RESULT",
        "status": "EXACT_PLANE_WAVE_ROTATING_SCREEN_CONNECTION_TERMS_REQUIRED_NAIVE_TRANSPORTED_JACOBI_MAP_SUPERSEDED_NOT_ELL0",
        "open_gate": "PHYSICAL_SCREEN_CONNECTION_ENDPOINT_ANGULAR_VELOCITY_AND_DETECTOR_PHASE_VARIABLES_NOT_DERIVED",
        "raw_objects": ["K", "omega", "Q", "A", "A_prime", "G_source", "G_observer", "P_inertial", "P_naive_conjugated_profile", "P_covariant"],
        "zero_connection": zero_connection_control(n),
        "endpoint_graph": endpoint_graph_control(n),
        "naive_counterexample": naive_counterexample(n),
        "common_basis": common_basis_control(n),
        "right_anchor": right_anchor_control(n),
        "affine_orbit": affine_orbit_control(n),
        "ell0_gate": ell0_gate(["K", "omega", "A", "G", "P", "L"]),
        "correction_disposition": "PR76_WINDOW_RESULTS_PRESERVED_P_TRANSPORT_RENAMED_P_NAIVE_CONJUGATED_PROFILE_ROTATING_PHASE_INTERPRETATION_SUPERSEDED_PR77_VELOCITY_MAP_RETAINED_CHARACTERISTIC_IS_COORDINATE_DIAGNOSTIC_NOT_CANONICAL_INVARIANT",
        "source_scope": "Coley-McNutt-Milson supports exact vacuum Brinkmann plane waves and curvature-driven geodesic deviation; it does not establish the chosen rotating screen, detector phase variables, endpoint angular velocities, window/kernel, affine nuisance law, UMCH, ell0, or detection.",
        "structural_dead_end": False,
        "hypothesis_status": "UNPROVEN",
        "conclusion": "NO_POSITIVE_DETECTION_CLAIM",
    }


def render():
    return json.dumps(build_artifact(), indent=2, sort_keys=True) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    text = render()
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text() != text:
            print("Plane-wave covariant screen-phase artifact differs", file=sys.stderr)
            return 1
        print("Plane-wave covariant screen-phase artifact is current.")
        return 0
    OUTPUT.write_text(text)
    print(f"Wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
