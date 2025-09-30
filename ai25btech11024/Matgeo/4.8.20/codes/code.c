#include<math.h>

double dot(double a[3],double b[3]){
		return a[0]*b[0]+a[1]*b[1]+a[2]*b[2];
}

double dist(double arr[3]){
		double n[3]={3,2,2};
		double b[3]={3,6,2};

		double d=sqrt(dot(b,b))*dot(n,arr)/dot(n,b);

		return d;
}
