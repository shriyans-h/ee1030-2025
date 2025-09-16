// triangle.c
#include <math.h>

#define PI 3.141592653589793

// Compute coordinates of point A using derived formula
void compute_A(double *Ax, double *Ay) {
    double a = 7.0; // BC
    double angle_B_deg = 45.0;
    double angle_C_deg = 60.0;
    double angle_A_deg = 180.0 - (angle_B_deg + angle_C_deg); // 75°

    // Convert to radians
    double angle_B = angle_B_deg * PI / 180.0;
    double angle_C = angle_C_deg * PI / 180.0;
    double angle_A = angle_A_deg * PI / 180.0;

    // Compute K using Law of Sines
    double sin_C = sin(angle_C);
    double sin_A = sin(angle_A);
    double K = (a * sin_C) / sin_A;

    // Compute c using derived formula
    double cos_B = cos(angle_B);
    double numerator = (K * K) - (a * a);
    double denominator = 2.0 * (K - a * cos_B);
    double c = numerator / denominator;

    // Compute coordinates of A using direction of angle B
    double uBx = cos(angle_B);
    double uBy = sin(angle_B);

    *Ax = c * uBx;
    *Ay = c * uBy;
}

