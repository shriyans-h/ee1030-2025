#include <stdio.h>
int main() {
    // Intercept points
    double A[2] = {-3, 0};   // x-intercept (-3,0)
    double B[2] = {0, 2};    // y-intercept (0,2)

    // Direction vector m = A - B
    double m[2];
    m[0] = A[0] - B[0];
    m[1] = A[1] - B[1];

    printf("Direction vector m = (%.2f, %.2f)\n", m[0], m[1]);

    // Normal vector n (perpendicular to m)
    double n[2];
    n[0] = -m[1];   // -y
    n[1] = m[0];    // x

    printf("Normal vector n = (%.2f, %.2f)\n", n[0], n[1]);

    // Point h (we take y-intercept B as reference point)
    double h[2] = {0, 2};

    // Equation: n^T * (x - h) = 0
    // Expanding: n^T * x = n^T * h
    double c = n[0]*h[0] + n[1]*h[1];

    printf("Equation of line: %.2fx + %.2fy = %.2f\n", n[0], n[1], c);

    return 0;
}
