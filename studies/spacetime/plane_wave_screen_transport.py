#!/usr/bin/env python3
"""Screen-transport, finite-window, and Jacobi order controls in an exact plane wave."""
import argparse
import importlib.util
import json
import math
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
OUTPUT = HERE / "plane-wave-screen-transport-results.json"


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


base = load("plane_wave_cross_channel_transport", "plane_wave_cross_channel.py")
full = load("plane_wave_full_jacobi_transport", "plane_wave_full_jacobi.py")
spectrum = load("plane_wave_common_spectrum_transport", "plane_wave_common_spectrum.py")


def transpose(a):
    return [list(row) for row in zip(*a)]


def subtract(a, b):
    return base.add(a, b, -1.0)


def rotation(angle):
    c, s = math.cos(angle), math.sin(angle)
    return [[c, -s], [s, c]]


def omega(u):
    return 0.43 + 0.31 * u + 0.14 * u * u


def omega_integral(u):
    return 0.43 * u + 0.155 * u * u + (0.14 / 3.0) * u ** 3


def transport(u, omega_integral_fun=omega_integral):
    return rotation(-omega_integral_fun(u))


def transported_profile(kfun=base.base_k, omega_integral_fun=omega_integral):
    def profile(u):
        q = transport(u, omega_integral_fun)
        return base.mm(base.mm(transpose(q), kfun(u)), q)
    return profile


def kernel_weight(u, length, kernel):
    if kernel == "top_hat":
        return 1.0
    if kernel == "triangular":
        return max(0.0, 1.0 - 2.0 * abs(u) / length)
    raise ValueError(kernel)


def window(kfun, length=0.94, kernel="top_hat", n=5000):
    step = length / n
    out = base.zero()
    for index in range(n + 1):
        u = -length / 2.0 + index * step
        endpoint = 0.5 if index in (0, n) else 1.0
        out = base.add(out, base.scale(kfun(u), endpoint * kernel_weight(u, length, kernel) * step))
    return out


def matrix_residual(a, b):
    return base.norm(subtract(a, b))


def characteristic(p):
    return spectrum.characteristic_coefficients(p)


def vector_residual(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def zero_connection_control(n=5000, length=0.94):
    zero_integral = lambda u: 0.0
    moved = transported_profile(base.base_k, zero_integral)
    return {
        "window_residual": matrix_residual(window(base.base_k, length, n=n), window(moved, length, n=n)),
        "map_residual": matrix_residual(full.full_map(base.base_k, length, n), full.full_map(moved, length, n)),
    }


def order_control(n=5000, length=0.94, kernel="top_hat"):
    moved = transported_profile()
    raw_w, moved_w = window(base.base_k, length, kernel, n), window(moved, length, kernel, n)
    raw_p, moved_p = full.full_map(base.base_k, length, n), full.full_map(moved, length, n)
    return {
        "kernel": kernel,
        "raw_window": raw_w,
        "transported_window": moved_w,
        "window_difference": matrix_residual(raw_w, moved_w),
        "map_difference": matrix_residual(raw_p, moved_p),
        "characteristic_difference": vector_residual(characteristic(raw_p), characteristic(moved_p)),
    }


def invariants(a):
    trace = a[0][0] + a[1][1]
    determinant = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    frobenius2 = sum(value * value for row in a for value in row)
    return [trace, determinant, frobenius2]


def invariant_average(kfun, length=0.94, n=5000):
    step = length / n
    out = [0.0, 0.0, 0.0]
    for index in range(n + 1):
        u = -length / 2.0 + index * step
        endpoint = 0.5 if index in (0, n) else 1.0
        local = invariants(kfun(u))
        for j in range(3):
            out[j] += endpoint * step * local[j]
    return out


def invariant_average_control(n=5000, length=0.94):
    moved = transported_profile()
    sample_residuals = [vector_residual(invariants(base.base_k(-length / 2 + i * length / 40)), invariants(moved(-length / 2 + i * length / 40))) for i in range(41)]
    raw_average = invariant_average(base.base_k, length, n)
    moved_average = invariant_average(moved, length, n)
    isotropic = base.scale(base.eye(), raw_average[0] / (2.0 * length))
    moved_w = window(moved, length, n=n)
    moved_p = full.full_map(moved, length, n)
    reconstructed_p = full.full_map(lambda u: isotropic, length, n)
    return {
        "pointwise_max_residual": max(sample_residuals),
        "raw_invariant_average": raw_average,
        "transported_invariant_average": moved_average,
        "average_invariant_residual": vector_residual(raw_average, moved_average),
        "reconstruction_rule": "ISOTROPIC_TRACE_ONLY_REPRESENTATIVE",
        "transported_window_vs_invariant_reconstruction_gap": matrix_residual(moved_w, base.scale(isotropic, length)),
        "transported_map_vs_invariant_reconstruction_gap": matrix_residual(moved_p, reconstructed_p),
    }


def canonical_rotation(r):
    z = base.zero()
    return full.assemble(r, z, z, r)


def common_basis_control(n=5000, length=0.94, angle=0.57):
    moved = transported_profile()
    r = rotation(angle)
    rotated = lambda u: base.mm(base.mm(transpose(r), moved(u)), r)
    first_w, second_w = window(moved, length, n=n), window(rotated, length, n=n)
    first_p, second_p = full.full_map(moved, length, n), full.full_map(rotated, length, n)
    g = canonical_rotation(r)
    predicted_w = base.mm(base.mm(transpose(r), first_w), r)
    predicted_p = base.mm(base.mm(transpose(g), first_p), g)
    return {
        "window_conjugation_residual": matrix_residual(second_w, predicted_w),
        "map_similarity_residual": matrix_residual(second_p, predicted_p),
        "characteristic_residual": vector_residual(characteristic(first_p), characteristic(second_p)),
    }


def scaled_profile(factor):
    return lambda u: base.scale(base.base_k(u / factor), 1.0 / factor ** 2)


def scaled_omega_integral(factor):
    return lambda u: omega_integral(u / factor)


def affine_orbit_control(kernel="top_hat", n=5000, length=0.94, factor=1.47):
    first_k = transported_profile()
    second_k = transported_profile(scaled_profile(factor), scaled_omega_integral(factor))
    first_w = base.scale(window(first_k, length, kernel, n), length)
    second_w = base.scale(window(second_k, factor * length, kernel, n), factor * length)
    first_p = full.full_map(first_k, length, n)
    second_p = full.full_map(second_k, factor * length, n)
    return {
        "kernel": kernel,
        "scale_factor": factor,
        "dimensionless_window_residual": matrix_residual(first_w, second_w),
        "characteristic_residual": vector_residual(characteristic(first_p), characteristic(second_p)),
    }


def alternate_omega_integral(u):
    return 0.19 * u - 0.12 * u * u + 0.08 * u ** 3


def transport_profile_mobility_control(n=5000, length=0.94):
    first, second = transported_profile(), transported_profile(base.base_k, alternate_omega_integral)
    return {
        "curvature_profile_difference": 0.0,
        "window_difference": matrix_residual(window(first, length, n=n), window(second, length, n=n)),
        "map_difference": matrix_residual(full.full_map(first, length, n), full.full_map(second, length, n)),
        "interpretation": "TRANSPORT_PROTOCOL_MOVES_OUTPUTS_AT_FIXED_CURVATURE",
    }


def ell0_gate(symbols):
    return "ELL0_REQUIRES_PHYSICAL_TRANSPORT_AND_SCALE_LAW" if "ell0" in symbols else "SCREEN_TRANSPORT_WINDOW_JACOBI_PROTOCOL_AND_AFFINE_NOT_ELL0"


def build_artifact(n=5000):
    return {
        "study_id": "plane-wave-screen-transport-window-jacobi-v1",
        "classification": "EXACT_SPACETIME_TRANSPORT_WINDOW_JACOBI_CONTROL_AND_NEGATIVE_IDENTIFIABILITY_RESULT",
        "status": "EXACT_PLANE_WAVE_SCREEN_TRANSPORT_AVERAGE_ORDER_OPERATOR_AND_JACOBI_PROTOCOL_DEPENDENT_AFFINE_SCALE_BLIND_NOT_ELL0",
        "open_gate": "PHYSICAL_SCREEN_CONNECTION_PATH_KERNEL_AND_COMMON_ENDPOINT_STANDARD_NOT_DERIVED",
        "raw_objects": ["K", "omega", "Q", "W_raw", "W_transport", "local_invariant_averages", "P_raw", "P_transport"],
        "zero_connection": zero_connection_control(n),
        "order_top_hat": order_control(n=n),
        "order_triangular": order_control(n=n, kernel="triangular"),
        "invariant_average": invariant_average_control(n),
        "common_basis": common_basis_control(n),
        "affine_top_hat": affine_orbit_control(n=n),
        "affine_triangular": affine_orbit_control(kernel="triangular", n=n),
        "transport_profile_mobility": transport_profile_mobility_control(n),
        "ell0_gate": ell0_gate(["K", "omega", "Q", "W", "P", "L"]),
        "source_scope": "Coley-McNutt-Milson supports exact vacuum Brinkmann plane waves and curvature-driven geodesic deviation; it does not establish the chosen screen connection, window/kernel, path/anchor, common endpoint standard, affine scaling law, UMCH, ell0, or detection.",
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
            print("Plane-wave screen-transport artifact differs", file=sys.stderr)
            return 1
        print("Plane-wave screen-transport artifact is current.")
        return 0
    OUTPUT.write_text(text)
    print(f"Wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
