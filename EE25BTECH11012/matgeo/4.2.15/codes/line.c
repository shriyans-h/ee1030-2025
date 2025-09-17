#include <stdio.h>

int main() {
    // For the line equation y = 2x, which can be rewritten as 2x - 1y = 0.
    // This is in the general form Ax + By + C = 0.
    
    // Coefficients from the equation 2x - y = 0
    float A = 2.0;
    float B = -1.0;
    
    // The normal vector is given by the coefficients (A, B)
    float normal_vector_x = A;
    float normal_vector_y = B;
    
    // The direction vector is perpendicular to the normal vector.
    // A vector perpendicular to (A, B) is (-B, A).
    float direction_vector_x = -B;
    float direction_vector_y = A;
    
    // Print the results
    printf("For the line y = 2x (or %.1fx + %.1fy = 0):\n\n", A, B);
    
    printf("A Normal Vector is: (%.1f, %.1f)\n", normal_vector_x, normal_vector_y);
    printf("A Direction Vector is: (%.1f, %.1f)\n", direction_vector_x, direction_vector_y);
    
    return 0;
}