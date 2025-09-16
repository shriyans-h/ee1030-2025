#include <stdio.h>

int main() {
    // Input: two points (x1,y1), (x2,y2)
    double x1 = 2, y1 = -3;
    double x2 = 4, y2 = -5;

    // Step 1: Direction vector m = (x2-x1, y2-y1)
    double m1 = x2 - x1;
    double m2 = y2 - y1;

    // Step 2: Find normal vector n = (n1,n2)
    // Condition: n^T * m = 0  => n1*m1 + n2*m2 = 0
    // One valid solution is n = (m2, -m1)
    double n1 = m2;
    double n2 = -m1;

    // Step 3: Find c using point (x1,y1)
    double c = n1*x1 + n2*y1;

    // Final line equation: n1*x + n2*y = c
    printf("Equation of line: %.2lf*x + %.2lf*y = %.2lf\n", n1, n2, c);

    return 0;
}
