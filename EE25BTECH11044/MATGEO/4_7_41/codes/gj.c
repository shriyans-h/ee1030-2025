#include <stdio.h>
#include <math.h>

#define ROWS 4
#define COLS 5   // 4 variables + 1 RHS

// Function to perform Gaussian elimination to RREF
void gaussJordan(double mat[ROWS][COLS]) {
    int i, j, k;
    for (i = 0; i < ROWS; i++) {
        // Make the pivot element = 1
        double pivot = mat[i][i];
        if (pivot != 0) {
            for (j = 0; j < COLS; j++) {
                mat[i][j] /= pivot;
            }
        }
        // Eliminate all other entries in column i
        for (k = 0; k < ROWS; k++) {
            if (k != i) {
                double factor = mat[k][i];
                for (j = 0; j < COLS; j++) {
                    mat[k][j] -= factor * mat[i][j];
                }
            }
        }
    }
}

int main() {
    // Augmented matrix for system in variables (x,y,z,lambda)
    double mat[ROWS][COLS] = {
        { 1,  0,  0, -1, -5},   // x - λ = -5
        { 0,  1,  0, -4, -3},   // y - 4λ = -3
        { 0,  0,  1,  9,  6},   // z + 9λ = 6
        {-1, -4,  9,  0, -27}   // -x - 4y + 9z = -27
    };

    gaussJordan(mat);

    double x = mat[0][4];
    double y = mat[1][4];
    double z = mat[2][4];
    double lambda = mat[3][4];

    printf("Solution: x = %.2f, y = %.2f, z = %.2f, lambda = %.2f\n", x, y, z, lambda);

    // Given point P(2,4,-1)
    double px = 2, py = 4, pz = -1;

    // Distance between P and Q(x,y,z)
    double dist = sqrt((px - x)*(px - x) + (py - y)*(py - y) + (pz - z)*(pz - z));

    printf("Distance = %.2f\n", dist);

    return 0;
}
