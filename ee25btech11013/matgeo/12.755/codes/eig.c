#include <stdio.h>
#include <math.h>

#define N 3

// Function to print a matrix
void print_matrix(double A[N][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%8.3f ", A[i][j]);
        }
        printf("\n");
    }
}

// Function to compute B = A - λI
void subtract_lambda_identity(double A[N][N], double B[N][N], double lambda) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (i == j)
                B[i][j] = A[i][j] - lambda;
            else
                B[i][j] = A[i][j];
        }
    }
}

// Function to check if λ = 1 is approximately an eigenvalue (det ~ 0)
double determinant(double A[N][N]) {
    double det =
        A[0][0]*(A[1][1]*A[2][2] - A[1][2]*A[2][1]) -
        A[0][1]*(A[1][0]*A[2][2] - A[1][2]*A[2][0]) +
        A[0][2]*(A[1][0]*A[2][1] - A[1][1]*A[2][0]);
    return det;
}

// Exposed function to be called from Python
void process_matrix(double A[N][N], double B[N][N], double lambda) {
    printf("Matrix A:\n");
    print_matrix(A);
    printf("\n---------------------------------\n");

    double detA = determinant(A);
    printf("Determinant of A = %.3f\n", detA);

    subtract_lambda_identity(A, B, lambda);
    printf("\nMatrix (A - %.2fI):\n", lambda);
    print_matrix(B);

    double detB = determinant(B);
    printf("\nDeterminant of (A - %.2fI) = %.3f\n", lambda, detB);
    if (fabs(detB) > 1e-6)
        printf("\nλ = %.2f is NOT an eigenvalue of A.\n", lambda);
    else
        printf("\nλ = %.2f is an eigenvalue of A.\n", lambda);
}

