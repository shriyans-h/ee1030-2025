import numpy as np
import matplotlib.pyplot as plt

a = 6
b = 8
c = (a**2 + b**2)**0.5  # Hypotenuse calculation

# Coordinates for triangle at (0,0), (a,0), (0,b)
pts = np.array([[0,0], [a,0], [0,b], [0,0]])

plt.figure(figsize=(5,5))
plt.plot(pts[:,0], pts[:,1], '-o', label='Triangle')
plt.text(a/2, -0.5, f'{a} cm', ha='center')
plt.text(-0.5, b/2, f'{b} cm', va='center', rotation=90)
plt.text(a/2, b/2, f'{c:.2f} cm', color='purple')
plt.axis('equal')
plt.grid(True)
plt.title('Right Triangle: sides 6 cm and 8 cm')
plt.xlabel('cm')
plt.ylabel('cm')
plt.legend()
plt.savefig('right_triangle.png')
plt.show()
