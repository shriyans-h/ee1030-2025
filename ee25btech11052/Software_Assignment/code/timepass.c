// Structure to hold matrix
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef struct {
    int rows;
    int cols;
    double **data;
} Matrix;

// Skip comment lines starting with '#'
void skipComments(FILE *fp) {
    int ch;
    while ((ch = fgetc(fp)) == '#') {
        // Skip until end of line
        while (fgetc(fp) != '\n');
    }
    ungetc(ch, fp);  // Put back non-comment character
}

// Read PGM file into matrix
Matrix readPGM(const char *filename) {
    FILE *fp = fopen(filename, "r");
    if (!fp) {
        printf("Error: Cannot open %s\n", filename);
        exit(1);
    }
    
    char magic[3];
    int width, height, maxval;
    
    // Read magic number (P2 or P5)
    fscanf(fp, "%s", magic);
    
    // Skip any comments after magic number
    skipComments(fp);
    
    // Read dimensions
    fscanf(fp, "%d %d", &width, &height);
    
    // Skip comments
    skipComments(fp);
    
    // Read maximum value
    fscanf(fp, "%d", &maxval);
    
    // Allocate matrix
    Matrix img;
    img.rows = height;
    img.cols = width;
    img.data = (double**)malloc(height * sizeof(double*));
    for (int i = 0; i < height; i++) {
        img.data[i] = (double*)malloc(width * sizeof(double));
    }
    
    // Read pixel data
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            int pixel;
            fscanf(fp, "%d", &pixel);
            img.data[i][j] = (double)pixel;
        }
    }
    
    fclose(fp);
    return img;
}