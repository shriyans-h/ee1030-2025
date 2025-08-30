#include <stdio.h>

// Function to write points into a file
void generate_points(const char *filename) {
    FILE *fp = fopen(filename, "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return;
    }

    // Points A, B, C
    double A[3] = {0, 7, -10};
    double B[3] = {1, 6, -6};
    double C[3] = {4, 9, -6};

    fprintf(fp, "%lf %lf %lf\n", A[0], A[1], A[2]);
    fprintf(fp, "%lf %lf %lf\n", B[0], B[1], B[2]);
    fprintf(fp, "%lf %lf %lf\n", C[0], C[1], C[2]);

    fclose(fp);
}

