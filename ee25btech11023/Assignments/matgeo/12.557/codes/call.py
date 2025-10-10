import numpy as np

A = np.array([
    [ 5, -3],
    [ 6, -4]
])

eigenvalues = np.linalg.eigvals(A)
lambda_1, lambda_2 = eigenvalues


print(f"Trace of A^1000={lambda_1}^1000+{lambda_2**1000}")

