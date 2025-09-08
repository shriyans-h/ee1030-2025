import numpy as np
import matplotlib.pyplot as plt

# Define vectors
a = np.array([2.0, 1.0, 3.0])
b = np.array([-1.0, 2.0, 1.0])
c = np.array([3.0, 1.0, 2.0])

# Cross product (NumPy)
bx_c = np.cross(b, c)

# Scalar triple product
scalar_triple = np.dot(a, bx_c)

# Print results
print("b x c =", bx_c)
print("a · (b x c) =", scalar_triple)

# ---------- Image Generation ----------
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def draw_vec(v, color, label):
    ax.quiver(0, 0, 0, v[0], v[1], v[2],
              color=color, arrow_length_ratio=0.1, label=label)

# Draw vectors
draw_vec(a, 'r', 'a')
draw_vec(b, 'g', 'b')
draw_vec(c, 'b', 'c')
draw_vec(bx_c, 'm', 'b × c')

# Axis limits
lim = 4
ax.set_xlim([-lim, lim])
ax.set_ylim([-lim, lim])
ax.set_zlim([-lim, lim])

# Labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.title(f"Scalar triple product = {scalar_triple}")

# Save image
plt.savefig("triple_product_python.png", dpi=300)
plt.show()
