#include<stdio.h>
void midpoint(float* out, float* A, float* B) {
    out[0] = (A[0] + B[0]) / 2.0f; // X-coordinate
    out[1] = (A[1] + B[1]) / 2.0f; // Y-coordinate
    out[2] = (A[2] + B[2]) / 2.0f; // Z-coordinate
}
