#include <stdio.h>

// Function to compute t = (v^T (P - A)) / (v^T v)
double compute_t(double P[3], double A[3], double v[3]) {
    double diff[3];
    for (int i = 0; i < 3; i++) {
        diff[i] = P[i] - A[i];
    }

    // v^T v
    double vtv = 0.0;
    for (int i = 0; i < 3; i++) {
        vtv += v[i] * v[i];
    }

    // v^T (P - A)
    double vtd = 0.0;
    for (int i = 0; i < 3; i++) {
        vtd += v[i] * diff[i];
    }

    return vtd / vtv;
}

