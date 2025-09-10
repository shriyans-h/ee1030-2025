#include <stdio.h>
#include <math.h>

// Structure for 2D vector
typedef struct {
    double x;
    double y;
} Vector;

// Function to normalize a vector
Vector normalize(Vector v) {
    double mag = sqrt(v.x * v.x + v.y * v.y);
    Vector result = {v.x / mag, v.y / mag};
    return result;
}

// Function to add two vectors
Vector add(Vector a, Vector b) {
    Vector result = {a.x + b.x, a.y + b.y};
    return result;
}

// Function to subtract two vectors
Vector subtract(Vector a, Vector b) {
    Vector result = {a.x - b.x, a.y - b.y};
    return result;
}

// Function to negate a vector
Vector negate(Vector v) {
    Vector result = {-v.x, -v.y};
    return result;
}

// Function to compute magnitude
double magnitude(Vector v) {
    return sqrt(v.x * v.x + v.y * v.y);
}

// Function to save vectors to .dat file
void save_to_dat(Vector a, Vector b, Vector neg_b, Vector sum, Vector diff, const char *filename) {
    FILE *fp = fopen(filename, "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return;
    }
    fprintf(fp, "Vector\tX\tY\tMagnitude\n");
    fprintf(fp, "a\t%.4f\t%.4f\t%.4f\n", a.x, a.y, magnitude(a));
    fprintf(fp, "b\t%.4f\t%.4f\t%.4f\n", b.x, b.y, magnitude(b));
    fprintf(fp, "-b\t%.4f\t%.4f\t%.4f\n", neg_b.x, neg_b.y, magnitude(neg_b));
    fprintf(fp, "a+b\t%.4f\t%.4f\t%.4f\n", sum.x, sum.y, magnitude(sum));
    fprintf(fp, "a-b\t%.4f\t%.4f\t%.4f\n", diff.x, diff.y, magnitude(diff));
    fclose(fp);
    printf("Data saved to %s\n", filename);
}

int main() {
    // Define vectors: a = (1,0), b = (cos120, sin120)
    Vector a = {1.0, 0.0};
    Vector b = {cos(M_PI * 120.0 / 180.0), sin(M_PI * 120.0 / 180.0)};
    
    // Normalize to ensure unit vectors
    a = normalize(a);
    b = normalize(b);
    
    // Compute required vectors
    Vector sum = add(a, b);
    Vector diff = subtract(a, b);
    Vector neg_b = negate(b);
    
    // Print to console
    printf("|a+b| = %.3f\n", magnitude(sum));
    printf("|a-b| = %.3f\n", magnitude(diff));
    printf("|-b|  = %.3f\n", magnitude(neg_b));
    
    // Save results in same folder as code
    save_to_dat(a, b, neg_b, sum, diff, "vectors_data.dat");
    
    return 0;
}
