#include <stdio.h>
#include <math.h>
#include <stdbool.h>

#define SIZE 3
#define EPS 1e-9  // tolerance for floating-point comparison

// Function to build matrix f(theta)
void f(double theta, double M[SIZE][SIZE]) {
    M[0][0] = cos(theta);  M[0][1] = -sin(theta); M[0][2] = 0;
    M[1][0] = sin(theta);  M[1][1] =  cos(theta); M[1][2] = 0;
    M[2][0] = 0;           M[2][1] = 0;           M[2][2] = 1;
}

// Multiply two 3x3 matrices
void multiply(double A[SIZE][SIZE], double B[SIZE][SIZE], double C[SIZE][SIZE]) {
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            C[i][j] = 0;
            for (int k = 0; k < SIZE; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

// Check if two matrices are approximately equal
bool equal(double A[SIZE][SIZE], double B[SIZE][SIZE]) {
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            if (fabs(A[i][j] - B[i][j]) > EPS)
                return false;
        }
    }
    return true;
}

// Print a 3x3 matrix
void printMatrix(double M[SIZE][SIZE]) {
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            printf("%10.6f ", M[i][j]);
        }
        printf("\n");
    }
}

int main() {
    double alpha, beta;
    printf("Enter alpha (in radians): ");
    scanf("%lf", &alpha);
    printf("Enter beta (in radians): ");
    scanf("%lf", &beta);

    double F_alpha[SIZE][SIZE], F_minus_beta[SIZE][SIZE], F_alpha_minus_beta[SIZE][SIZE];
    double lhs[SIZE][SIZE], rhs[SIZE][SIZE];

    // Build matrices
    f(alpha, F_alpha);
    f(-beta, F_minus_beta);
    f(alpha - beta, F_alpha_minus_beta);

    // Compute lhs = f(alpha) * f(-beta)
    multiply(F_alpha, F_minus_beta, lhs);

    // rhs = f(alpha - beta)
    for (int i = 0; i < SIZE; i++)
        for (int j = 0; j < SIZE; j++)
            rhs[i][j] = F_alpha_minus_beta[i][j];

    // Compare
    if (equal(lhs, rhs)) {
        printf("\n Verified: f(alpha) f(-beta) = f(alpha - beta)\n");
    } else {
        printf("\nNot equal!\n");
        printf("\nLHS =\n"); printMatrix(lhs);
        printf("\nRHS =\n"); printMatrix(rhs);
    }

    return 0;
}

