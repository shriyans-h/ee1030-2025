import numpy as np
import matplotlib.pyplot as plt
import math

def read_vector_data(filename):
    """Read vector data from the .dat file"""
    with open(filename, 'r') as f:
        lines = f.readlines()

    # Skip comment lines (starting with #)
    data_line = None
    for line in lines:
        if not line.strip().startswith('#') and line.strip():
            data_line = line.strip()
            break

    if data_line is None:
        raise ValueError("No data found in file")

    # Parse the data: a_x a_y b_x b_y c_x c_y theta
    values = list(map(float, data_line.split()))

    return {
        'a': np.array([values[0], values[1]]),
        'b': np.array([values[2], values[3]]),
        'c': np.array([values[4], values[5]]),
        'theta': values[6]
    }

def plot_vectors(data):
    """Create visualization of vectors a, b, and c"""
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))

    # Extract vectors
    a = data['a']
    b = data['b']
    c = data['c']
    theta = data['theta']

    # Plot vectors from origin
    # Vector a (red)
    ax.quiver(0, 0, a[0], a[1], angles='xy', scale_units='xy', scale=1, 
              color='red', width=0.006, label='Vector a', linewidth=2)

    # Vector b (blue) - only once from origin
    ax.quiver(0, 0, b[0], b[1], angles='xy', scale_units='xy', scale=1, 
              color='blue', width=0.006, label='Vector b', linewidth=2)

    # Vector c (green) - resultant
    ax.quiver(0, 0, c[0], c[1], angles='xy', scale_units='xy', scale=1, 
              color='green', width=0.006, label='Vector c (a+b)', linewidth=2)

    # Draw angle arc between vectors a and b
    angle_radius = min(np.linalg.norm(a), np.linalg.norm(b)) * 0.3
    angle_arc = np.linspace(0, theta, 50)
    arc_x = angle_radius * np.cos(angle_arc)
    arc_y = angle_radius * np.sin(angle_arc)
    ax.plot(arc_x, arc_y, 'k-', linewidth=1.5)

    # Add angle label (just θ without specific value)
    mid_angle = theta / 2
    label_radius = angle_radius * 1.3
    label_x = label_radius * np.cos(mid_angle)
    label_y = label_radius * np.sin(mid_angle)
    ax.text(label_x, label_y, 'θ', 
            fontsize=14, ha='center', va='center', weight='bold')

    # Add vector magnitude labels
    ax.text(a[0]/2, a[1]/2 - 0.3, f'|a| = {np.linalg.norm(a):.1f}', 
            fontsize=10, ha='center', color='red', weight='bold')
    ax.text(b[0]/2 - 0.3, b[1]/2, f'|b| = {np.linalg.norm(b):.1f}', 
            fontsize=10, ha='center', color='blue', weight='bold')
    ax.text(c[0]/2, c[1]/2 + 0.3, f'|c| = {np.linalg.norm(c):.1f}', 
            fontsize=10, ha='center', color='green', weight='bold')

    # Set equal aspect ratio and grid
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper right', fontsize=11)

    # Set axis limits with some padding
    max_coord = max(np.max(np.abs(a)), np.max(np.abs(b)), np.max(np.abs(c))) * 1.2
    ax.set_xlim(-1, max_coord)
    ax.set_ylim(-1, max_coord)

    # Labels and title
    ax.set_xlabel('X', fontsize=12)
    ax.set_ylabel('Y', fontsize=12)
    ax.set_title('Vectors a, b, c', fontsize=14, weight='bold')

    # Save the figure
    plt.tight_layout()
    plt.savefig('fig1.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("Vector visualization saved as fig1.png")
    print(f"Vector a: ({a[0]:.3f}, {a[1]:.3f}), |a| = {np.linalg.norm(a):.3f}")
    print(f"Vector b: ({b[0]:.3f}, {b[1]:.3f}), |b| = {np.linalg.norm(b):.3f}")
    print(f"Vector c: ({c[0]:.3f}, {c[1]:.3f}), |c| = {np.linalg.norm(c):.3f}")
    print(f"Angle θ: {math.degrees(theta):.1f}°")

# Main execution
if __name__ == "__main__":
    try:
        # Read vector data from file
        vector_data = read_vector_data('vectors.dat')

        # Create visualization
        plot_vectors(vector_data)

    except FileNotFoundError:
        print("Error: vectors.dat file not found!")
        print("Please run the C program first to generate the data file.")
    except Exception as e:
        print(f"Error: {e}")
