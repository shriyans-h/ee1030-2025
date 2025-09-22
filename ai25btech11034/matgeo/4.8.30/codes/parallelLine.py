import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

# Given data
A = np.array([2, 3, 2])       # Point on line 1
a2 = np.array([-2, 3, 0])     # Point on line 2
b = np.array([2, -3, 6])      # Direction vector (common)

# Compute shortest distance using projection method
diff = a2 - A
numerator = np.linalg.norm(np.cross(diff, b))
denominator = np.linalg.norm(b)
d = numerator / denominator

print("Shortest distance between the two parallel lines =", d)

# -------- Find foot of perpendicular --------
# Unit normal perpendicular to b in plane (diff, b)
n = np.cross(diff, b)
n = n / np.linalg.norm(n)

# Projection of diff onto n gives the perpendicular segment
perp_vec = np.dot(diff, n) * n
P1 = A                           # Point on Line 1
P2 = A + perp_vec                 # Closest point on Line 2

# -------- Plotting --------
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Range of parameter for plotting lines
t = np.linspace(-2, 2, 50)

# Line 1: through A
L1 = A.reshape(3,1) + np.outer(b, t)

# Line 2: through a2
L2 = a2.reshape(3,1) + np.outer(b, t)

# Plot both lines
ax.plot(L1[0], L1[1], L1[2], label="Line 1", color="blue")
ax.plot(L2[0], L2[1], L2[2], label="Line 2", color="red")

# Mark given points
ax.scatter(*A, color="blue", s=50, marker="o", label="Point A (Line 1)")
ax.scatter(*a2, color="red", s=50, marker="^", label="Point (Line 2)")

# Plot shortest distance segment
ax.plot([P1[0], P2[0]], [P1[1], P2[1]], [P1[2], P2[2]], 
        color="green", linestyle="--", linewidth=2, label="Shortest Distance")

# Formatting
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("Shortest Distance Between Two Parallel Lines")
ax.legend()
ax.grid(True)

# -------- Save the figure --------
save_path = os.path.join("..", "figures", "parallel_lines.png")
plt.savefig(save_path, dpi=300, bbox_inches="tight")

plt.show()

