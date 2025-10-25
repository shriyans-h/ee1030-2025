#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>

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
    for (int i = 0; i < row; i++)
    {
        m.data[i] = (double *)calloc(col, sizeof(double));
    }
    return m;
}
// memory free karne ka function
void freematrix(matrix m)
{
    for (int i = 0; i < m.row; i++)
    {
        free(m.data[i]);
    }
    free(m.data);
}

void skipComments(FILE *fp)
{
    int ch;
    char line[1024];
    while ((ch = fgetc(fp)) == '#')
    {
        fgets(line, sizeof(line), fp);
    }
    ungetc(ch, fp);
}

// file se matrix read karne ka function
matrix PGMfilereader(const char *file)
{
    FILE *fp = fopen(file, "r");
    char magicnum[3];
    int width;
    int height;
    int maxvalue;

    fscanf(fp, "%s", magicnum);
    skipComments(fp);
    fscanf(fp, "%d %d", &width, &height);
    skipComments(fp);
    fscanf(fp, "%d", &maxvalue);

    matrix img = creatematrix(height, width);

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int pix = 0;
            fscanf(fp, "%d", &pix);
            img.data[i][j] = (double)pix;
        }
    }
    fclose(fp);
    return img;
}
// ye range me lane ke liye  and round off karne ke liye
int clamp(double value)
{
    if (value < 0)
        return 0;
    else if (value > 255)
        return 255;
    else
        return (int)(value + 0.5);
}

// PGM file likhne ka function
void writepgm(const char *filename, matrix img)
{
    FILE *fp = fopen(filename, "w");
    fprintf(fp, "P2\n");
    fprintf(fp, "# did the SVD\n");
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

// yaha se main function start hota hai and now all the function needed to perform SVD using power iterative method

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
        printf("cannot multiply\n");
        exit(1);
    }

    matrix AB = creatematrix(A.row, B.col);
    {
        for (int i = 0; i < A.row; i++)
        {
            for (int j = 0; i < B.col; j++)
            {
                for (int k = 0; k < A.col; k++)
                {
                    AB.data[i][j] += A.data[i][k] * B.data[k][j];
                }
            }
        }
    }

    return AB;
}

// B = A^T * A
// Matrix At_multiply_A ( Matrix A ) -- ye cheez directy main functionm me likhenge

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



void matrix_vector_multiplication(matrix A,double* v, double* w)
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


















// int main(int argc, char *argv[])
{
    // Check if a filename was provided on the command line
    if (argc < 2)
    {
        printf("Usage: %s <input_image.pgm>\n", argv[0]);
        return 1; // Exit with an error
    }

    const char *inputFilename = argv[1];

    printf("Reading image %s...\n", inputFilename);

    matrix myImage = PGMfilereader(inputFilename);

    // Print the results to show it worked
    printf("Image loaded successfully!\n");
    printf("Dimensions: %d rows x %d cols\n", myImage.row, myImage.col);

    // Example: Print the pixel value at (0,0)
    if (myImage.row > 0 && myImage.col > 0)
    {
        printf("Pixel value at (0,0): %.1f\n", myImage.data[0][0]);
    }

    freematrix(myImage);
    printf("Matrix memory freed.\n");

    return 0;
}