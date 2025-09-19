import numpy as np

A = np.array([[2,0,-1],
              [5,1,0],
              [0,1,3]])

A_inv = np.linalg.inv(A)

print("Matrix A:")
print(A)
print("\nInverse of A:")
print(A_inv)
