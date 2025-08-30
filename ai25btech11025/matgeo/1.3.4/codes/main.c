#include <stdio.h>

// Function declarations (prototypes)
double dx_from_abc(double ax, double ay, double bx, double by, double cx, double cy);
double dy_from_abc(double ax, double ay, double bx, double by, double cx, double cy);
int write_points_file(const char *filepath,
                      double ax, double ay,
                      double bx, double by,
                      double cx, double cy);

int main(void) {
    // Given A(1,3), B(-1,2), C(2,5)
    double ax=1, ay=3, bx=-1, by=2, cx=2, cy=5;

    double dx = dx_from_abc(ax, ay, bx, by, cx, cy);
    double dy = dy_from_abc(ax, ay, bx, by, cx, cy);

    printf("Computed x for D: %.10g\n", dx);
    printf("Computed y for D (for consistency): %.10g\n", dy);

    // Write coordinates to a file
    if (write_points_file("points.dat", ax, ay, bx, by, cx, cy) != 0) {
        fprintf(stderr, "Failed to write points.dat\n");
        return 1;
    }
    printf("Wrote points to points.dat\n");

    return 0;
}
