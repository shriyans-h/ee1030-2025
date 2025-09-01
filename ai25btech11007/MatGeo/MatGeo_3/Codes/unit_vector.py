import numpy as np

# A vector perpendicular to both a and b is (0,1,1)
n = np.array([0, 1, 1], dtype=float)

# Magnitude
mag = np.linalg.norm(n)

# Unit vector
unit = n / mag

print("Unit vector perpendicular to a and b:", unit)
