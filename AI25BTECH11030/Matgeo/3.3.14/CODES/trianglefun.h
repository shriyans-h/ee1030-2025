#ifndef TRIANGLEFUN_H
#define TRIANGLEFUN_H

typedef struct {
    double x;
    double y;
} Vector2D;

Vector2D vector_create(double x, double y);
Vector2D vector_add(Vector2D a, Vector2D b);
double vector_magnitude(Vector2D v);

#endif
