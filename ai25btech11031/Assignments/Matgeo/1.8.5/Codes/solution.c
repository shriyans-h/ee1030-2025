#include <stdio.h>

// Define a 3D vector struct
typedef struct {
    double x, y, z;
} Vector3;

// Dot product of two vectors
double dot(Vector3 v1, Vector3 v2) {
    return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z;
}

int main() {
    Vector3 A = {3, 4, 5};
    Vector3 B = {-1, 3, -7};

    // Vector sum A+B
    Vector3 AplusB = {A.x + B.x, A.y + B.y, A.z + B.z};

    // Dot products |A|^2 and |B|^2
    double A_dot = dot(A, A);
    double B_dot = dot(B, B);

    // Equation in vector form:
    // 2 * (P·P) - 2 * (A+B)·P + |A|^2 + |B|^2 = K^2
    printf("Vector form equation of locus P satisfies:\n");
    printf("2 * (P · P) - 2 * (A+B) · P + |A|^2 + |B|^2 = K^2\n");
    printf("where\n");
    printf("A + B = (%.1f, %.1f, %.1f),\n", AplusB.x, AplusB.y, AplusB.z);
    printf("|A|^2 = %.1f, |B|^2 = %.1f\n", A_dot, B_dot);

    return 0;
}
