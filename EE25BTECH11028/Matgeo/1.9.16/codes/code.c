#include <stdio.h>
#include <math.h>

int main() {
    int A_x = -2, A_y = 0;
    int B_x = 6, B_y = 0;
    int P_x1, P_x2;

    // Based on |x + 2| = |x - 6|, two cases arise:
    // Case 1: x + 2 = x - 6 (not possible)
    // Case 2: x + 2 = -(x - 6)

    // Case 2 calculation:
    P_x1 = (6 - 2) / 2; // x = 2
    P_x2 = 2; // Only one valid solution as per the problem.

    printf("Coordinates of point P are: (%d, 0)\n", P_x2);

    return 0;
}
