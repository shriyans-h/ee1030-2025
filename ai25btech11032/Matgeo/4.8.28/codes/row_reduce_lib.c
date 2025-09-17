#include <math.h>

#define EPS 1e-9

// Row reduction to Reduced Row Echelon Form (RREF)
void row_reduce(int rows, int cols, double *M) {
    int r = 0; // pivot row
    for (int c = 0; c < cols - 1 && r < rows; c++) {
        // 1. Find pivot
        int pivot = r;
        for (int i = r+1; i < rows; i++) {
            if (fabs(M[i*cols + c]) > fabs(M[pivot*cols + c])) {
                pivot = i;
            }
        }
        if (fabs(M[pivot*cols + c]) < EPS) continue;

        // 2. Swap rows if needed
        if (pivot != r) {
            for (int j = 0; j < cols; j++) {
                double tmp = M[r*cols + j];
                M[r*cols + j] = M[pivot*cols + j];
                M[pivot*cols + j] = tmp;
            }
        }

        // 3. Normalize pivot row
        double div = M[r*cols + c];
        for (int j = c; j < cols; j++) {
            M[r*cols + j] /= div;
        }

        // 4. Eliminate in all other rows
        for (int i = 0; i < rows; i++) {
            if (i == r) continue;
            double factor = M[i*cols + c];
            for (int j = c; j < cols; j++) {
                M[i*cols + j] -= factor * M[r*cols + j];
            }
        }
        r++;
    }
}

