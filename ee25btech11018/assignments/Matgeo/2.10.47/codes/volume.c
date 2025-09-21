#include <stdio.h>
#include <math.h>

// Determinant of Gram matrix calculation with inline dot product calculations
double gram_determinant(double a) {
    double G11 = 2 + a * a;
    double G12 = 2 * a;
    double G13 = a + 1;
    double G21 = 2 * a;
    double G22 = a * a + 1;
    double G23 = a;
    double G31 = a + 1;
    double G32 = a;
    double G33 = 1 + a * a;

    double det = G11 * (G22 * G33 - G23 * G32) 
               - G12 * (G21 * G33 - G23 * G31) 
               + G13 * (G21 * G32 - G22 * G31);

    return det;
}

// Volume calculation (sqrt of determinant)
double volume(double a) {
    double det = gram_determinant(a);
    if (det < 0) det = -det; // use absolute value for volume
    return sqrt(det);
}

int main() {
    double options[] = {-3, 3, 1.0 / sqrt(3), sqrt(3)};
    int num_options = 4;

    double min_vol = 1e9;
    double min_a = 0;

    printf("%-10s %-15s %-15s\n", "a", "Determinant", "Volume");
    printf("-------------------------------------------\n");

    for (int i = 0; i < num_options; i++) {
        double a = options[i];
        double det = gram_determinant(a);
        double vol = volume(a);
        printf("%-10.6f %-15.6f %-15.6f\n", a, det, vol);
        if (vol < min_vol) {
            min_vol = vol;
            min_a = a;
        }
    }

    printf("\nMinimum volume is at a = %.6f with volume = %.6f\n", min_a, min_vol);

    return 0;
}

