#include <stdio.h>

void isosceles_triangle(double *points) {
    double coords[6] = {5,-2,  6,4,  7,-2,};

    for (int i = 0; i < 6; i++) {
        points[i] = coords[i];
    }
}
