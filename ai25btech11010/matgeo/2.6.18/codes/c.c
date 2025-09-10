#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Structure to store a 2D point
typedef struct {
    double x;
    double y;
} Point;

// Function to calculate the area of a triangle using 2D determinant formula
double triangle_area(Point A, Point B, Point C) {
    return 0.5 * fabs(A.x*(B.y - C.y) + B.x*(C.y - A.y) + C.x*(A.y - B.y));
}

// Function to save points and area to a file
void save_points_and_area(const char *filename, Point A, Point B, Point C, double area) {
    FILE *fp = fopen(filename, "w");
    if (fp == NULL) {
        printf("Error opening file!\n");
        exit(1);
    }
    fprintf(fp, "Triangle Vertices:\n");
    fprintf(fp, "A: %.2lf %.2lf\n", A.x, A.y);
    fprintf(fp, "B: %.2lf %.2lf\n", B.x, B.y);
    fprintf(fp, "C: %.2lf %.2lf\n", C.x, C.y);
    fprintf(fp, "Area of the triangle: %.2lf\n", area);
    fclose(fp);
}

int main() {
    // Triangle vertices
    Point A = {-1, 0};
    Point B = {1, 3};
    Point C = {3, 2};

    // Calculate area
    double area = triangle_area(A, B, C);

    // Print points and area
    printf("Triangle Vertices:\n");
    printf("A: (%.2lf, %.2lf)\n", A.x, A.y);
    printf("B: (%.2lf, %.2lf)\n", B.x, B.y);
    printf("C: (%.2lf, %.2lf)\n", C.x, C.y);
    printf("Area of the triangle: %.2lf\n", area);

    // Save points and area to file
    save_points_and_area("points.dat", A, B, C, area);
    printf("Triangle points and area saved in points.dat\n");

    return 0;
}

