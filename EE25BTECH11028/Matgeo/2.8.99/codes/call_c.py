import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# Part 1: Input vectors
# ==========================================
a = np.array([3.0, 0, 0])   # Along X-axis
b = np.array([0, 4.0, 0])   # Along Y-axis
c = np.array([0, 0, 5.0])   # Along Z-axis

print("---- Part 1: Input Vectors ----")
print("a =", a)
print("b =", b)
print("c =", c)

# ==========================================
# Part 2: Resultant vector calculation
# ==========================================
res = a + b + c
sumSq = np.dot(a, a) + np.dot(b, b) + np.dot(c, c)
result = np.linalg.norm(res)

print("\n---- Part 2: Resultant ----")
print(f"||a + b + c|| = sqrt({sumSq:.0f}) = {result:.4f}")

# ==========================================
# Part 3: Plot vectors
# ==========================================
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.quiver(0, 0, 0, a[0], a[1], a[2], color='r', label='a (3)')
ax.quiver(0, 0, 0, b[0], b[1], b[2], color='g', label='b (4)')
ax.quiver(0, 0, 0, c[0], c[1], c[2], color='b', label='c (5)')
ax.quiver(0, 0, 0, res[0], res[1], res[2], color='k', linewidth=2, label='a+b+c')

# ==========================================
# Part 4: Plot setup and show
# ==========================================
ax.set_xlim([0, 6])
ax.set_ylim([0, 6])
ax.set_zlim([0, 6])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Vector Addition: a + b + c')
ax.legend()

plt.show()
