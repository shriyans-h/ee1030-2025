#include <stdio.h>
#include <math.h>

double angleWithYAxis(double vx, double vy, double vz) {
    double jy = 1.0;
    double dot = vy * jy;
    double magv = sqrt(vx*vx + vy*vy + vz*vz);
    double magj = 1.0;
    double cosTheta = dot / (magv * magj);
    double thetaRad = acos(cosTheta);
    double thetaDeg = thetaRad * 180.0 / M_PI;
    return thetaDeg;
}

int main() {
    double vx = 1, vy = -1, vz = 2;
    double theta = angleWithYAxis(vx, vy, vz);
    printf("Angle with positive Y-axis = %.2f degrees\n", theta);
    return 0;
}
