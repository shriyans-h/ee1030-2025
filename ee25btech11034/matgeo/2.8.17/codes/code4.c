#include <stdio.h>
#include <stdlib.h>

// This function will be called from Python.
// It generates points for the two perpendicular lines and fills the provided arrays.
void generate_line_points(int num_points, double* line1_x, double* line1_y, double* line1_z, double* line2_x, double* line2_y, double* line2_z) {
    
    // Direction vector for Line 1 (derived by setting l=1)
    double d1_x = 1.0;
    double d1_y = -2.0;
    double d1_z = -2.0;

    // Direction vector for Line 2 (derived by setting m=1)
    double d2_x = -2.0;
    double d2_y = 1.0;
    double d2_z = -2.0;

    // Generate points along a parameter t from -3.0 to 3.0
    double t_start = -3.0;
    double t_end = 3.0;
    double t_step = (t_end - t_start) / (num_points - 1);
    
    double t = t_start;
    for (int i = 0; i < num_points; i++) {
        // Calculate points for Line 1: P = t * d1
        line1_x[i] = t * d1_x;
        line1_y[i] = t * d1_y;
        line1_z[i] = t * d1_z;

        // Calculate points for Line 2: P = t * d2
        line2_x[i] = t * d2_x;
        line2_y[i] = t * d2_y;
        line2_z[i] = t * d2_z;
        
        t += t_step;
    }
}
