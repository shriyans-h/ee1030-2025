#include <stdio.h>

int main() {
    // Given values
    int xB = 2, yB = 6;
    int xC = 3, yC = -1;  // Center of the circle

    // Calculate coordinates of A using midpoint formula
    int xA = 2 * xC - xB;
    int yA = 2 * yC - yB;

    // Print result
    printf("Coordinates of point A are: (%d, %d)\n", xA, yA);

    // Verify midpoint
    float midX = (xA + xB) / 2.0;
    float midY = (yA + yB) / 2.0;
    printf("Midpoint of A and B is: (%.1f, %.1f)\n", midX, midY);

    return 0;
}