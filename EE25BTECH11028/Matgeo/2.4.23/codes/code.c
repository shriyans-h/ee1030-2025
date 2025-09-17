#include <stdio.h>

int main() {
    // Given points
    int x1=3,y1=2, x2=-2,y2=-3, x3=2,y3=3;

    /* -------- PART 1 : Check Collinearity -------- */
    int det = x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2);

    if(det==0){
        printf("PART 1: The points are collinear. No triangle formed.\n");
        printf("PART 3: Final Conclusion -> No triangle exists.\n");
        return 0;
    }
    else{
        printf("PART 1: The points form a triangle.\n");
    }

    /* -------- PART 2 : Check Right Angle -------- */
    int ABx=x2-x1, ABy=y2-y1;
    int ACx=x3-x1, ACy=y3-y1;
    int BCx=x3-x2, BCy=y3-y2;

    int right=0; // flag
    char vertex;

    if(ABx*ACx + ABy*ACy == 0){ right=1; vertex='A'; }
    else if(ABx*BCx + ABy*BCy == 0){ right=1; vertex='B'; }
    else if(ACx*BCx + ACy*BCy == 0){ right=1; vertex='C'; }

    if(right)
        printf("PART 2: The triangle is right-angled at %c.\n", vertex);
    else
        printf("PART 2: The triangle is not right-angled.\n");

    /* -------- PART 3 : Final Conclusion -------- */
    if(right)
        printf("PART 3: Final Conclusion -> Triangle formed, right-angled at %c.\n", vertex);
    else
        printf("PART 3: Final Conclusion -> Triangle formed, but not right-angled.\n");

    return 0;
}
