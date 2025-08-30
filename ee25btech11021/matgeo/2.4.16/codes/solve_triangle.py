
import ctypes
import numpy as np

# Load the shared object
lib = ctypes.CDLL("./gen_points.so")

# Call the C function to generate points.dat
lib.generate_points(b"points.dat")

# Load points from file
points = np.loadtxt("points.dat")
A, B, C = points

# Function to compute squared distance
def dist2(P, Q):
    return np.sum((P - Q) ** 2)

# Squared lengths
AB2 = dist2(A, B)
BC2 = dist2(B, C)
CA2 = dist2(C, A)

print("Squared lengths:")
print("AB^2 =", AB2, " BC^2 =", BC2, " CA^2 =", CA2)

# Check isosceles (two sides equal)
isosceles = (AB2 == BC2) or (BC2 == CA2) or (CA2 == AB2)
print("Isosceles Triangle:", isosceles)

# Check right angle (Pythagoras theorem)
right_angle = (AB2 + BC2 == CA2) or (BC2 + CA2 == AB2) or (CA2 + AB2 == BC2)
print("Right Angled Triangle:", right_angle)
