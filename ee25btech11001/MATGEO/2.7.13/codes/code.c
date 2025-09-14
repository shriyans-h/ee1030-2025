#include <stdio.h>
#include <math.h>

double area_of_quadrilateral(double x1, double y1,
                             double x2, double y2,
                             double x3, double y3,
                             double x4, double y4) {
    double area = 0.5 * fabs(x1*y2 + x2*y3 + x3*y4 + x4*y1
                           - y1*x2 - y2*x3 - y3*x4 - y4*x1);
    return area;
}
