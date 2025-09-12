#include <stdio.h>

#define ROWS 3
#define COLS 3

void row_echelon_form(double A[ROWS][COLS]) {
    int pivot_row = 0;

    for (int pivot_col = 0; pivot_col < COLS; pivot_col++) {
        int pivot = -1;
        for (int r = pivot_row; r < ROWS; r++) {
            if (A[r][pivot_col] != 0.0) {
                pivot = r;
                break;
            }
        }
        if (pivot == -1) continue;

        if (pivot != pivot_row) {
            for (int c = 0; c < COLS; c++) {
                double tmp = A[pivot_row][c];
                A[pivot_row][c] = A[pivot][c];
                A[pivot][c] = tmp;
            }
        }

        for (int r = pivot_row + 1; r < ROWS; r++) {
            if (A[r][pivot_col] != 0.0) {
                double factor = A[r][pivot_col] / A[pivot_row][pivot_col];
                for (int c = pivot_col; c < COLS; c++) {
                    A[r][c] -= factor * A[pivot_row][c];
                }
            }
        }
        pivot_row++;
        if (pivot_row == ROWS) break;
    }
}

void solve_ref(double *out) {
    double A[ROWS][COLS] = {
        {2, 3, 7},
        {6, 4, 7},
        {4, 6, 14}
    };

    row_echelon_form(A);

    int k = 0;
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            out[k++] = A[i][j];
        }
    }
}

