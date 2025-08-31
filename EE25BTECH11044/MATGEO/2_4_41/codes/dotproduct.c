#include <stdio.h>

int main() {
      double A[3],B[3],C[3];
    double AB[3] = {B[0]-A[0], B[1]-A[1], B[2]-A[2]};
    double AC[3] = {C[0]-A[0], C[1]-A[1], C[2]-A[2]};
    double BC[3] = {C[0]-B[0], C[1]-B[1], C[2]-B[2]};

    double ABdotAC = AB[0]*AC[0] + AB[1]*AC[1] + AB[2]*AC[2];
    double ABdotBC = AB[0]*BC[0] + AB[1]*BC[1] + AB[2]*BC[2];
    double ACdotBC = AC[0]*BC[0] + AC[1]*BC[1] + AC[2]*BC[2];

    if(ABdotAC==0 || ABdotBC==0 || ACdotBC==0)
        printf("Right-angled triangle\n");
    else
        printf("Not right-angled\n");

    return 0;
}
