#include<math.h>

double find(double a00,double a02,double a10,double a11,double a12,double a20,double a21,double a22, double A){
	double alpha;
	alpha=(-1)*(pow(A,2)-a00*(a11*a22-a21*a12)-a02*(a10*a21-a20*a11))/(a10*a22-a20*a12);
	return alpha;
}
