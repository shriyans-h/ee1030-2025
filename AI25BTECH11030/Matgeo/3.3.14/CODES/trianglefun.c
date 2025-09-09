#include <math.h>
#include "trianglefun.h"

Vector2D vector_create(double x, double y) {
    Vector2D v;
    v.x = x;
    v.y = y;
    return v;
}

Vector2D vector_add(Vector2D a, Vector2D b) {
    Vector2D result;
    result.x = a.x + b.x;
    result.y = a.y + b.y;
    return result;
}

double vector_magnitude(Vector2D v) {
    return sqrt(v.x * v.x + v.y * v.y);
}
