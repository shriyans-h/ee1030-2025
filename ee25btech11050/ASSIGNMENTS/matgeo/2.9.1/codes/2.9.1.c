// Save this as shapes.c
#include <stdio.h>

typedef struct {
    int x, y;
} Point;

void get_triangle(Point* pts) {
    pts[0].x = 200; pts[0].y = 800;     // A
    pts[1].x = 200; pts[1].y = 0;       // Q
    pts[2].x = -600; pts[2].y = 0;      // C
}

void get_square(Point* pts) {
    pts[0].x = -200; pts[0].y = 0;      // P
    pts[1].x = 200;  pts[1].y = 0;    // Q
    pts[2].x = 200; pts[2].y = 400;    // R
    pts[3].x = -200;  pts[3].y = 400;      // S 
}






