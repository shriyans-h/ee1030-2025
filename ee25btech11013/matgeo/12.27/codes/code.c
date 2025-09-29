void mat_vec_mult(double* a, double* x, double* result) {
    result[0] = a[0] * x[0] + a[1] * x[1];
    result[1] = a[2] * x[0] + a[3] * x[1];
}
