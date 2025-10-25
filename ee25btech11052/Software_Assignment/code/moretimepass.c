// Compute transpose of matrix

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct
{
    int rows;
    int cols;
    double **data;
} Matrix;

Matrix transpose(Matrix A)
{
    Matrix T = createMatrix(A.cols, A.rows);
    for (int i = 0; i < A.rows; i++)
    {
        for (int j = 0; j < A.cols; j++)
        {
            T.data[j][i] = A.data[i][j];
        }
    }
    return T;
}

// Multiply two matrices: C = A * B
Matrix multiply(Matrix A, Matrix B)
{
    if (A.cols != B.rows)
    {
        fprintf(stderr, "Error: Matrix dimension mismatch for multiplication\n");
        exit(1);
    }
    Matrix C = createMatrix(A.rows, B.cols);
    for (int i = 0; i < A.rows; i++)
    {
        for (int j = 0; j < B.cols; j++)
        {
            // C.data[i][j] is already 0 from calloc
            for (int k = 0; k < A.cols; k++)
            {
                C.data[i][j] += A.data[i][k] * B.data[k][j];
            }
        }
    }
    return C;
}

// Compute B = A_transpose * A
Matrix At_multiply_A(Matrix A)
{
    Matrix At = transpose(A);
    Matrix AtA = multiply(At, A);
    freeMatrix(At);
    return AtA;
}

// Copy matrix B = A
Matrix copyMatrix(Matrix A)
{
    Matrix B = createMatrix(A.rows, A.cols);
    for (int i = 0; i < A.rows; i++)
    {
        for (int j = 0; j < A.cols; j++)
        {
            B.data[i][j] = A.data[i][j];
        }
    }
    return B;
}