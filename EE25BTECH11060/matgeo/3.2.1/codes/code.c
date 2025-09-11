#include <stdio.h>
#include <math.h>

int main() {
    // Given distances (according to your solution)
    double AC = 9.0, BC = 6.0;
    double AB = 4.0;

    // Fix A and B
    double Ax = 0.0, Ay = 0.0;
    double Bx = 4.0, By = 0.0;

    // Step 1: Find x using the relation (from your derivation)
    // 2 * B^T * C = AC^2 + B^T B - BC^2
    double x = (AC*AC + (Bx*Bx + By*By) - BC*BC) / (2 * Bx);

    // Step 2: Use AC^2 = x^2 + y^2 to solve for y
    double y_square = AC*AC - x*x;

    if (y_square < 0) {
        printf("No real solution (triangle inequality violated).\n");
        return 0;
    }

    double y1 = sqrt(y_square);
    double y2 = -sqrt(y_square);

    // Print results
    printf("Coordinates of A: (%.3f, %.3f)\n", Ax, Ay);
    printf("Coordinates of B: (%.3f, %.3f)\n", Bx, By);
    printf("Possible coordinates of C:\n");
    printf("C1 = (%.3f, %.3f)\n", x, y1);
    printf("C2 = (%.3f, %.3f)\n", x, y2);

    return 0;
}
