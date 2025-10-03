#include<stdio.h>
#include<math.h>

void solve(double arr[2][2]){
	double a=1;
	double b;
	double c;

	b=(-1)*(arr[0][0]+arr[1][1]);
	c=arr[0][0]*arr[1][1]-arr[0][1]*arr[1][0];

	printf("(%.0lf)A^2 + (%.0lf)A + (%.0lf)I",a,b,c);
}
