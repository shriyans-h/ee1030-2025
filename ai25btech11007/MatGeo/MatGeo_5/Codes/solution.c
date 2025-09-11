#include <stdio.h>
#include <math.h>

int main() {
    int s_vals[2] = {5, -11};   // possible values of s
    int p, q, r, s;
    double A = 5 * sqrt(6);     // area of triangle

    printf("Given area = %.2f\n", A);

    for (int i = 0; i < 2; i++) {
        s = s_vals[i];
        p = s + 3;   // from relation p = s+3
        q = 4;
        r = 2;

        printf("Solution %d: (p,q,r,s) = (%d,%d,%d,%d)\n", i+1, p, q, r, s);
    }

    return 0;
}
