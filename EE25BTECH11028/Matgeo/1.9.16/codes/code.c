#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main() {
    // Coordinates of points A and B
    int Ax = -2, Ay = 0;
    int Bx = 6, By = 0;

    // We know P lies on the x-axis: P = (x, 0)
    // So we'll find x such that |P - A| = |P - B|

    int x;

    // Vector subtraction magnitudes:
    // |P - A| = sqrt((x + 2)^2 + 0^2)
    // |P - B| = sqrt((x - 6)^2 + 0^2)
    // Equating:
    // |x + 2| = |x - 6|

    // Solve the absolute value equation manually:

    // Case 1: x + 2 = x - 6 => 2 = -6 → invalid
    int lhs1 = x + 2;
    int rhs1 = x - 6;

    if (lhs1 == rhs1) {
        printf("Case 1 valid, x = any value (unexpected)\n");
    } else {
        printf("Case 1: %d = %d → Not possible\n", lhs1, rhs1);
    }

    // Case 2: x + 2 = -(x - 6)
    //         x + 2 = -x + 6
    //         2x = 4 => x = 2

    x = 2;

    // Output the result
    printf("The point P that is equidistant from A and B on the x-axis is: (%d, 0)\n", x);

    // Optional: verify distances
    double distance_PA = sqrt(pow(x - Ax, 2) + pow(0 - Ay, 2));
    double distance_PB = sqrt(pow(x - Bx, 2) + pow(0 - By, 2));

    printf("Distance PA = %.2f\n", distance_PA);
    printf("Distance PB = %.2f\n", distance_PB);

    return 0;
}
