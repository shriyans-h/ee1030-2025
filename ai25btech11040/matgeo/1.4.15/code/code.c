double point_x(double x1, double x2, double l, double m) {
    /* Returns the x-coordinate of the point dividing points with coordinates (x1, y1) and (x2, y2) in the ratio l:m */
    return (x1*m + x2*l)/(l+m);
}

double point_y(double y1, double y2, double l, double m) {
    /* Returns the y-coordinate of the point dividing points with coordinates (x1, y1) and (x2, y2) in the ratio l:m */
    return (y1*m + y2*l)/(l+m);
}