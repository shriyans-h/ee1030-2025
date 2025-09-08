// Vector ops for 3D problems (dot, cross, norms, angle).
// Compile:  gcc vec.c -lm
#include <stdio.h>
#include <math.h>

typedef struct { double x, y, z; } V3;

static inline V3  cross(V3 a, V3 b){
    V3 c = { a.y*b.z - a.z*b.y,
             a.z*b.x - a.x*b.z,
             a.x*b.y - a.y*b.x };
    return c;
}
static inline double dot(V3 a, V3 b){ return a.x*b.x + a.y*b.y + a.z*b.z; }
static inline double norm(V3 a){ return sqrt(dot(a,a)); }

int main(void){
    V3 a, b;
    // Input: ax ay az  bx by bz
    if (scanf("%lf %lf %
