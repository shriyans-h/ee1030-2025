#include <math.h>
double cross_product_x(double a_x, double a_y, double a_z, double b_x, double b_y, double b_z) {
    return (a_y * b_z - a_z * b_y);
}

double cross_product_y(double a_x, double a_y, double a_z, double b_x, double b_y, double b_z) {
    return (a_z * b_x - a_x * b_z);
}

double cross_product_z(double a_x, double a_y, double a_z, double b_x, double b_y, double b_z) {
    return (a_x * b_y - a_y * b_x);
}

double dot_product(double a_x, double a_y, double a_z, double b_x, double b_y, double b_z) {
    return a_x * b_x + a_y * b_y + a_z * b_z;
}