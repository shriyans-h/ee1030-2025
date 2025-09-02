#include <stdio.h>
#include <math.h>

int main() {
    // Given values
    double magnitude_a = 5.0;
    double magnitude_b = 1.5;
    double theta = M_PI / 6;  // 30 degrees in radians (you can change this)

    // Vector a (let's place it along x-axis for simplicity)
    double a_x = magnitude_a;
    double a_y = 0.0;

    // Vector b (at angle theta from vector a)
    double b_x = magnitude_b *(cos(theta));
    double b_y = magnitude_b *(sin(theta));

    // Resultant vector c = a + b
    double c_x = a_x + b_x;
    double c_y = a_y + b_y;

    // Open file for writing
    FILE *file = fopen("vectors.dat", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Write header
    fprintf(file, "# Vector data: a_x a_y b_x b_y c_x c_y theta\n");

    // Write vector components and angle
    fprintf(file, "%.6f %.6f %.6f %.6f %.6f %.6f %.6f\n", 
            a_x, a_y, b_x, b_y, c_x, c_y, theta);

    fclose(file);
double root = pow(c_x*c_x + c_y*c_y, 0.5);

    printf("Vector data saved to vectors.dat\n");
    printf("Vector a: (%.3f, %.3f), magnitude: %.3f\n", a_x, a_y, magnitude_a);
    printf("Vector b: (%.3f, %.3f), magnitude: %.3f\n", b_x, b_y, magnitude_b);
    printf("Vector c: (%.3f, %.3f), magnitude: %.3f\n", c_x, c_y, root);
    printf("Angle theta: %.3f radians (%.1f degrees)\n", theta, theta * 180.0 / M_PI);

    return 0;
}
