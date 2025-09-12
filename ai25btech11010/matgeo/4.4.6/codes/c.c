#include <stdio.h>

typedef struct {
    double x, y, z;
} Point;

int main() {
    Point A = {2, 5, -3};
    Point B = {-2, -3, 5};
    Point C = {5, 3, -3};

    // Compute vectors AB and AC
    double AB[3] = {B.x - A.x, B.y - A.y, B.z - A.z};
    double AC[3] = {C.x - A.x, C.y - A.y, C.z - A.z};

    // Normal vector n = AB x AC
    double n[3];
    n[0] = AB[1]*AC[2] - AB[2]*AC[1];
    n[1] = AB[2]*AC[0] - AB[0]*AC[2];
    n[2] = AB[0]*AC[1] - AB[1]*AC[0];

    // Plane equation: n•X = d
    double d = n[0]*A.x + n[1]*A.y + n[2]*A.z;

    // Save points and plane to file
    FILE *fp = fopen("plane_points.dat", "w");
    fprintf(fp, "# Plane: %lf*x + %lf*y + %lf*z = %lf\n", n[0], n[1], n[2], d);
    fprintf(fp, "%lf %lf %lf\n", A.x, A.y, A.z);
    fprintf(fp, "%lf %lf %lf\n", B.x, B.y, B.z);
    fprintf(fp, "%lf %lf %lf\n", C.x, C.y, C.z);
    fclose(fp);

    // Print normal and d for Python
    printf("%lf %lf %lf %lf\n", n[0], n[1], n[2], d);

    return 0;
}

