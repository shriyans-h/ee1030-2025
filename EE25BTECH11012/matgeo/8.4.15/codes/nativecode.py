import numpy as np
import matplotlib.pyplot as plt

# --- 1. Define the fixed base and derive ellipse parameters ---
# Let the fixed base BC be on the x-axis, centered at the origin.
# B = (-k, 0), C = (k, 0). We can choose k=2 for a clear visual.
k = 2
B = np.array([-k, 0])
C = np.array([k, 0])

# The length of the base 'a' is the distance between B and C.
# Note: 'a' here is the side length, not the semi-major axis of the ellipse.
side_a = np.linalg.norm(C - B)  # side_a = 2k = 4

# --- 2. Use the derived condition to find the ellipse's properties ---
# From the solution, we found b + c = 2a.
# b = distance(A, C) and c = distance(A, B).
# So, distance(A, C) + distance(A, B) = 2 * side_a = 2 * (4) = 8.
# This is the definition of an ellipse with foci at B and C.
# The constant sum of distances is 2 * a_ellipse (semi-major axis).
constant_sum = 2 * side_a
a_ellipse = constant_sum / 2  # a_ellipse = side_a = 4

# The distance from the center to a focus is c_ellipse.
c_ellipse = k  # c_ellipse = 2

# For an ellipse, a_ellipse^2 = b_ellipse^2 + c_ellipse^2
b_ellipse = np.sqrt(a_ellipse**2 - c_ellipse**2)  # Semi-minor axis

# --- 3. Generate points for the ellipse (locus of A) ---
t = np.linspace(0, 2 * np.pi, 300)
x_ellipse = a_ellipse * np.cos(t)
y_ellipse = b_ellipse * np.sin(t)

# --- 4. Create the plot ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 8))

# Plot the locus of A
ax.plot(x_ellipse, y_ellipse, label='Locus of Vertex A (Ellipse)', color='dodgerblue', linewidth=2)

# Plot the fixed base BC and foci
ax.plot([B[0], C[0]], [B[1], C[1]], 'o', markersize=8, color='red', label='Foci (Fixed Base BC)')
ax.text(B[0], B[1] - 0.5, f'B({B[0]}, {B[1]})', ha='center', fontsize=12)
ax.text(C[0], C[1] - 0.5, f'C({C[0]}, {C[1]})', ha='center', fontsize=12)

# --- 5. Illustrate with an example triangle ---
# Choose an example point A on the ellipse (e.g., at t = 2π/5)
t_example = 2 * np.pi / 5
A_example = np.array([a_ellipse * np.cos(t_example), b_ellipse * np.sin(t_example)])

# Draw the triangle ABC
triangle_x = [A_example[0], B[0], C[0], A_example[0]]
triangle_y = [A_example[1], B[1], C[1], A_example[1]]
ax.plot(triangle_x, triangle_y, 'g--', label='Example Triangle ABC', linewidth=1.5)
ax.plot(A_example[0], A_example[1], 'go', markersize=6)
ax.text(A_example[0], A_example[1] + 0.3, 'A(x, y)', ha='center', fontsize=12)

# Verify the condition for the example point and display it
side_b = np.linalg.norm(A_example - C)
side_c = np.linalg.norm(A_example - B)
info_text = (
    f"Condition:  $b + c = 2a$\n\n"
    f"Side $a$ (distance BC) = {side_a:.2f}\n"
    f"Side $b$ (distance AC) = {side_b:.2f}\n"
    f"Side $c$ (distance AB) = {side_c:.2f}\n\n"
    f"Check:  ${side_b:.2f} + {side_c:.2f} = {side_b + side_c:.2f}$\n"
    f"Required: $2 \\times a = 2 \\times {side_a:.2f} = {2 * side_a:.2f}$"
)
ax.text(0.95, 0.05, info_text, transform=ax.transAxes, fontsize=11,
        verticalalignment='bottom', horizontalalignment='right',
        bbox=dict(boxstyle='round,pad=0.5', fc='aliceblue', alpha=0.9))

# --- 6. Finalize the plot ---
ax.set_aspect('equal', adjustable='box')
ax.set_title('Locus of Vertex A is an Ellipse', fontsize=16)
ax.set_xlabel('x-axis', fontsize=12)
ax.set_ylabel('y-axis', fontsize=12)
ax.legend(loc='upper left')
plt.show()

