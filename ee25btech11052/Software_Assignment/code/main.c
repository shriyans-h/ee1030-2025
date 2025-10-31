/* svd_compress.c */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <ctype.h> // <-- ADD THIS INCLUDE

typedef struct
{
    int row;
    int col;
    double **data;
} matrix;

matrix creatematrix(int row, int col)
{
    matrix m;
    m.row = row;
    m.col = col;
    m.data = (double **)malloc(row * sizeof(double *));
    if (m.data == NULL) {
        fprintf(stderr, "Error: malloc failed for matrix data\n");
        exit(1);
    }
    for (int i = 0; i < row; i++)
    {
        m.data[i] = (double *)calloc(col, sizeof(double));
        if (m.data[i] == NULL) {
            fprintf(stderr, "Error: calloc failed for matrix row\n");
            for(int j = 0; j < i; j++) free(m.data[j]);
            free(m.data);
            exit(1);
        }
    }
    return m;
}

void freematrix(matrix m)
{
    if (m.data) {
        for (int i = 0; i < m.row; i++)
        {
            free(m.data[i]);
        }
        free(m.data);
    }
}

//______________________________________________________________________________________________________

// --- REPLACED FUNCTION ---
void skipComments(FILE *fp)
{
    int ch;
    char line[1024];

    // Loop to handle multiple comment lines and whitespace
    while (1) {
        // First, skip any leading whitespace (spaces, newlines, etc.)
        while ((ch = fgetc(fp)) != EOF && isspace(ch));

        // If the character is not a comment, put it back and we're done
        if (ch != '#') {
            if (ch != EOF) { // Don't put back End-Of-File
                ungetc(ch, fp);
            }
            return;
        }

        // If it was a comment, read and discard the rest of the line
        if (fgets(line, sizeof(line), fp) == NULL) {
            // Reached end of file after a '#', which is fine.
            return;
        }
    }
}


matrix PGMfilereader(const char *file)
{
    FILE *fp = fopen(file, "r");
    if (!fp)
    {
        fprintf(stderr, "Error: Cannot open file %s\n", file);
        exit(1);
    }
    
    char magicnum[3];
    int width;
    int height;
    int maxvalue;

    if (fscanf(fp, "%s", magicnum) != 1) {
        fprintf(stderr, "Error: Could not read magic number from %s\n", file);
        fclose(fp);
        exit(1);
    }
    
    skipComments(fp);
    
    if (fscanf(fp, "%d %d", &width, &height) != 2) {
        fprintf(stderr, "Error: Could not read width and height from %s\n", file);
        fclose(fp);
        exit(1);
    }
    
    skipComments(fp);
    
    if (fscanf(fp, "%d", &maxvalue) != 1) {
        fprintf(stderr, "Error: Could not read max value from %s\n", file);
        fclose(fp);
        exit(1);
    }
    
    // Consume the single whitespace character after the max value
    fgetc(fp);

    matrix img = creatematrix(height, width);

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int pix = 0;
            if (fscanf(fp, "%d", &pix) != 1) {
                fprintf(stderr, "Error: Failed reading pixel data at (%d, %d)\n", i, j);
                freematrix(img);
                fclose(fp);
                exit(1);
            }
            img.data[i][j] = (double)pix;
        }
    }
    fclose(fp);
    return img;
}

//______________________________________________________________//

int clamp(double value)
{
    if (value < 0)
        return 0;
    else if (value > 255)
        return 255;
    else
        return (int)(value + 0.5);
}

void writepgm(const char *filename, matrix img)
{
    FILE *fp = fopen(filename, "w");
    if (!fp)
    {
        fprintf(stderr, "Error: Cannot write to file %s\n", filename);
        exit(1);
    }
    
    fprintf(fp, "P2\n");
    fprintf(fp, "# SVD reconstructed image\n");
    fprintf(fp, "%d %d\n", img.col, img.row);
    fprintf(fp, "255\n");
    for (int i = 0; i < img.row; i++)
    {
        for (int j = 0; j < img.col; j++)
        {
            fprintf(fp, "%d ", clamp(img.data[i][j]));
        }
        fprintf(fp, "\n");
    }
    fclose(fp);
}

//_______________________________________________________________________//

matrix Transpose(matrix A)
{
    matrix A_t = creatematrix(A.col, A.row);
    for (int i = 0; i < A.row; i++)
    {
        for (int j = 0; j < A.col; j++)
        {
            A_t.data[j][i] = A.data[i][j];
        }
    }
    return A_t;
}

matrix multiply(matrix A, matrix B)
{
    if (A.col != B.row)
    {
        printf("Error: Cannot multiply - dimension mismatch\n");
        exit(1);
    }

    matrix AB = creatematrix(A.row, B.col);
    for (int i = 0; i < A.row; i++)
    {
        for (int j = 0; j < B.col; j++)
        {
            for (int k = 0; k < A.col; k++)
            {
                AB.data[i][j] += A.data[i][k] * B.data[k][j];
            }
        }
    }
    return AB;
}

double norm(double *v, int n)
{
    double sum = 0.0;
    for (int i = 0; i < n; i++)
    {
        sum += v[i] * v[i];
    }
    return sqrt(sum);
}

void normalize(double *v, int n)
{
    double norm_v = norm(v, n);
    if (norm_v > 1e-9)
    {
        for (int i = 0; i < n; i++)
        {
            v[i] /= norm_v;
        }
    }
}

double dot_product(double *v, double *w, int n)
{
    double result = 0.0;
    for (int i = 0; i < n; i++)
    {
        result += v[i] * w[i];
    }
    return result;
}

void matrix_vector_multiplication(matrix A, double *v, double *w)
{
    int m = A.row;
    int n = A.col;
    for (int i = 0; i < m; i++)
    {
        w[i] = 0.0;
        for (int j = 0; j < n; j++)
        {
            w[i] += A.data[i][j] * v[j];
        }
    }
}

matrix At_multiply_A(matrix A)
{
    matrix At = Transpose(A);
    matrix AtA = multiply(At, A);
    freematrix(At);
    return AtA;
}

void deflatematrix(matrix b, double l, double *v)
{
    int n = b.row;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            b.data[i][j] -= l * v[i] * v[j];
        }
    }
}

//________________________________________________________________//

matrix copyMatrix(matrix A)
{
    matrix B = creatematrix(A.row, A.col);
    for (int i = 0; i < A.row; i++)
    {
        for (int j = 0; j < A.col; j++)
        {
            B.data[i][j] = A.data[i][j];
        }
    }
    return B;
}

double poweriteration(matrix b, double *v)
{
    int n = b.row;
    const int maxit = 1000;
    const double tol = 1e-6;
    double l = 0.0;
    double lprev = 0.0;

    for (int i = 0; i < n; i++)
    {
        v[i] = (double)rand() / RAND_MAX;
    }

    normalize(v, n);

    double *w = (double *)malloc(n * sizeof(double));
    if (w == NULL) {
        fprintf(stderr, "Error: malloc failed in poweriteration\n");
        exit(1);
    }

    for (int i = 0; i < maxit; i++)
    {
        matrix_vector_multiplication(b, v, w);
        l = dot_product(v, w, n);

        normalize(w, n);
        for (int j = 0; j < n; j++)
        {
            v[j] = w[j];
        }

        if (fabs(l - lprev) < tol)
        {
            break;
        }

        lprev = l;
    }

    free(w);
    return l;
}

typedef struct
{
    matrix u;
    matrix v;
    double *s;
    int k;
} svdresult;

void freeSVDResult(svdresult svd)
{
    freematrix(svd.u);
    freematrix(svd.v);
    free(svd.s);
}

svdresult SVD_compute(matrix a, int k)
{
    int m = a.row;
    int n = a.col;

    matrix b = At_multiply_A(a);
    matrix b_temp = copyMatrix(b);

    svdresult svd;
    svd.k = k;
    svd.s = (double *)malloc(k * sizeof(double));
    if (svd.s == NULL) {
        fprintf(stderr, "Error: malloc failed for singular values\n");
        exit(1);
    }
    svd.v = creatematrix(n, k);
    svd.u = creatematrix(m, k);

    double *v = (double *)malloc(n * sizeof(double));
    if (v == NULL) {
        fprintf(stderr, "Error: malloc failed for v vector\n");
        exit(1);
    }
    double *u_col = (double *)malloc(m * sizeof(double));
    if (u_col == NULL) {
        fprintf(stderr, "Error: malloc failed for u_col vector\n");
        exit(1);
    }

    printf("Starting Power Iteration loop for k=%d...\n", k);

    for (int i = 0; i < k; i++)
    {
        double l = poweriteration(b_temp, v);
        svd.s[i] = sqrt(l);

        for (int j = 0; j < n; j++)
        {
            svd.v.data[j][i] = v[j];
        }

        deflatematrix(b_temp, l, v);
    }

    for (int i = 0; i < k; i++)
    {
        for (int j = 0; j < n; j++)
        {
            v[j] = svd.v.data[j][i];
        }

        matrix_vector_multiplication(a, v, u_col);

        double sigma = svd.s[i];
        if (sigma > 1e-9)
        {
            for (int j = 0; j < m; j++)
            {
                svd.u.data[j][i] = u_col[j] / sigma;
            }
        }
        else
        {
            for (int j = 0; j < m; j++)
            {
                svd.u.data[j][i] = 0.0;
            }
        }
    }

    freematrix(b);
    freematrix(b_temp);
    free(v);
    free(u_col);

    return svd;
}

int main(int argc, char *argv[])
{
    if (argc < 3)
    {
        printf("Usage: %s <input_image.pgm> <k_value_1> [k_value_2] ...\n", argv[0]);
        return 1;
    }

    srand(42);

    const char *filename = argv[1];

    printf("Reading image %s...\n", filename);
    matrix A = PGMfilereader(filename);
    printf("Image size: %d rows x %d cols\n", A.row, A.col);

    int max_k = (A.row < A.col) ? A.row : A.col;

    for (int i = 2; i < argc; i++)
    {
        int k = atoi(argv[i]);
        if (k <= 0 || k > max_k)
        {
            printf("Skipping invalid k=%d. Must be > 0 and <= %d\n", k, max_k);
            continue;
        }

        printf("\n--- Computing SVD for k=%d ---\n", k);

        svdresult svd = SVD_compute(A, k);

        printf("SVD computation complete. Singular values:\n");
        for (int j = 0; j < k; j++)
        {
            printf("  sigma_%d = %.2f\n", j + 1, svd.s[j]);
        }

        printf("Reconstructing image...\n");
        matrix A_k = creatematrix(A.row, A.col);
        
        for (int r = 0; r < k; r++)
        {
            double sigma = svd.s[r];
            for (int row_idx = 0; row_idx < A.row; row_idx++)
            {
                for (int col_idx = 0; col_idx < A.col; col_idx++)
                {
                    A_k.data[row_idx][col_idx] += sigma * svd.u.data[row_idx][r] * svd.v.data[col_idx][r];
                }
            }
        }

        char out_filename[100];
        sprintf(out_filename, "reconstructed_k%d.pgm", k);
        printf("Writing %s...\n", out_filename);
        writepgm(out_filename, A_k);

        freeSVDResult(svd);
        freematrix(A_k);

        printf("Done for k=%d\n", k);
    }

    freematrix(A);
    return 0;
}