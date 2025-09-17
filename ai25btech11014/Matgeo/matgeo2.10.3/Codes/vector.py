import numpy as np

P = np.array([1, -1, 2])
Q = np.array([2, 0, -1])
R = np.array([0, 2, 1])

PQ = Q - P
PR = R - P
N = np.cross(PQ, PR)
unit = N / np.linalg.norm(N)

print("Unit vector:", unit)
