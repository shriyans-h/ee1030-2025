#include <stdio.h>

int main() {
    // Coefficient matrix
    double A[2][2] = {{2, -3}, {4, -5}};
    double B[2] = {1, 1};  // RHS vector
    double det, u, v, a, b;

    // Determinant of A
    det = A[0][0]*A[1][1] - A[0][1]*A[1][0];

    if(det == 0) {
        printf("System has no unique solution.\n");
        return 0;
    }

    // Cramer's Rule
    u = (B[0]*A[1][1] - B[1]*A[0][1]) / det;
    v = (A[0][0]*B[1] - A[1][0]*B[0]) / det;

    // Recover a and b
    a = 1.0 / u;
    b = 1.0 / v;

    printf("Solution: a = %.2f, b = %.2f\n", a, b);

    return 0;
}
