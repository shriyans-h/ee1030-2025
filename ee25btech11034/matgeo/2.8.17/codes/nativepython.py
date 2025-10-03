import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy

# 1. Define l, m, n as symbolic variables
l, m, n = sympy.symbols('l m n')

# 2. Define the two equations
eq1 = sympy.Eq(2*l + 2*m - n, 0)
eq2 = sympy.Eq(m*n + n*l + l*m, 0)
# 3. Solve the linear equation for n and substitute it into the quadratic equation
n_solution = sympy.solve(eq1, n)[0]
eq2_substituted = eq2.subs(n, n_solution)
# 4. Factor the resulting quadratic equation
factored_eq = sympy.factor(eq2_substituted.lhs)
print("-" * 40)

# This gives two conditions, one for each line.

# 5. Find the symbolic direction vector for each case
# Case 1: The first factor is zero
m_sol1 = sympy.solve(factored_eq.args[0], m)[0] # m = -2*l
n_sol1 = n_solution.subs(m, m_sol1)
# The first direction vector is proportional to (l, -2*l, -2*l)
d1 = sympy.Matrix([l, m_sol1, n_sol1])

# Case 2: The second factor is zero
l_sol2 = sympy.solve(factored_eq.args[1], l)[0] # l = -2*m
n_sol2 = n_solution.subs(l, l_sol2)
# The second direction vector is proportional to (-2*m, m, -2*m)
d2 = sympy.Matrix([l_sol2, m, n_sol2])

# 6. Verify perpendicularity by calculating the dot product
dot_product = d1.dot(d2)
print(f"The symbolic dot product is: {dot_product}")

if dot_product == 0:
    print(" The dot product is identically zero, so the lines are always perpendicular.")
else:
    print(" The lines are not perpendicular.")

d1_symbolic = sympy.Matrix([l, -2*l, -2*l])
d2_symbolic = sympy.Matrix([-2*m, m, -2*m])

# --- Substitute numerical values for plotting ---
# For Line 1, we substitute l=1
d1_numeric = np.array(d1_symbolic.subs(l, 1).evalf(), dtype=float).flatten()
# For Line 2, we substitute m=1
d2_numeric = np.array(d2_symbolic.subs(m, 1).evalf(), dtype=float).flatten()

# --- Plotting Code (requires numerical vectors) ---
# Create the figure and a 3D subplot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Generate points for the lines
t = np.linspace(-3, 3, 100)
line1_points = d1_numeric[:, np.newaxis] * t
line2_points = d2_numeric[:, np.newaxis] * t

# Plot the two lines
ax.plot(line1_points[0], line1_points[1], line1_points[2], color='blue')
ax.plot(line2_points[0], line2_points[1], line2_points[2], color='red')
ax.text(line1_points[0, -1] * 1.1, 
        line1_points[1, -1] * 1.1, 
        line1_points[2, -1] * 1.1, 
        "Line 1", 
        color='blue',
        fontsize=12)

ax.text(line2_points[0, -1] * 1.1, 
        line2_points[1, -1] * 1.1, 
        line2_points[2, -1] * 1.1, 
        "Line 2", 
        color='red',
        fontsize=12)

# Plot the origin
ax.scatter(0, 0, 0, color='black', s=50, label='Origin')

# Set plot labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Visualization of the Two Perpendicular Lines')

# Set equal aspect ratio for accurate visualization
ax.set_aspect('equal', adjustable='box')

plt.show()
