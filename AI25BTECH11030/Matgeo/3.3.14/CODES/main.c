#include <stdio.h>
#include "trianglefun.h"

int main() {
    double side1, side2;

    printf("Enter the lengths of two sides of the right triangle: ");
    scanf("%lf %lf", &side1, &side2);

    Vector2D A = vector_create(side1, 0);
    Vector2D B = vector_create(0, side2);

    Vector2D C = vector_add(A, B);
    double hypotenuse = vector_magnitude(C);

    printf("The hypotenuse length is: %.2f\n", hypotenuse);

    return 0;
}

