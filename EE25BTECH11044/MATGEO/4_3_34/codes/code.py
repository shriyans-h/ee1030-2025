import numpy as np
import matplotlib.pyplot as plt

# Define coefficient matrix and RHS
A = np.array([[2, -3],
              [4, -5]], dtype=float)
B = np.array([1, 1], dtype=float)

# Solve for u and v using numpy.linalg.solve
u, v = np.linalg.solve(A, B)

# Recover a and b
a = 1 / u
b = 1 / v

print(f"Solution: a = {a}, b = {b}")

# Define line equation: x/a + y/b = 1 -> y = b*(1 - x/a)
x = np.linspace(-6, 6, 400)
y = b * (1 - x/a)

# Given points
points = [(2, -3), (4, -5)]
px, py = zip(*points)

# Plot
plt.figure(figsize=(6,6))
plt.plot(x, y, label=rf"$\frac{{x}}{{{a:.0f}}} + \frac{{y}}{{{b:.0f}}} = 1$", color="blue")
plt.scatter(px, py, color="red", zorder=5, label="Given points")

# Mark points
for (xi, yi) in points:
    plt.text(xi+0.2, yi, f"({xi},{yi})", fontsize=10, color="black")

# Plot intercepts
plt.scatter([a, 0], [0, b], color="green", zorder=5, label="Intercepts")
plt.text(a+0.2, 0.2, f"({a:.0f},0)", color="green")
plt.text(0.2, b+0.2, f"(0,{b:.0f})", color="green")

# Add slope-intercept equation annotation
plt.text(-5.5, 4.5, r"$y = -x - 1$", fontsize=12, color="purple", bbox=dict(facecolor="white", alpha=0.6))

# Axes settings
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.xlim(-6, 6)
plt.ylim(-6, 6)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.title("Line passing through given points")
plt.show()
