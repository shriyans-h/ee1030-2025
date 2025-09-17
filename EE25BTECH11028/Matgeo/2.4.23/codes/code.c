#include <stdio.h>
#include <math.h>

int main() {
    int x1=3,y1=2, x2=-2,y2=-3, x3=2,y3=3;
    int area = x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2);

    if(area == 0) {
        printf("Collinear, no triangle.\n");
        return 0;
    }

    double AB = sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1));
    double BC = sqrt((x3-x2)*(x3-x2) + (y3-y2)*(y3-y2));
    double AC = sqrt((x3-x1)*(x3-x1) + (y3-y1)*(y3-y1));

    if(AB==BC && BC==AC)
        printf("Equilateral triangle\n");
    else if(AB==BC || BC==AC || AB==AC)
        printf("Isosceles triangle\n");
    else
        printf("Scalene triangle\n");

    return 0;
} 