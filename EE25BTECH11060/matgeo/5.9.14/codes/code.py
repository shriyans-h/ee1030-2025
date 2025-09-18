import numpy as np
import matplotlib.pyplot as plt
# Define the lines as functions: m = f(c)
# Line 1: 5c - 4m = 40  -> m = (5c - 40)/4
# Line 2: 5c - 8m = -80 -> m = (5c + 80)/8

# Choose range for c
c = np.linspace(-20, 20, 400)

# Compute m for both lines
m1 = (5*c - 40)/4
m2 = (5*c + 80)/8

# Plot the lines
plt.plot(c, m1, label=r'$5c - 4m = 40$', color='blue')
plt.plot(c, m2, label=r'$5c - 8m = -80$', color='red')

# Labels and title
plt.xlabel('c')
plt.ylabel('m')
plt.title('Graph of Two Lines')
plt.grid(True)
plt.legend()

# Show plot
plt.show()
