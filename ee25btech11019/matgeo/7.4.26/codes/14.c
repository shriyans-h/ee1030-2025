#include <stdio.h>
#include <math.h>

// Function to get circle center (cx, cy) and radius r for given p, q
void circle_params(float p, float q, float *cx, float *cy, float *r) {
    // Equation: x^2 + y^2 = px + qy
    // Rewrite: (x - p/2)^2 + (y - q/2)^2 = (p^2 + q^2)/4
    *cx = p / 2.0;
    *cy = q / 2.0;
    *r = sqrt((p*p + q*q) / 4.0);
}

// Function to compare p^2 and 8q^2
int compare_pq(float p, float q) {
    float left = p*p;
    float right = 8*q*q;

    if (fabs(left - right) < 1e-3)
        return 0;   // equal
    else if (left < right)
        return -1;  // p^2 < 8q^2
    else
        return 1;   // p^2 > 8q^2
}