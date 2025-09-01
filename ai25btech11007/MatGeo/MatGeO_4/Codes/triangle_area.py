import numpy as np

# Coordinates of points A, B, C
A = np.array([1, 2, 3])
B = np.array([2, -1, 4])
C = np.array([4, 5, -1])

# Compute vectors AB and AC
AB = B - A
AC = C - A

# Compute cross product AB x AC
cross = np.cross(AB, AC)

# Compute magnitude of cross product
magnitude = np.linalg.norm(cross)

# Area of triangle = 1/2 * |AB x AC|
area = 0.5 * magnitude

print(f"Area of triangle ABC = {area:.5f}")
