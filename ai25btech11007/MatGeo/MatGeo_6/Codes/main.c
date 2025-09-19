#include <stdio.h>
#include <math.h>

// Custom sqrt (overrides math.h sqrt)
double sqrt(double n) {
    if (n < 0) return -1; // invalid for negative numbers
    if (n == 0) return 0;

    double guess = n / 2.0;
    for (int i = 0; i < 20; i++) { // Newton-Raphson iterations
        guess = 0.5 * (guess + n / guess);
    }
    return guess;
}

// Function to calculate dot product of two vectors
double dotProduct(double A[], double B[]) {
    return A[0]*B[0] + A[1]*B[1];
}

// Function to calculate magnitude of a vector
double magnitude(double V[]) {
    return sqrt(V[0]*V[0] + V[1]*V[1]);
}

// Function to calculate angle (in degrees) between two vectors
double angleBetweenVectors(double A[], double B[]) {
    double dot = dotProduct(A, B);
    double magA = magnitude(A);
    double magB = magnitude(B);
    double cosTheta = dot / (magA * magB);

    // Clamp cosTheta to avoid floating point domain errors
    if (cosTheta > 1.0) cosTheta = 1.0;
    else if (cosTheta < -1.0) cosTheta = -1.0;

    double angleRad = acos(cosTheta); // still uses math.h
    double angleDeg = angleRad * (180.0 / M_PI);
    return angleDeg;
}

int main() {
    // Coordinates of points
    double A[2] = {1.5625, 2.705}; // Approx values from calculation
    double B[2] = {0.0, 0.0};
    double C[2] = {5.0, 0.0};

    // Vector BA = A - B
    double BA[2] = {A[0] - B[0], A[1] - B[1]};
    // Vector BC = C - B
    double BC[2] = {C[0] - B[0], C[1] - B[1]};

    // Calculate angle at B
    double angleB = angleBetweenVectors(BA, BC);

    printf("The angle at vertex B is: %.2f degrees\n", angleB);

    // Also check side lengths
    double AB_len = magnitude(BA);
    double AC_len = sqrt((A[0] - C[0])*(A[0] - C[0]) + (A[1] - C[1])*(A[1] - C[1]));
    double BC_len = magnitude(BC);

    printf("AB = %.3f cm\n", AB_len);
    printf("AC = %.3f cm\n", AC_len);
    printf("BC = %.3f cm\n", BC_len);
    printf("AB + AC = %.3f cm\n", AB_len + AC_len);

    return 0;
}
