#include <stdio.h>

// Function to calculate Dx (x-coordinate of D)
double dx_from_abc(double ax, double ay, double bx, double by, double cx, double cy) {
    (void)ay; (void)by; (void)cy; // unused
    return ax + cx - bx;
}

// Function to calculate Dy (y-coordinate of D)
double dy_from_abc(double ax, double ay, double bx, double by, double cx, double cy) {
    (void)ax; (void)bx; (void)cx; // unused
    return ay + cy - by;
}

// Function to write points into a file
int write_points_file(const char *filepath,
                      double ax, double ay,
                      double bx, double by,
                      double cx, double cy) {
    double dx = dx_from_abc(ax, ay, bx, by, cx, cy);
    double dy = dy_from_abc(ax, ay, bx, by, cx, cy);

    FILE *fp = fopen(filepath, "w");
    if (!fp) return 1;
    fprintf(fp, "A %.10g %.10g\n", ax, ay);
    fprintf(fp, "B %.10g %.10g\n", bx, by);
    fprintf(fp, "C %.10g %.10g\n", cx, cy);
    fprintf(fp, "D %.10g %.10g\n", dx, dy);
    fclose(fp);
    return 0;
}
