#include <stdio.h>

// Function to compute square root using Newton-Raphson method
double my_sqrt(double n) {
    if(n == 0) return 0;
    double x = n;      // initial guess
    double y = 1.0;
    double eps = 1e-6; // desired precision

    while(x - y > eps) {
        x = (x + y) / 2;
        y = n / x;
    }
    return x;
}

int main() {
    // Coordinates of points A, B, C
    double A[3] = {1, 2, 3};
    double B[3] = {2, -1, 4};
    double C[3] = {4, 5, -1};

    // Compute vectors AB and AC
    double AB[3], AC[3];
    for(int i = 0; i < 3; i++) {
        AB[i] = B[i] - A[i];
        AC[i] = C[i] - A[i];
    }

    // Compute cross product AB x AC
    double cross[3];
    cross[0] = AB[1]*AC[2] - AB[2]*AC[1];
    cross[1] = AB[2]*AC[0] - AB[0]*AC[2];
    cross[2] = AB[0]*AC[1] - AB[1]*AC[0];

    // Compute magnitude of cross product using my_sqrt
    double magnitude = my_sqrt(cross[0]*cross[0] + cross[1]*cross[1] + cross[2]*cross[2]);

    // Area of triangle = 1/2 * |AB x AC|
    double area = 0.5 * magnitude;

    printf("Area of triangle ABC = %.5f\n", area);

    return 0;
}
