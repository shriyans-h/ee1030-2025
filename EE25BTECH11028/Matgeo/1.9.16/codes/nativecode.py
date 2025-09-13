import matplotlib.pyplot as plt

# Define points
A = (-2, 0)
B = (6, 0)
P = (2, 0)

# Create figure and axis
fig, ax = plt.subplots()

# Plot points
ax.plot(A[0], A[1], 'ro', label='A(-2, 0)')
ax.plot(B[0], B[1], 'bo', label='B(6, 0)')
ax.plot(P[0], P[1], 'go', label='P(2, 0)')

# Draw x and y axis
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)

# Add labels for axes
ax.text(7, 0, 'x', fontsize=12, verticalalignment='bottom')
ax.text(0, 2, 'y', fontsize=12, horizontalalignment='left')

# Add text indicating P is equidistant from A and B
ax.text(2, 0.3, 'P is equidistant from A and B', fontsize=10, verticalalignment='bottom', horizontalalignment='left')

# Add point labels
ax.text(A[0], A[1] - 0.3, 'A(-2, 0)', color='red', fontsize=10, horizontalalignment='center')
ax.text(B[0], B[1] - 0.3, 'B(6, 0)', color='blue', fontsize=10, horizontalalignment='center')
ax.text(P[0], P[1] + 0.3, 'P(2, 0)', color='green', fontsize=10, horizontalalignment='center')

# Set limits and aspect
ax.set_xlim(-4, 8)
ax.set_ylim(-1, 3)
ax.set_aspect('equal')

# Hide the ticks
ax.set_xticks([])
ax.set_yticks([])

plt.show()
