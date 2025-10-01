import numpy as np

P = np.array([1, -1, 2])
Q = np.array([2, 0, -1])
R = np.array([0, 2, 1])

A = Q - P
B = R - P

M = np.array([A, B])
U, S, Vt = np.linalg.svd(M)

N = Vt[-1]  # Null space vector
unit_vector = N / np.linalg.norm(N)
print("Unit vector:", unit_vector)
