// triangle.c
#include <math.h>

#define PI 3.141592653589793

// Compute coordinates of point A
void compute_A(double *Ax, double *Ay) {
    double BC = 7.0;
    double angle_B = 45.0 * PI / 180.0;
    double angle_C = 60.0 * PI / 180.0;

    // Unit vectors from B and C
    double uBx = cos(angle_B);
    double uBy = sin(angle_B);
    double uCx = cos(PI - angle_C);
    double uCy = sin(PI - angle_C);

    // Solve intersection: r1(t) = r2(s)
    // From derivation: s = 14 / (sqrt(3) + 1)
    double s = 14.0 / (sqrt(3.0) + 1.0);
    double t = (sqrt(6.0) / 2.0) * s;

    // A = t * uB
    *Ax = t * uBx;
    *Ay = t * uBy;
}

