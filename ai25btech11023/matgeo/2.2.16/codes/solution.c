#include <stdio.h>
#include <stdlib.h>
#include "geofun.h"
#include "matfun.h"

int main() {
    // Plane 1 normal: (2, -3, 1), constant: -1
    double **n1 = createMat(3, 1);
    n1[0][0] = 2; n1[1][0] = -3; n1[2][0] = 1;
    double d1 = -1;

    // Plane 2 normal: (1, -1, 0), constant: -4
    double **n2 = createMat(3, 1);
    n2[0][0] = 1; n2[1][0] = -1; n2[2][0] = 0;
    double d2 = -4;

    // Compute dot product and norms
    double dot = Matdot(n1, n2, 3);
    double norm1 = Matnorm(n1, 3);
    double norm2 = Matnorm(n2, 3);
    double cos_theta = dot / (norm1 * norm2);

    // Write space-separated values to output.dat
    FILE *fp = fopen("output.dat", "w");
    if (fp == NULL) {
        printf("Error opening output.dat\n");
        return -1;
    }
    // Format: n1_x n1_y n1_z d1 n2_x n2_y n2_z d2 cos_theta (all space-separated)
    fprintf(fp, "%lf %lf %lf %lf %lf %lf %lf %lf %lf\n",
            n1[0][0], n1[1][0], n1[2][0], d1,
            n2[0][0], n2[1][0], n2[2][0], d2,
            cos_theta);
    fclose(fp);

    freeMat(n1, 3);
    freeMat(n2, 3);

    return 0;
}
