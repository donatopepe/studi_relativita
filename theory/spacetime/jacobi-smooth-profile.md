# Smooth Jacobi profile moment gate

Classification: `PROJECT_DERIVATION_AND_NEGATIVE_RESULT`.

Status: `JACOBI_SMOOTH_EQUAL_INTEGRAL_DIFFERENT_WEIGHTED_ENDPOINT_NOT_ELL0`; `NO_POSITIVE_DETECTION_CLAIM`.

For `d''+epsilon f(s)d=0`, vertex data `d(0)=0,d'(0)=1`, and fixed observer `S`, first variation around zero focusing gives

`d(S)=S-epsilon int_0^S (S-t)t f(t)dt+O(epsilon^2)`.

Hence integrated optical strength alone is insufficient. Normalized smooth nonnegative profiles `f_a=1/S` and `f_b=6t(S-t)/S^3` both integrate to one, but weighted moments are `S^2/6` and `S^2/5`; first-order endpoints differ by `epsilon S^2/30`.

The weighted moment is only first-order sufficient, not an exact finite-strength statistic. Kernel `(S-t)t` is reflection symmetric, so reflected profiles collide at this order. Affine interval, vertex and observer boundary are fixed here; changing them changes kernel.

Result extends thin-lens profile dependence to smooth profiles but remains scalar perturbation theory, not exact varying-matrix Sachs propagation or spacetime observation. It contains no `ell0`; no core reformulation is triggered.
