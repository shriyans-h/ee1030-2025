import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


angle_deg = 30

angle_rad = np.radians(angle_deg)

x = np.cos(angle_rad)
y = np.sin(angle_rad)
z = 0  

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the vector
ax.quiver(0, 0, 0, x, y, z, color='r', label=f'Unit vector at {angle_deg}°')
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])

# Plot the axes
ax.plot([0, 1], [0, 0], [0, 0], color='b', label="X-axis")  # X axis
ax.plot([0, 0], [0, 1], [0, 0], color='g', label="Y-axis")  # Y axis
ax.plot([0, 0], [0, 0], [0, 1], color='y', label="Z-axis")  # Z axis

# Labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Unit Vector in XY Plane at 30°')

# Show the plot
plt.legend()
plt.show()
