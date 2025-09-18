#include <stdio.h>
#include <math.h>

int main() {
    // Given magnitudes
    double a = 3.0;
    double b = 4.0;
    double c = 5.0;

    // Since a, b, c are mutually perpendicular:
    double sumSq = a*a + b*b + c*c;

    // Magnitude of (a+b+c)
    double result = sqrt(sumSq);

    printf("||a + b + c|| = sqrt(%.0f) = %.4f\n", sumSq, result);

    return 0;
}