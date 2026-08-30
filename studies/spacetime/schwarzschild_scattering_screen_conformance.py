#!/usr/bin/env python3
"""Schwarzschild scattering screen/Riemann conformance control; no UMCH inference."""
import importlib.util
import math
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
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
