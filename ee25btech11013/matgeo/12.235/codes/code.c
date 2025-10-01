#include <stdio.h>

int determinant(int mat[3][3]) {
    int det;
    det = mat[0][0]*(mat[1][1]*mat[2][2] - mat[1][2]*mat[2][1])
        - mat[0][1]*(mat[1][0]*mat[2][2] - mat[1][2]*mat[2][0])
        + mat[0][2]*(mat[1][0]*mat[2][1] - mat[1][1]*mat[2][0]);
    return det;
}