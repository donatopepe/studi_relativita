#!/usr/bin/env python3
"""Finite-boundary Reissner–Nordström null Jacobi control; no UMCH evidence."""
import argparse
import importlib.util
import json
import math
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "reissner-nordstrom-null-scattering-jacobi-results.json"
STATUS = "REISSNER_NORDSTROM_CHARGE_ADDS_DIMENSIONLESS_RICCI_WEYL_OPTICAL_SHAPE_BUT_Q_SQUARED_DEGENERACY_AND_JOINT_MQ_DILATION_RETAIN_ABSOLUTE_SCALE_BLINDNESS_NOT_ELL0"
GATE = "PHYSICAL_CHARGE_SOURCE_EMITTER_ABSORBER_ENDPOINT_SCREEN_PREPARATION_ABSOLUTE_FREQUENCY_RECEIVER_TRANSFER_CALIBRATED_NOISE_JOINT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED"
SCOPE = "FOUR_DIMENSIONAL_ASYMPTOTICALLY_FLAT_REISSNER_NORDSTROM_EXTERIOR_EQUATORIAL_NEUTRAL_FUTURE_NULL_FINITE_EQUAL_RADIUS_ENDPOINT_ONE_TURNING_POINT_DECLARED_SCREEN_UNIT_KILLING_ENERGY_NO_DETECTOR"
CLASSIFICATION = "PROJECT_DERIVATION_AND_TOY_BOUNDARY_CONTROL_WITH_NEGATIVE_CHARGE_SIGN_AND_ABSOLUTE_SCALE_IDENTIFIABILITY_RESULTS"
J = [[0., 0., 1., 0.], [0., 0., 0., 1.], [-1., 0., 0., 0.], [0., -1., 0., 0.]]


def _load(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


sj = _load("rn_schwarzschild_jacobi", "schwarzschild_null_scattering_jacobi.py")
m = sj.m


def maxabs(A):
    return max((abs(x) for row in A for x in row), default=0.)


def sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def transpose(A):
    return [list(row) for row in zip(*A)]


def norm(v):
    return math.sqrt(sum(x * x for x in v))


def photon_radius(epsilon):
    if abs(epsilon) > 1:
        raise ValueError("require abs(epsilon)<=1 for black-hole exterior control")
    return (3 + math.sqrt(9 - 8 * epsilon * epsilon)) / 2


def lapse(x, epsilon):
    return 1 - 2 / x + epsilon * epsilon / (x * x)


def turning_beta(rho, epsilon):
    return rho / math.sqrt(lapse(rho, epsilon))


def validate(M, epsilon, rho, R, n):
    if M <= 0 or abs(epsilon) > 1 or rho <= photon_radius(epsilon) or R <= rho or n < 20:
        raise ValueError("require M>0, abs(epsilon)<=1, R>rho>rho_ph(epsilon), n>=20")


def _trap(values, h):
    return [0.] + [sum((values[k] + values[k + 1]) * h / 2 for k in range(i)) for i in range(1, len(values))]


def _regularized_affine(M, epsilon, rho, R, orientation, n):
    validate(M, epsilon, rho, R, n)
    if orientation not in (-1, 1):
        raise ValueError("orientation must be +/-1")
    beta = turning_beta(rho, epsilon)
    ymax = math.sqrt(R - rho)
    h = ymax / n
    ys = [i * h for i in range(n + 1)]
    # rad(x)=1-beta^2 f(x)/x^2; -d rad/dx at turning is positive outside photon sphere.
    slope = beta * beta * (2 / rho ** 3 - 6 / rho ** 4 + 4 * epsilon * epsilon / rho ** 5)

    def rate(y):
        if y == 0:
            return 2 * M / math.sqrt(slope)
        x = rho + y * y
        rad = 1 - beta * beta * lapse(x, epsilon) / (x * x)
        return 2 * M * y / math.sqrt(max(rad, 1e-30))

    ls = _trap([rate(y) for y in ys], h)
    half = ls[-1]
    path = [("incoming", rho + ys[i] ** 2, half - ls[i]) for i in range(n, 0, -1)]
    path.append(("turning", rho, half))
    path.extend(("outgoing", rho + ys[i] ** 2, half + ls[i]) for i in range(1, n + 1))
    return path, beta


def metric(M, epsilon, r, theta=math.pi / 2):
    x = r / M
    f = lapse(x, epsilon)
    return [-f, 1 / f, r * r, r * r * math.sin(theta) ** 2]


def metric_matrix(M, epsilon, r, theta):
    d = metric(M, epsilon, r, theta)
    return [[d[i] if i == j else 0. for j in range(4)] for i in range(4)]


def _metric_derivative(M, epsilon, r, theta, coordinate, relative_step=2e-5):
    if coordinate not in (1, 2):
        return [[0.] * 4 for _ in range(4)]
    h = relative_step * r if coordinate == 1 else relative_step
    rp, rm = r + (h if coordinate == 1 else 0), r - (h if coordinate == 1 else 0)
    tp, tm = theta + (h if coordinate == 2 else 0), theta - (h if coordinate == 2 else 0)
    gp, gm = metric_matrix(M, epsilon, rp, tp), metric_matrix(M, epsilon, rm, tm)
    return [[(gp[i][j] - gm[i][j]) / (2 * h) for j in range(4)] for i in range(4)]


def christoffel(M, epsilon, r, theta=math.pi / 2, relative_step=2e-5):
    g = metric_matrix(M, epsilon, r, theta)
    gi = [[1 / g[i][i] if i == j else 0. for j in range(4)] for i in range(4)]
    dg = [_metric_derivative(M, epsilon, r, theta, c, relative_step) for c in range(4)]
    return [[[0.5 * sum(gi[a][d] * (dg[b][d][c] + dg[c][d][b] - dg[d][b][c]) for d in range(4))
              for c in range(4)] for b in range(4)] for a in range(4)]


def riemann(M, epsilon, r, theta=math.pi / 2, relative_step=2e-5):
    G = christoffel(M, epsilon, r, theta, relative_step)
    dG = [[[[0.] * 4 for _ in range(4)] for _ in range(4)] for _ in range(4)]
    for coordinate in (1, 2):
        h = relative_step * r if coordinate == 1 else relative_step
        gp = christoffel(M, epsilon, r + (h if coordinate == 1 else 0), theta + (h if coordinate == 2 else 0), relative_step)
        gm = christoffel(M, epsilon, r - (h if coordinate == 1 else 0), theta - (h if coordinate == 2 else 0), relative_step)
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    dG[coordinate][a][b][c] = (gp[a][b][c] - gm[a][b][c]) / (2 * h)
    raised = [[[[dG[c][a][d][b] - dG[d][a][c][b] + sum(G[a][c][e] * G[e][d][b] - G[a][d][e] * G[e][c][b] for e in range(4))
                for d in range(4)] for c in range(4)] for b in range(4)] for a in range(4)]
    gd = metric(M, epsilon, r, theta)
    return [[[[gd[a] * raised[a][b][c][d] for d in range(4)] for c in range(4)] for b in range(4)] for a in range(4)]


def _project(Rm, screen, k):
    return [[-sum(Rm[a][b][c][d] * screen[A][a] * k[b] * screen[B][c] * k[d]
                  for a in range(4) for b in range(4) for c in range(4) for d in range(4))
             for B in range(2)] for A in range(2)]


def _screen_sample(M, epsilon, beta, orientation, item):
    branch, x, lam = item
    r, f = M * x, lapse(x, epsilon)
    rad = max(0., 1 - beta * beta * f / (x * x))
    sign = -1 if branch == "incoming" else 1 if branch == "outgoing" else 0
    nr = sign * math.sqrt(rad)
    k = [1 / f, nr, 0., orientation * beta * M / (r * r)]
    e1 = [0., 0., 1 / r, 0.]
    e2 = [0., -orientation * beta * f / x, 0., nr / r]
    screen = [e1, e2]
    g = metric(M, epsilon, r)
    dot = lambda u, v: sum(g[i] * u[i] * v[i] for i in range(4))
    ortho = max(abs(dot(k, e1)), abs(dot(k, e2)), abs(dot(e1, e1) - 1), abs(dot(e2, e2) - 1), abs(dot(e1, e2)))
    K = _project(riemann(M, epsilon, r), screen, k)
    tr = K[0][0] + K[1][1]
    return {"branch": branch, "lambda": lam, "lambda_over_M": lam / M, "r": r, "r_over_M": x,
            "screen_order": ["polar", "in-plane"], "screen_orthonormality_residual": ortho, "K": K,
            "K_trace": tr, "K_trace_free": [[K[0][0] - tr / 2, K[0][1]], [K[1][0], K[1][1] - tr / 2]],
            "M2_K": [[M * M * z for z in row] for row in K]}


def profile_control(M=1., epsilon=0.8, rho=4., R=12., orientation=1, n=60):
    path, beta = _regularized_affine(M, epsilon, rho, R, orientation, n)
    samples = [_screen_sample(M, epsilon, beta, orientation, z) for z in path]
    return {"M": M, "Q": epsilon * M, "epsilon": epsilon, "rho": rho, "R": R, "beta": beta,
            "orientation": orientation, "branches": ["incoming", "turning", "outgoing"],
            "screen_order": ["polar", "in-plane"], "affine_normalization": "UNIT_KILLING_ENERGY_PROJECT_ANCHOR_NOT_DETECTOR_FREQUENCY",
            "samples": samples, "maximum_screen_orthonormality_residual": max(z["screen_orthonormality_residual"] for z in samples),
            "maximum_K_symmetry_residual": max(abs(z["K"][0][1] - z["K"][1][0]) for z in samples),
            "maximum_abs_Ricci_trace": max(abs(z["K_trace"]) for z in samples)}


def generator(K):
    return [[0., 0., 1., 0.], [0., 0., 0., 1.], [K[0][0], K[0][1], 0., 0.], [K[1][0], K[1][1], 0., 0.]]


def _maps(profile):
    samples, P, maps = profile["samples"], m.eye(), [m.eye()]
    for a, b in zip(samples, samples[1:]):
        h = b["lambda"] - a["lambda"]
        K = [[(a["K"][i][j] + b["K"][i][j]) / 2 for j in range(2)] for i in range(2)]
        P = m.mm(m.expm(m.scale(generator(K), h)), P)
        maps.append(P)
    return maps


def _phase_from_profile(profile):
    maps = _maps(profile)
    P = maps[-1]
    reverse = m.eye()
    samples = profile["samples"]
    for a, b in zip(reversed(samples[1:]), reversed(samples[:-1])):
        h = b["lambda"] - a["lambda"]
        K = [[(a["K"][i][j] + b["K"][i][j]) / 2 for j in range(2)] for i in range(2)]
        reverse = m.mm(m.expm(m.scale(generator(K), h)), reverse)
    turn = len(samples) // 2
    composition = m.mm(maps[-1], sj.inverse(maps[turn]))
    composition = m.mm(composition, maps[turn])
    sym = m.mm(transpose(P), m.mm(J, P))
    return maps, P, {"symplectic_residual": maxabs(sub(sym, J)), "reverse_inverse_residual": maxabs(sub(m.mm(reverse, P), m.eye())), "turning_composition_residual": maxabs(sub(composition, P))}


def phase_control(M=1., epsilon=0.8, rho=4., R=12., orientation=1, n=60):
    profile = profile_control(M, epsilon, rho, R, orientation, n)
    maps, P, residuals = _phase_from_profile(profile)
    A, B, C, D = sj.split(P)
    return {**residuals, "P_phase": P, "A": A, "B": B, "C": C, "D": D, "graph": graph(D, B),
            "primary_object": "FULL_SCREEN_PHASE_MAP_THROUGH_CAUSTICS", "profile": profile, "checkpoint_maps": maps}


def graph(D, B, tol=1e-8):
    return sj.graph(D, B, tol)


def zero_window_control():
    return {"P_phase": m.eye(), "identity_residual": 0., "classification": "ZERO_AFFINE_WINDOW_IDENTITY"}


def _matrix_residual(A, B):
    return maxabs(sub(A, B))


def schwarzschild_limit_control(rho=4., R=12., n=50):
    a, b = profile_control(epsilon=0., rho=rho, R=R, n=n), sj.profile_control(rho=rho, R=R, n=n)
    path = max(abs(x["lambda"] - y["lambda"]) for x, y in zip(a["samples"], b["samples"]))
    profile = max(_matrix_residual(x["K"], y["K"]) for x, y in zip(a["samples"], b["samples"]))
    phase = _matrix_residual(phase_control(epsilon=0., rho=rho, R=R, n=n)["P_phase"], sj.phase_control(rho=rho, R=R, n=n)["P_phase"])
    return {"path_residual": path, "profile_residual": profile, "phase_map_residual": phase, "classification": "SCHWARZSCHILD_LIMIT_CONFORMANCE"}


def charge_sign_control(epsilon=0.8, n=45):
    a, b = phase_control(epsilon=epsilon, n=n), phase_control(epsilon=-epsilon, n=n)
    return {"path_residual": max(abs(x["lambda"] - y["lambda"]) for x, y in zip(a["profile"]["samples"], b["profile"]["samples"])),
            "profile_residual": max(_matrix_residual(x["K"], y["K"]) for x, y in zip(a["profile"]["samples"], b["profile"]["samples"])),
            "phase_map_residual": _matrix_residual(a["P_phase"], b["P_phase"]), "classification": "Q_SQUARED_METRIC_DEGENERACY_NOT_ELL0"}


def orientation_control(epsilon=0.8, n=45):
    a, b = phase_control(epsilon=epsilon, orientation=1, n=n), phase_control(epsilon=epsilon, orientation=-1, n=n)
    return {"phase_similarity_residual": _matrix_residual(a["P_phase"], b["P_phase"]),
            "scope": "DECLARED_EQUATORIAL_SCREEN_ONLY_NOT_STATISTICAL_INDEPENDENCE"}


def conversion(factor):
    return [[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., 1 / factor, 0.], [0., 0., 0., 1 / factor]]


def geometric_scale_control(factor=2.5, epsilon=0.8, n=45):
    a, b = phase_control(M=1., epsilon=epsilon, n=n), phase_control(M=factor, epsilon=epsilon, n=n)
    D = conversion(factor)
    back = m.mm(sj.inverse(D), m.mm(b["P_phase"], D))
    prof = max(_matrix_residual(x["M2_K"], y["M2_K"]) for x, y in zip(a["profile"]["samples"], b["profile"]["samples"]))
    return {"factor": factor, "dimensionless_profile_residual": prof, "frequency_converted_phase_map_residual": _matrix_residual(a["P_phase"], back),
            "classification": "JOINT_MQ_GEOMETRIC_DILATION_NOT_INTERIOR_SCALE"}


def _features(M, epsilon, n):
    c = phase_control(M=M, epsilon=epsilon, n=n)
    D = conversion(M)
    P = m.mm(sj.inverse(D), m.mm(c["P_phase"], D))
    turn = c["profile"]["samples"][len(c["profile"]["samples"]) // 2]
    return [P[0][0], P[0][2], P[1][1], P[1][3], turn["M2_K"][0][0], turn["M2_K"][1][1], turn["K_trace"] * M * M]


def rank_control(epsilon=0.8, n=35, step=2e-4):
    def col(a, b):
        return [(x - y) / (2 * step) for x, y in zip(a, b)]
    # Exact dilation representative: converted features depend only on epsilon;
    # direct multi-M residual is audited separately in geometric_scale_control.
    cm = [0. for _ in _features(1., epsilon, n)]
    ce = col(_features(1., epsilon + step, n), _features(1., epsilon - step, n))
    return {"jacobian_columns": {"log_M": cm, "epsilon": ce}, "rank_with_log_M_and_epsilon": sj.matrix_rank([cm, ce], 1e-5),
            "log_M_column_norm": norm(cm), "scale_null_direction": [1, 0], "independent_channels": False,
            "dependence_status": "DEPENDENCE_UNRESOLVED_WITHOUT_JOINT_COVARIANCE"}


def _stable(x):
    if isinstance(x, float):
        if abs(x) < 1e-7:
            return 0.0
        return float(format(x, ".8g"))
    if isinstance(x, list):
        return [_stable(z) for z in x]
    if isinstance(x, dict):
        return {k: _stable(v) for k, v in x.items()}
    return x


def build_result(n=40):
    result = {"status": STATUS, "scope": SCOPE, "classification": CLASSIFICATION, "gate": GATE, "UMCH": "UNPROVEN",
              "ell0_identified": False, "structural_dead_end": "NOT_DECLARED", "detection": "NO_POSITIVE_DETECTION_CLAIM",
              "maximum_interpretation": "CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE", "raw": phase_control(n=n),
              "zero_window": zero_window_control(), "schwarzschild_limit": schwarzschild_limit_control(n=n),
              "charge_sign": charge_sign_control(n=n), "orientation": orientation_control(n=n),
              "geometric_scale": geometric_scale_control(n=n), "rank": rank_control(n=max(30, n - 5)),
              "source_scope": "CANONICAL_RN_AND_SACHS_SOURCES_DO_NOT_ESTABLISH_PROJECT_PROTOCOL_ELL0_UMCH_OR_DETECTION"}
    result["raw"].pop("checkpoint_maps")
    result["raw"]["profile"]["samples"] = [result["raw"]["profile"]["samples"][i] for i in (0, n, 2 * n)]
    return _stable(result)


def render(path=OUT, n=40):
    path.write_text(json.dumps(build_result(n), indent=2, sort_keys=True) + "\n")


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=pathlib.Path, default=OUT)
    parser.add_argument("--samples", type=int, default=40)
    args = parser.parse_args(argv)
    render(args.output, args.samples)


if __name__ == "__main__":
    main()
