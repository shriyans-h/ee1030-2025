#include <stdio.h>
#include <math.h>

// Step 0: helper for 2x2 matrix multiplication: C = D^(-1/2) G D^(-1/2)
void matmul(double A[2][2], double B[2][2], double C[2][2]) {
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            C[i][j] = 0.0;
            for (int k = 0; k < 2; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

// Step 1: Construct Gram matrix from two vectors
void gram_matrix(double *u, double *v, int n, double G[2][2]) {
    double g11 = 0.0, g22 = 0.0, g12 = 0.0;
    for (int i = 0; i < n; i++) {
        g11 += u[i] * u[i];
        g22 += v[i] * v[i];
        g12 += u[i] * v[i];
    }
    G[0][0] = g11;
    G[0][1] = g12;
    G[1][0] = g12;
    G[1][1] = g22;
}

// Step 2: Normalize Gram matrix → G_norm = D^(-1/2) * G * D^(-1/2)
void normalize_gram(double G[2][2], double G_norm[2][2]) {
    double d11 = 1.0 / sqrt(G[0][0]);
    double d22 = 1.0 / sqrt(G[1][1]);

    double Dinv[2][2] = {{d11, 0.0}, {0.0, d22}};

    double temp[2][2];
    matmul(Dinv, G, temp);      // temp = D^(-1/2) * G
    matmul(temp, Dinv, G_norm); // G_norm = temp * D^(-1/2)
}

// Step 3: Extract angle from normalized Gram matrix
double angle_from_normalized(double G_norm[2][2]) {
    // off-diagonal entry
    double cos_theta = G_norm[0][1]; 
    // numerical safety
    if (cos_theta > 1.0) {
        cos_theta = 1.0; 
    }
    if (cos_theta < -1.0) {
        cos_theta = -1.0;
    }
    return acos(cos_theta);
}
