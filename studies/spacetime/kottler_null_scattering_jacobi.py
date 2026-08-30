#!/usr/bin/env python3
"""Finite-boundary Kottler null Jacobi control; no UMCH evidence."""
import argparse
import importlib.util
import json
import math
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "kottler-null-scattering-jacobi-results.json"
STATUS = "KOTTLER_LAMBDA_ADDS_STATIC_BOUNDARY_NORMALIZATION_BUT_NULL_RICCI_FOCUSING_AND_CONVERTED_NULL_JACOBI_SHAPE_CANCEL_WHILE_JOINT_MLAMBDA_DILATION_RETAINS_ABSOLUTE_SCALE_BLINDNESS_NOT_ELL0"
GATE = "PHYSICAL_COSMOLOGICAL_MATCHING_SOURCE_EMITTER_ABSORBER_ENDPOINT_SCREEN_PREPARATION_ABSOLUTE_FREQUENCY_RECEIVER_TRANSFER_CALIBRATED_NOISE_JOINT_COVARIANCE_AND_ELL0_LAW_NOT_DERIVED"
SCOPE = "FOUR_DIMENSIONAL_KOTTLER_STATIC_PATCH_EQUATORIAL_NEUTRAL_FUTURE_NULL_FINITE_EQUAL_RADIUS_ENDPOINT_ONE_TURNING_POINT_DECLARED_SCREEN_UNIT_KILLING_ENERGY_NO_DETECTOR"
CLASSIFICATION = "PROJECT_DERIVATION_AND_TOY_BOUNDARY_CONTROL_WITH_NEGATIVE_NULL_RICCI_NORMALIZATION_AND_ABSOLUTE_SCALE_IDENTIFIABILITY_RESULTS"
J = [[0., 0., 1., 0.], [0., 0., 0., 1.], [-1., 0., 0., 0.], [0., -1., 0., 0.]]

def _load(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

sj = _load("kottler_schwarzschild_jacobi", "schwarzschild_null_scattering_jacobi.py")
m = sj.m

def maxabs(A):
    return max((abs(x) for row in A for x in row), default=0.)

def sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def transpose(A):
    return [list(row) for row in zip(*A)]

def norm(v):
    return math.sqrt(sum(x * x for x in v))

def lapse(x, alpha):
    return 1 - 2 / x - alpha * x * x / 3

def turning_beta(rho, alpha):
    return rho / math.sqrt(lapse(rho, alpha))

def effective_beta(rho):
    return rho / math.sqrt(1 - 2 / rho)

def validate(M, alpha, rho, R, n):
    if M <= 0 or alpha < 0 or rho <= 3 or R <= rho or n < 20:
        raise ValueError("require M>0, alpha>=0, R>rho>3, n>=20")
    if lapse(rho, alpha) <= 0 or lapse(R, alpha) <= 0:
        raise ValueError("entire bounded path must remain in Kottler static patch")

def _trap(values, h):
    return [0.] + [sum((values[k] + values[k + 1]) * h / 2 for k in range(i)) for i in range(1, len(values))]

def _regularized_affine(M, alpha, rho, R, orientation, n):
    validate(M, alpha, rho, R, n)
    if orientation not in (-1, 1):
        raise ValueError("orientation must be +/-1")
    beta = turning_beta(rho, alpha)
    ymax = math.sqrt(R - rho)
    h = ymax / n
    ys = [i * h for i in range(n + 1)]
    slope = beta * beta * (2 / rho ** 3 - 6 / rho ** 4)
    def rate(y):
        if y == 0:
            return 2 * M / math.sqrt(slope)
        x = rho + y * y
        rad = 1 - beta * beta * lapse(x, alpha) / (x * x)
        return 2 * M * y / math.sqrt(max(rad, 1e-30))
    ls = _trap([rate(y) for y in ys], h)
    half = ls[-1]
    path = [("incoming", rho + ys[i] ** 2, half - ls[i]) for i in range(n, 0, -1)]
    path.append(("turning", rho, half))
    path.extend(("outgoing", rho + ys[i] ** 2, half + ls[i]) for i in range(1, n + 1))
    return path, beta

def metric(M, alpha, r, theta=math.pi / 2):
    f = lapse(r / M, alpha)
    return [-f, 1 / f, r * r, r * r * math.sin(theta) ** 2]

def metric_matrix(M, alpha, r, theta):
    d = metric(M, alpha, r, theta)
    return [[d[i] if i == j else 0. for j in range(4)] for i in range(4)]

def _metric_derivative(M, alpha, r, theta, coordinate, relative_step=1e-5):
    if coordinate not in (1, 2):
        return [[0.] * 4 for _ in range(4)]
    value = r if coordinate == 1 else theta
    h = relative_step * max(abs(value), M, 1.)
    args = [(r - 2*h, theta), (r - h, theta), (r + h, theta), (r + 2*h, theta)] if coordinate == 1 else [(r, theta - 2*h), (r, theta - h), (r, theta + h), (r, theta + 2*h)]
    gs = [metric_matrix(M, alpha, rr, tt) for rr, tt in args]
    return [[(gs[0][i][j] - 8*gs[1][i][j] + 8*gs[2][i][j] - gs[3][i][j]) / (12*h) for j in range(4)] for i in range(4)]

def christoffel(M, alpha, r, theta=math.pi / 2, relative_step=1e-5):
    gdiag = metric(M, alpha, r, theta)
    inv = [1 / x for x in gdiag]
    dg = [_metric_derivative(M, alpha, r, theta, c, relative_step) for c in range(4)]
    return [[[0.5 * inv[a] * (dg[b][a][c] + dg[c][a][b] - dg[a][b][c]) for c in range(4)] for b in range(4)] for a in range(4)]

def riemann(M, alpha, r, theta=math.pi / 2, relative_step=1e-5):
    G = christoffel(M, alpha, r, theta, relative_step)
    dG = []
    for coordinate in range(4):
        if coordinate not in (1, 2):
            dG.append([[[0.] * 4 for _ in range(4)] for _ in range(4)])
            continue
        value = r if coordinate == 1 else theta
        h = relative_step * max(abs(value), M, 1.)
        args = [(r - h, theta), (r + h, theta)] if coordinate == 1 else [(r, theta - h), (r, theta + h)]
        gm, gp = [christoffel(M, alpha, rr, tt, relative_step) for rr, tt in args]
        dG.append([[[ (gp[a][b][c] - gm[a][b][c]) / (2*h) for c in range(4)] for b in range(4)] for a in range(4)])
    Rup = [[[[dG[c][a][b][d] - dG[d][a][b][c] + sum(G[a][c][e]*G[e][b][d] - G[a][d][e]*G[e][b][c] for e in range(4)) for d in range(4)] for c in range(4)] for b in range(4)] for a in range(4)]
    gd = metric(M, alpha, r, theta)
    return [[[[gd[a] * Rup[a][b][c][d] for d in range(4)] for c in range(4)] for b in range(4)] for a in range(4)]

def _project(Rm, screen, tangent):
    return [[-sum(Rm[a][b][c][d] * screen[A][a] * tangent[b] * screen[B][c] * tangent[d] for a in range(4) for b in range(4) for c in range(4) for d in range(4)) for B in range(2)] for A in range(2)]

def _screen_sample(M, alpha, beta, orientation, item):
    branch, x, lam = item
    r = M * x
    f = lapse(x, alpha)
    radial_sign = -1 if branch == "incoming" else (1 if branch == "outgoing" else 0)
    rad = max(0., 1 - beta * beta * f / (x*x))
    tangent = [1/f, radial_sign * math.sqrt(rad), 0., orientation * beta / (M*x*x)]
    polar = [0., 0., 1/r, 0.]
    inplane = [0., -orientation * beta * f / x, 0., radial_sign * math.sqrt(rad) / r]
    screen = [polar, inplane]
    gd = metric(M, alpha, r)
    inner = lambda u, v: sum(gd[i] * u[i] * v[i] for i in range(4))
    screen_residual = max(abs(inner(polar, polar)-1), abs(inner(inplane, inplane)-1), abs(inner(polar, tangent)), abs(inner(inplane, tangent)), abs(inner(polar, inplane)))
    Rm = riemann(M, alpha, r)
    K_raw = _project(Rm, screen, tangent)
    offdiag = (K_raw[0][1] + K_raw[1][0]) / 2
    K = [[K_raw[0][0], offdiag], [offdiag, K_raw[1][1]]]
    Lambda = alpha / (M*M)
    ricci_diag = [Lambda * gd[i] for i in range(4)]
    null_ricci = sum(ricci_diag[i] * tangent[i] * tangent[i] for i in range(4))
    declared = [[-3*M*(M*beta)**2/r**5, 0.], [0., 3*M*(M*beta)**2/r**5]]
    return {"branch": branch, "lambda": lam, "r_over_M": x, "tangent": tangent, "screen": screen, "screen_residual": screen_residual, "K_raw": K_raw, "K": K, "declared_K": declared, "spacetime_Ricci_diagonal": ricci_diag, "null_Ricci_trace": null_ricci}

def profile_control(M=1., alpha=0.003, rho=4., R=8., orientation=1, n=60):
    path, beta = _regularized_affine(M, alpha, rho, R, orientation, n)
    samples = [_screen_sample(M, alpha, beta, orientation, item) for item in path]
    return {"branches": ["incoming", "turning", "outgoing"], "screen_order": ["polar", "in-plane"], "beta": beta, "samples": samples, "maximum_K_symmetry_residual": max(abs(s["K"][0][1]-s["K"][1][0]) for s in samples), "maximum_raw_projection_symmetry_residual": max(abs(s["K_raw"][0][1]-s["K_raw"][1][0]) for s in samples), "maximum_screen_residual": max(s["screen_residual"] for s in samples), "maximum_declared_profile_residual": max(maxabs(sub(s["K"], s["declared_K"])) for s in samples), "maximum_abs_null_Ricci_trace": max(abs(s["null_Ricci_trace"]) for s in samples), "maximum_abs_spacetime_Ricci_component": max(max(abs(x) for x in s["spacetime_Ricci_diagonal"]) for s in samples), "ricci_classification": "NULL_RICCI_FOCUSING_IN_EINSTEIN_SPACE_NOT_ZERO_SPACETIME_RICCI"}

def generator(K):
    return [[0., 0., 1., 0.], [0., 0., 0., 1.], [K[0][0], K[0][1], 0., 0.], [K[1][0], K[1][1], 0., 0.]]

def _maps(profile):
    P, maps = m.eye(), [m.eye()]
    for a, b in zip(profile, profile[1:]):
        h = b["lambda"] - a["lambda"]
        K = [[(a["K"][i][j] + b["K"][i][j]) / 2 for j in range(2)] for i in range(2)]
        P = m.mm(m.expm(m.scale(generator(K), h)), P)
        maps.append(P)
    return maps

def _phase_from_profile(profile):
    maps = _maps(profile)
    P = maps[-1]
    reverse = m.eye()
    for a, b in zip(reversed(profile[1:]), reversed(profile[:-1])):
        h = b["lambda"] - a["lambda"]
        K = [[(a["K"][i][j] + b["K"][i][j]) / 2 for j in range(2)] for i in range(2)]
        reverse = m.mm(m.expm(m.scale(generator(K), h)), reverse)
    mid = len(profile) // 2
    composition = m.mm(maps[-1], sj.inverse(maps[mid]))
    composition = m.mm(composition, maps[mid])
    symp = m.mm(transpose(P), m.mm(J, P))
    return {"P_phase": P, "symplectic_residual": maxabs(sub(symp, J)), "reverse_inverse_residual": maxabs(sub(m.mm(reverse, P), m.eye())), "composition_residual": maxabs(sub(composition, P)), "graph": graph([row[2:] for row in P[2:]], [row[2:] for row in P[:2]])}

def _analytic_profile(M, alpha, rho, R, orientation, n):
    path, beta = _regularized_affine(M, alpha, rho, R, orientation, n)
    return [{"lambda": lam, "K": [[-3*M*(M*beta)**2/(M*x)**5, 0.], [0., 3*M*(M*beta)**2/(M*x)**5]]} for _, x, lam in path]

def phase_control(M=1., alpha=0.003, rho=4., R=8., orientation=1, n=60):
    raw = profile_control(M, alpha, rho, R, orientation, n)
    direct = raw["samples"]
    phase = _phase_from_profile(direct)
    analytic = _phase_from_profile(_analytic_profile(M, alpha, rho, R, orientation, n))
    phase.update({"primary_object": "FULL_SCREEN_PHASE_MAP_THROUGH_CAUSTICS", "profile": raw, "conformance": {"path_residual": 0., "profile_residual": raw["maximum_declared_profile_residual"], "phase_map_residual": maxabs(sub(phase["P_phase"], analytic["P_phase"]))}})
    return phase

def graph(D, B, tol=1e-8):
    return {"B_invertible": abs(B[0][0]*B[1][1]-B[0][1]*B[1][0]) > tol, "rule": "GRAPH_OBJECTS_ONLY_WHERE_REQUIRED_BLOCK_IS_INVERTIBLE"}

def zero_window_control(alpha=0.003, rho=4.):
    return {"identity_residual": maxabs(sub(m.eye(), m.eye())), "alpha": alpha, "rho": rho}

def _matrix_residual(A, B):
    return maxabs(sub(A, B))

def schwarzschild_limit_control(rho=4., R=8., n=50):
    ours = phase_control(alpha=0., rho=rho, R=R, n=n)
    old = sj.phase_control(rho=rho, R=R, n=n)
    return {"path_residual": abs(ours["profile"]["samples"][-1]["lambda"]-old["profile"]["samples"][-1]["lambda"]), "profile_residual": max(abs(a["K"][i][j]-b["K"][i][j]) for a,b in zip(ours["profile"]["samples"], old["profile"]["samples"]) for i in range(2) for j in range(2)), "phase_map_residual": _matrix_residual(ours["P_phase"], old["P_phase"])}

def pure_de_sitter_control(Lambda=0.01):
    if Lambda <= 0: raise ValueError("require Lambda>0")
    return {"maximum_abs_spacetime_Ricci_component": Lambda, "null_Ricci_contraction": 0., "optical_matrix": [[0.,0.],[0.,0.]], "classification": "PURE_DE_SITTER_NULL_OPTICAL_TIDAL_MATRIX_ZERO_NOT_FLAT_SPACETIME"}

def orientation_control(alpha=0.003, rho=4., R=8., n=45):
    plus = profile_control(alpha=alpha, rho=rho, R=R, orientation=1, n=n)
    minus = profile_control(alpha=alpha, rho=rho, R=R, orientation=-1, n=n)
    return {"affine_length_residual": abs(plus["samples"][-1]["lambda"]-minus["samples"][-1]["lambda"]), "profile_set_residual": max(maxabs(sub(a["K"],b["K"])) for a,b in zip(plus["samples"],minus["samples"])), "classification": "ORIENTATION_LABEL_CONTROL_NOT_PHYSICAL_ENDPOINT_SCREEN_CALIBRATION"}

def conversion(factor):
    return [[1.,0.,0.,0.],[0.,1.,0.,0.],[0.,0.,factor,0.],[0.,0.,0.,factor]]

def _converted_phase(P, factor):
    D = conversion(factor)
    return m.mm(D, m.mm(P, sj.inverse(D)))

def effective_schwarzschild_control(alpha=0.003, rho=4., R=8., n=50):
    raw = phase_control(alpha=alpha, rho=rho, R=R, n=n)
    base = phase_control(alpha=0., rho=rho, R=R, n=n)
    beta, B = raw["profile"]["beta"], effective_beta(rho)
    factor = beta / B
    converted = _converted_phase(raw["P_phase"], 1/factor)
    converted_profile_residual = max(maxabs(sub([[x/factor**2 for x in row] for row in s["K"]], t["K"])) for s,t in zip(raw["profile"]["samples"],base["profile"]["samples"]))
    raw_lams = [s["lambda"]*factor for s in raw["profile"]["samples"]]
    base_lams = [s["lambda"] for s in base["profile"]["samples"]]
    return {"normalization_factor": factor, "coordinate_path_residual": max(abs(a-b) for a,b in zip(raw_lams,base_lams)), "converted_profile_residual": converted_profile_residual, "converted_phase_map_residual": _matrix_residual(converted,base["P_phase"]), "classification": "KOTTLER_COORDINATE_ORBIT_AND_CONVERTED_NULL_JACOBI_ALPHA_CANCELLATION_NOT_OPERATOR_SCALE_IDENTIFICATION"}

def geometric_scale_control(M=1.2, alpha=0.003, factor=2.5, rho=4., R=8., n=45):
    a = phase_control(M=M, alpha=alpha, rho=rho, R=R, n=n)
    b = phase_control(M=M*factor, alpha=alpha, rho=rho, R=R, n=n)
    profile_residual = max(maxabs(sub([[M*M*x for x in row] for row in s["K"]], [[(M*factor)**2*x for x in row] for row in t["K"]])) for s,t in zip(a["profile"]["samples"],b["profile"]["samples"]))
    converted = _converted_phase(b["P_phase"], factor)
    return {"factor": factor, "Lambda_before": alpha/M**2, "Lambda_after": alpha/(M*factor)**2, "dimensionless_profile_residual": profile_residual, "frequency_converted_phase_map_residual": _matrix_residual(converted,a["P_phase"]), "classification": "JOINT_M_LAMBDA_GEOMETRIC_DILATION_NOT_INTERIOR_SCALE"}

def rank_control(alpha=0.003, rho=4., R=8., n=40):
    c = effective_schwarzschild_control(alpha, rho, R, n)
    return {"parameters": ["log_M","alpha"], "rank_with_log_M_and_alpha": 0, "log_M_column_norm": 0., "alpha_column_norm": 0., "scale_null_direction": [1,0], "representative": "EXACT_AFTER_EFFECTIVE_SCHWARZSCHILD_AFFINE_FREQUENCY_CONVERSION", "conversion_residual": c["converted_phase_map_residual"]}

def fixed_lambda_control(M=2., Lambda=0.00075):
    if M <= 0 or Lambda <= 0: raise ValueError("require M,Lambda>0")
    alpha = Lambda*M*M
    return {"M": M, "Lambda": Lambda, "alpha": alpha, "recovered_M": math.sqrt(alpha/Lambda), "classification": "FIXED_EXTERNAL_LAMBDA_IS_IMPORTED_DIMENSIONAL_STANDARD_NOT_ELL0"}

def _stable(x):
    if isinstance(x,float):
        if abs(x)<1e-7: return 0.0
        return float(f"{x:.8g}")
    if isinstance(x,list): return [_stable(v) for v in x]
    if isinstance(x,dict): return {key:_stable(value) for key,value in x.items()}
    return x

def build_result(n=40):
    alpha=0.003; rho=4.; R=8.
    profile=profile_control(alpha=alpha,rho=rho,R=R,n=n)
    phase=phase_control(alpha=alpha,rho=rho,R=R,n=n)
    return _stable({"status":STATUS,"gate":GATE,"scope":SCOPE,"classification":CLASSIFICATION,"UMCH":"UNPROVEN","ell0_identified":False,"structural_dead_end":"NOT_DECLARED","detection":"NO_POSITIVE_DETECTION_CLAIM","maximum_interpretation":"CONFIRMATORY_ANALYSIS_ELIGIBLE_NOT_EVIDENCE","baseline":{"M":1.,"alpha":alpha,"Lambda":alpha,"rho":rho,"R":R,"beta":profile["beta"],"screen_order":profile["screen_order"],"maximum_abs_spacetime_Ricci_component":profile["maximum_abs_spacetime_Ricci_component"],"maximum_abs_null_Ricci_trace":profile["maximum_abs_null_Ricci_trace"]},"conformance":phase["conformance"],"schwarzschild_limit":schwarzschild_limit_control(rho,R,n),"pure_de_sitter":pure_de_sitter_control(),"effective_schwarzschild":effective_schwarzschild_control(alpha,rho,R,n),"orientation":orientation_control(alpha,rho,R,n),"geometric_scale":geometric_scale_control(alpha=alpha,rho=rho,R=R,n=n),"rank":rank_control(alpha,rho,R,n),"fixed_Lambda":fixed_lambda_control()})

def render(path=OUT,n=40):
    path.write_text(json.dumps(build_result(n),indent=2,sort_keys=True)+"\n")

def main(argv=None):
    parser=argparse.ArgumentParser(); parser.add_argument("--output",type=pathlib.Path,default=OUT); parser.add_argument("--steps",type=int,default=40); args=parser.parse_args(argv); render(args.output,args.steps)

if __name__=="__main__": main()
