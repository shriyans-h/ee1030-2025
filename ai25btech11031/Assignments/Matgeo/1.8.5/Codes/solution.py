import numpy as np

# Define points A and B
A = np.array([3, 4, 5])
B = np.array([-1, 3, -7])

# Compute vector sum A+B
AplusB = A + B

# Compute dot products |A|^2 and |B|^2
A_dot = np.dot(A, A)
B_dot = np.dot(B, B)

print("Vector form equation of locus P satisfies:")
print("2 * (P · P) - 2 * (A+B) · P + |A|^2 + |B|^2 = K^2")
print("where")
print(f"A + B = ({AplusB[0]:.1f}, {AplusB[1]:.1f}, {AplusB[2]:.1f}),")
print(f"|A|^2 = {A_dot:.1f}, |B|^2 = {B_dot:.1f}")
