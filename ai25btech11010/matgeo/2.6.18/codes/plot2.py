import os
import matplotlib.pyplot as plt

# Run the C program
# On Windows use: os.system("triangle.exe")
os.system("./triangle")  # Linux/Mac

# Read points and area from points.dat
points = {}
area = 0
with open("points.dat", "r") as file:
    for line in file:
        line = line.strip()
        if line.startswith("A:"):
            x, y = map(float, line[2:].split())
            points['A'] = (x, y)
        elif line.startswith("B:"):
            x, y = map(float, line[2:].split())
            points['B'] = (x, y)
        elif line.startswith("C:"):
            x, y = map(float, line[2:].split())
            points['C'] = (x, y)
        elif line.startswith("Area"):
            area = float(line.split(":")[1])

print(f"Read Area from C program: {area}")
print("Triangle Points:", points)

# Prepare triangle points for plotting
triangle_coords = [points['A'], points['B'], points['C'], points['A']]  # close the triangle
x_vals, y_vals = zip(*triangle_coords)

# Create figs folder if it doesn't exist
os.makedirs('figs', exist_ok=True)

# Plot
plt.plot(x_vals, y_vals, 'b-o', label='Triangle')
plt.fill(x_vals, y_vals, 'skyblue', alpha=0.3)

# Label points
for label, coord in points.items():
    plt.text(coord[0], coord[1], label, fontsize=12, color='red')

plt.title(f'Triangle Plot (Area = {area})')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.legend()

# Save the plot in figs folder
plt.savefig('../figs/triangle_plot1.png', dpi=300)
print("Triangle plot saved in figs/triangle_plot.png")
plt.show()

