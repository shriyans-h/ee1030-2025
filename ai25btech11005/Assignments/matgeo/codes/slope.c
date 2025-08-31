#include <stdio.h>

int main() {
    // Points P(x1, y1) and Q(x2, y2)
    float x1 = 3, y1 = -2;
    float x2 = -1, y2 = 4;

    // Direction ratios (l, m)
    float l = x2 - x1;
    float m = y2 - y1;

    printf("For P(%.2f, %.2f) and Q(%.2f, %.2f):\n", x1, y1, x2, y2);
    printf("Direction ratios (l, m) = (%.2f, %.2f)\n", l, m);

    // Slope = m / l  (if l != 0)
    if(l != 0) {
        float slope = m / l;
        printf("Slope = %.2f\n", slope);
    } else {
        printf("Slope is undefined (vertical line).\n");
    }

    return 0;
}
