#!/usr/bin/env python3
"""Schwarzschild scattering screen/Riemann conformance control; no UMCH inference."""
import argparse
import importlib.util
import json
import math
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "schwarzschild-scattering-screen-conformance-results.json"
_BASE_SPEC = importlib.util.spec_from_file_location(
    "schwarzschild_scattering_jacobi_base", HERE / "schwarzschild_null_scattering_jacobi.py"
)
base = importlib.util.module_from_spec(_BASE_SPEC)
_BASE_SPEC.loader.exec_module(base)


def metric(M, r, theta=math.pi / 2):
    f = 1.0 - 2.0 * M / r
    return [-f, 1.0 / f, r * r, r * r * math.sin(theta) ** 2]


def dot(g, u, v):
    return sum(g[i] * u[i] * v[i] for i in range(4))


def christoffel_equatorial(M, r):
    f = 1.0 - 2.0 * M / r
    G = [[[0.0 for _ in range(4)] for _ in range(4)] for _ in range(4)]

    def sym(mu, a, b, value):
        G[mu][a][b] = value
        G[mu][b][a] = value

    sym(0, 0, 1, M / (r * r * f))
    G[1][0][0] = f * M / (r * r)
    G[1][1][1] = -M / (r * r * f)
    G[1][2][2] = -r * f
    G[1][3][3] = -r * f
    sym(2, 1, 2, 1.0 / r)
    sym(3, 1, 3, 1.0 / r)
    return G


def _vectors(M, rho, beta, orientation, item):
    branch, x, lam = item
    r = M * x
    f = 1.0 - 2.0 * M / r
    rad = max(0.0, 1.0 - (M * beta) ** 2 * f / (r * r))
    sign = -1.0 if branch == "incoming" else 1.0 if branch == "outgoing" else 0.0
    nr = sign * math.sqrt(rad)
    nphi = orientation * M * beta * math.sqrt(f) / r
    k = [1.0 / f, nr, 0.0, orientation * M * beta / (r * r)]
    e1 = [0.0, 0.0, 1.0 / r, 0.0]
    e2 = [0.0, -nphi * math.sqrt(f), 0.0, nr / r]
    # Auxiliary future-null vector normalized by k.l=-1.
    ell = [0.5, -0.5 * f * nr, 0.0, -0.5 * math.sqrt(f) * nphi / r]
    return {"branch": branch, "lambda": lam, "r": r, "f": f, "k": k, "screen": [e1, e2], "ell": ell}


def _derivative(values, xs, i):
    if i == 0:
        h = xs[1] - xs[0]
        return [(values[1][j] - values[0][j]) / h for j in range(4)]
    if i == len(xs) - 1:
        h = xs[-1] - xs[-2]
        return [(values[-1][j] - values[-2][j]) / h for j in range(4)]
    x0, x1, x2 = xs[i - 1], xs[i], xs[i + 1]
    c0 = (x1 - x2) / ((x0 - x1) * (x0 - x2))
    c1 = (2.0 * x1 - x0 - x2) / ((x1 - x0) * (x1 - x2))
    c2 = (x1 - x0) / ((x2 - x0) * (x2 - x1))
    return [c0 * values[i - 1][j] + c1 * values[i][j] + c2 * values[i + 1][j] for j in range(4)]


def _euclidean_tetrad_norm(v, r, f):
    tetrad = [math.sqrt(f) * v[0], v[1] / math.sqrt(f), r * v[2], r * v[3]]
    return math.sqrt(sum(z * z for z in tetrad))


def screen_transport_control(M=1.0, rho=4.0, R=12.0, orientation=1, n=120):
    path, beta = base._regularized_affine(M, rho, R, orientation, n)
    rows = [_vectors(M, rho, beta, orientation, item) for item in path]
    lambdas = [row["lambda"] for row in rows]
    screens = [[row["screen"][A] for row in rows] for A in range(2)]
    samples = []
    max_null = max_screen = max_kscreen = 0.0
    interior_q = interior_rotation = interior_raw = endpoint_q = 0.0
    for i, row in enumerate(rows):
        r, f, k, ell = row["r"], row["f"], row["k"], row["ell"]
        g = metric(M, r)
        max_null = max(max_null, abs(dot(g, k, k)), abs(dot(g, ell, ell)), abs(dot(g, k, ell) + 1.0))
        for A in range(2):
            max_kscreen = max(max_kscreen, abs(dot(g, k, row["screen"][A])))
            for B in range(2):
                max_screen = max(max_screen, abs(dot(g, row["screen"][A], row["screen"][B]) - float(A == B)))
        G = christoffel_equatorial(M, r)
        raw, quotient, coefficients, rotations = [], [], [], []
        for A in range(2):
            de = _derivative(screens[A], lambdas, i)
            e = row["screen"][A]
            q = [de[mu] + sum(G[mu][a][b] * k[a] * e[b] for a in range(4) for b in range(4)) for mu in range(4)]
            alpha = -dot(g, ell, q)
            qp = [q[mu] - alpha * k[mu] for mu in range(4)]
            raw.append(q)
            quotient.append(qp)
            coefficients.append(alpha)
            rotations.append([dot(g, row["screen"][B], q) for B in range(2)])
            raw_norm = _euclidean_tetrad_norm(q, r, f)
            q_norm = _euclidean_tetrad_norm(qp, r, f)
            rot_norm = max(abs(z) for z in rotations[-1])
            if i in (0, len(rows) - 1):
                endpoint_q = max(endpoint_q, q_norm)
            else:
                interior_raw = max(interior_raw, raw_norm)
                interior_q = max(interior_q, q_norm)
                interior_rotation = max(interior_rotation, rot_norm)
        samples.append({
            "branch": row["branch"], "lambda": row["lambda"], "r": r,
            "raw_covariant_derivative": raw,
            "null_gauge_coefficient": coefficients,
            "quotient_covariant_derivative": quotient,
            "screen_rotation": rotations,
        })
    indices = [0, n, len(rows) - 1]
    return {
        "screen_handedness": orientation,
        "max_null_residual": max_null,
        "max_screen_metric_residual": max_screen,
        "max_k_screen_residual": max_kscreen,
        "interior_max_raw_covariant_derivative": interior_raw,
        "interior_max_quotient_residual": interior_q,
        "interior_max_screen_rotation": interior_rotation,
        "endpoint_max_quotient_residual": endpoint_q,
        "checkpoints": [{"branch": rows[i]["branch"], "lambda": rows[i]["lambda"], "r": rows[i]["r"]} for i in indices],
        "samples": samples,
    }


def metric_matrix(M, r, theta):
    diagonal = metric(M, r, theta)
    return [[diagonal[i] if i == j else 0.0 for j in range(4)] for i in range(4)]


def _metric_derivative(M, r, theta, coordinate, h_r, h_theta):
    if coordinate not in (1, 2):
        return [[0.0] * 4 for _ in range(4)]
    step = h_r if coordinate == 1 else h_theta
    plus = metric_matrix(M, r + (step if coordinate == 1 else 0.0), theta + (step if coordinate == 2 else 0.0))
    minus = metric_matrix(M, r - (step if coordinate == 1 else 0.0), theta - (step if coordinate == 2 else 0.0))
    return [[(plus[i][j] - minus[i][j]) / (2.0 * step) for j in range(4)] for i in range(4)]


def numerical_christoffel(M, r, theta, relative_step):
    h_r = relative_step * r
    h_theta = relative_step
    g = metric_matrix(M, r, theta)
    gi = [[(1.0 / g[i][i]) if i == j else 0.0 for j in range(4)] for i in range(4)]
    dg = [_metric_derivative(M, r, theta, c, h_r, h_theta) for c in range(4)]
    G = [[[0.0 for _ in range(4)] for _ in range(4)] for _ in range(4)]
    for a in range(4):
        for b in range(4):
            for c in range(4):
                G[a][b][c] = 0.5 * sum(gi[a][d] * (dg[b][d][c] + dg[c][d][b] - dg[d][b][c]) for d in range(4))
    return G


def numerical_riemann_lowered(M, r, theta, relative_step):
    h_r = relative_step * r
    h_theta = relative_step
    G = numerical_christoffel(M, r, theta, relative_step)
    dG = [[[[0.0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(4)]
    for coordinate, step in ((1, h_r), (2, h_theta)):
        gp = numerical_christoffel(
            M, r + (step if coordinate == 1 else 0.0), theta + (step if coordinate == 2 else 0.0), relative_step
        )
        gm = numerical_christoffel(
            M, r - (step if coordinate == 1 else 0.0), theta - (step if coordinate == 2 else 0.0), relative_step
        )
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    dG[coordinate][a][b][c] = (gp[a][b][c] - gm[a][b][c]) / (2.0 * step)
    raised = [[[[0.0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(4)]
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    raised[a][b][c][d] = (
                        dG[c][a][d][b] - dG[d][a][c][b]
                        + sum(G[a][c][eta] * G[eta][d][b] - G[a][d][eta] * G[eta][c][b] for eta in range(4))
                    )
    g = metric(M, r, theta)
    return [[[[g[a] * raised[a][b][c][d] for d in range(4)] for c in range(4)] for b in range(4)] for a in range(4)]


def _project_riemann(Riemann, screen, k):
    return [[
        -sum(Riemann[a][b][c][d] * screen[A][a] * k[b] * screen[B][c] * k[d]
             for a in range(4) for b in range(4) for c in range(4) for d in range(4))
        for B in range(2)] for A in range(2)]


def matrix_distance(A, B):
    return math.sqrt(sum((A[i][j] - B[i][j]) ** 2 for i in range(len(A)) for j in range(len(A[0]))))


def _projection_at(M, rho, beta, orientation, item, relative_step):
    vectors = _vectors(M, rho, beta, orientation, item)
    r = vectors["r"]
    Riemann = numerical_riemann_lowered(M, r, math.pi / 2, relative_step)
    K_fd = _project_riemann(Riemann, vectors["screen"], vectors["k"])
    amp = 3.0 * M * (M * beta) ** 2 / r ** 5
    K_analytic = [[-amp, 0.0], [0.0, amp]]
    return {
        "branch": vectors["branch"], "r": r, "screen": vectors["screen"],
        "K_fd": K_fd, "K_analytic": K_analytic,
        "profile_mismatch": matrix_distance(K_fd, K_analytic),
        "symmetry_residual": abs(K_fd[0][1] - K_fd[1][0]),
        "vacuum_trace_residual": abs(K_fd[0][0] + K_fd[1][1]),
    }


def riemann_projection_control(M=1.0, rho=4.0, R=12.0, orientation=1, coarse_step=4e-4, fine_step=1e-4):
    path, beta = base._regularized_affine(M, rho, R, orientation, 24)
    items = [path[0], path[24], path[-1]]
    coarse = [_projection_at(M, rho, beta, orientation, item, coarse_step) for item in items]
    fine = [_projection_at(M, rho, beta, orientation, item, fine_step) for item in items]
    return {
        "uses_radial_metric_derivatives": True,
        "uses_polar_metric_derivatives": True,
        "coarse_relative_step": coarse_step,
        "fine_relative_step": fine_step,
        "coarse_max_profile_mismatch": max(row["profile_mismatch"] for row in coarse),
        "fine_max_profile_mismatch": max(row["profile_mismatch"] for row in fine),
        "fine_max_symmetry_residual": max(row["symmetry_residual"] for row in fine),
        "fine_max_vacuum_trace_residual": max(row["vacuum_trace_residual"] for row in fine),
        "coarse_checkpoints": coarse,
        "fine_checkpoints": fine,
    }


def photon_sphere_anchor(rho=3.000001):
    beta = base.sc.turning_beta(rho)
    value = 3.0 * beta * beta / rho ** 5
    return {
        "rho": rho,
        "turning_M2_K_polar": -value,
        "turning_M2_K_in_plane": value,
        "limit": "diag(-1,+1)/3 in (polar,in-plane) order",
    }


def build_result():
    transport_coarse = screen_transport_control(n=60)
    transport_fine = screen_transport_control(n=120)
    plus = riemann_projection_control(orientation=1)
    minus = riemann_projection_control(orientation=-1)
    corrected = base.build_result(n=120)
    return {
        "study_id": "schwarzschild-scattering-screen-conformance-v1",
        "status": "SCHWARZSCHILD_SCATTERING_SCREEN_IS_PARALLEL_MODULO_NULL_GAUGE_BUT_FULL_RIEMANN_RECONSTRUCTION_FALSIFIES_PRIOR_OPTICAL_PROFILE_AND_REQUIRES_CORRECTED_PHASE_MAP_NOT_ELL0",
        "prior_profile": "diag(+1,-1) M b^2/r^5",
        "corrected_profile": "diag(-1,+1) 3 M b^2/r^5 in (polar,in-plane) order",
        "prior_profile_status": "FALSIFIED_BY_INDEPENDENT_FOUR_DIMENSIONAL_RIEMANN_RECONSTRUCTION",
        "classification": "BOUNDED_PROJECT_CORRECTION_AND_NEGATIVE_IDENTIFIABILITY_CONTROL",
        "screen_transport": {
            "coarse_n": 60,
            "fine_n": 120,
            "coarse_interior_max_quotient_residual": transport_coarse["interior_max_quotient_residual"],
            "fine_interior_max_quotient_residual": transport_fine["interior_max_quotient_residual"],
            "fine_interior_max_raw_covariant_derivative": transport_fine["interior_max_raw_covariant_derivative"],
            "fine_interior_max_screen_rotation": transport_fine["interior_max_screen_rotation"],
            "fine_endpoint_max_quotient_residual": transport_fine["endpoint_max_quotient_residual"],
            "max_null_residual": transport_fine["max_null_residual"],
            "max_screen_metric_residual": transport_fine["max_screen_metric_residual"],
            "max_k_screen_residual": transport_fine["max_k_screen_residual"],
            "fine_samples": transport_fine["samples"],
            "classification": "PARALLEL_SCREEN_MODULO_EXPLICIT_NULL_GAUGE_PROJECT_DERIVATION",
        },
        "riemann_projection": {
            "orientation_plus": plus,
            "orientation_minus": minus,
            "orientation_profile_residual": matrix_distance(plus["fine_checkpoints"][1]["K_fd"], minus["fine_checkpoints"][1]["K_fd"]),
            "photon_sphere_anchor": photon_sphere_anchor(),
            "classification": "FULL_4D_FINITE_DIFFERENCE_RIEMANN_PROJECT_DERIVATION_INCLUDES_THETA_DERIVATIVES",
        },
        "corrected_phase_map": {
            "status": corrected["status"],
            "symplectic_residual": corrected["raw"]["symplectic_residual"],
            "reverse_inverse_residual": corrected["raw"]["reverse_inverse_residual"],
            "turning_composition_residual": corrected["raw"]["turning_composition_residual"],
            "dimensionless_profile_residual": corrected["geometric_scale"]["dimensionless_profile_residual"],
            "converted_phase_map_residual": corrected["geometric_scale"]["converted_phase_map_residual"],
            "rank_shape_boundary": corrected["rank"]["rank_shape_boundary"],
            "rank_with_log_M": corrected["rank"]["rank_with_log_M"],
            "log_M_column_norm": corrected["rank"]["log_M_column_norm"],
            "scale_null_direction": corrected["rank"]["scale_null_direction"],
            "global_injectivity": corrected["rank"]["global_injectivity"],
        },
        "gate": corrected["gate"],
        "UMCH": "UNPROVEN",
        "ell0_identified": False,
        "structural_dead_end": "NOT_DECLARED",
        "detection": "NO_POSITIVE_DETECTION_CLAIM",
        "maximum_interpretation": "CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE",
        "review": "DIRECT_REVIEW_NO_SUBAGENT",
        "source_scope": corrected["source_scope"],
    }


def render():
    return json.dumps(build_result(), indent=2, sort_keys=True) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    text = render()
    if args.check:
        if not OUT.exists() or OUT.read_text() != text:
            raise SystemExit("artifact mismatch")
    else:
        OUT.write_text(text)


if __name__ == "__main__":
    main()
