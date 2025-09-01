#include <stdio.h>

// Custom square root function using Newton-Raphson
double my_sqrt(double num) {
    if (num <= 0) return 0;
    double x = num;
    double prev = 0;
    while (x != prev) {
        prev = x;
        x = 0.5 * (x + num / x);
    }
    return x;
}

int main() {
    // A vector perpendicular to both a and b is (0,1,1)
    double n[3] = {0, 1, 1};

    // Magnitude of n using custom sqrt
    double mag = my_sqrt(n[0]*n[0] + n[1]*n[1] + n[2]*n[2]);

    // Unit vector
    double unit[3];
    for (int i = 0; i < 3; i++) {
        unit[i] = n[i] / mag;
    }

    // Output result
    printf("Unit vector perpendicular to a and b: ");
    printf("(%.6f, %.6f, %.6f)\n", unit[0], unit[1], unit[2]);

    return 0;
}
