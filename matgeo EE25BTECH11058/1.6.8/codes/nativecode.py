import matplotlib.pyplot as plt

# Step 1: Find x such that the points are collinear
# Area formula = 0 for collinear points:
# | x1(y2-y3) + x2(y3-y1) + x3(y1-y2) | = 0

# Points: (x, -1), (2, 1), (4, 5)
# Substitute:
# x*(-1 - 5) + 2*(5 + 1) + 4*(-1 - 1) = 0
# x*(-6) + 12 + (-8) = 0
# -6x + 4 = 0 --> x = 2/3

x = 2  # Correct value as derived

# Step 2: Prepare points for plotting
points_x = [x, 2, 4]
points_y = [-1, 1, 5]

# Step 3: Plotting
plt.figure(figsize=(6, 6))
plt.scatter(points_x, points_y, color='red', zorder=5)

# Draw the straight line through all points
plt.plot(points_x, points_y, '--b', label='Collinear points')

# Annotate each point
for px, py in zip(points_x, points_y):
    plt.annotate(f'({px},{py})', (px, py), textcoords="offset points", xytext=(10,5), ha='center')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of Collinear Points')
plt.grid(True)
plt.legend()
plt.xlim(0, 5)
plt.ylim(-2, 6)
plt.show()