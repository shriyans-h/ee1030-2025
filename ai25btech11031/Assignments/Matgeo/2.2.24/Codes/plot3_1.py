import numpy as np
import matplotlib.pyplot as plt

# Define the points
A = np.array([1, 1, 1])
B = np.array([2, 5, 0])
C = np.array([3, 2, -3])
D = np.array([1, -6, -1])

# Vectors
AB = B - A
CD = D - C

# Compute angle using dot product
dot_product = np.dot(AB, CD)
norms = np.linalg.norm(AB) * np.linalg.norm(CD)
cos_theta = dot_product / norms
theta = np.degrees(np.arccos(cos_theta))

print("Vector AB:", AB)
print("Vector CD:", CD)
print("Dot product =", dot_product)
print("cos(theta) =", cos_theta)
print("Angle between AB and CD =", theta, "degrees")

# Create 3D plot
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# Plot points
ax.scatter(*A, color='red', label='A(1,1,1)')
ax.scatter(*B, color='red', label='B(2,5,0)')
ax.scatter(*C, color='green', label='C(3,2,-3)')
ax.scatter(*D, color='green', label='D(1,-6,-1)')

# Plot vectors AB and CD
ax.quiver(*A, *AB, color='red', arrow_length_ratio=0.1, linewidth=2, label="AB")
ax.quiver(*C, *CD, color='green', arrow_length_ratio=0.1, linewidth=2, label="CD")

# Labels and formatting
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("Vectors AB and CD (Collinear)")
ax.legend()

# Save and show plot
plt.savefig("collinear_vectors.png", dpi=300)  # Save the figure
plt.show()

