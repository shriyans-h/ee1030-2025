import numpy as np

A = np.array([
    [2, 3, 10],
    [4, 6, 5],
    [6, 9, 20]
], dtype=np.float32)

B = np.array([4, 1, 2], dtype=np.float32)

U, residuals, rank, s = np.linalg.lstsq(A, B, rcond=None)

if residuals.size > 0 and residuals[0] > 1e-6:
    print("System is inconsistent. No exact solution exists.")
else:
    u, v, w = U
    x, y, z = 1/u, 1/v, 1/w
    print(f"x = {x:.3f}, y = {y:.3f}, z = {z:.3f}")

