import matplotlib.pyplot as plt

def create_plot():
    # Points A, P, and B
    A = (-2, 0)
    P = (2, 0)
    B = (6, 0)

    fig, ax = plt.subplots(figsize=(8, 3))

    # Plot points
    ax.plot(A[0], A[1], 'ro')  # red
    ax.plot(P[0], P[1], 'go')  # green
    ax.plot(B[0], B[1], 'bo')  # blue

    # Labels below points
    ax.text(A[0], A[1] - 0.25, r'$A(-2,0)$', color='red', ha='center', fontsize=12)
    ax.text(P[0], P[1] - 0.25, r'$P(2,0)$', color='green', ha='center', fontsize=12)
    ax.text(B[0], B[1] - 0.25, r'$B(6,0)$', color='blue', ha='center', fontsize=12)

    # Dashed line between A and B
    ax.plot([A[0], B[0]], [A[1], B[1]], 'k--', linewidth=1)

    # Annotation above dashed line
    ax.text(2, 0.3, r'$P$ is equidistant from $A$ and $B$', fontsize=12, style='italic', ha='center')

    # Draw x and y axis arrows
    ax.arrow(-4, 0, 12, 0, head_width=0.15, head_length=0.3, fc='black', ec='black', length_includes_head=True)
    ax.arrow(0, -1, 0, 2, head_width=0.15, head_length=0.3, fc='black', ec='black', length_includes_head=True)

    # Axis labels
    ax.text(7.9, -0.15, 'x', fontsize=12)
    ax.text(-0.2, 1.8, 'y', fontsize=12)

    # Remove ticks and spines except left and bottom
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)

    # Set limits and aspect
    ax.set_xlim(-4, 8)
    ax.set_ylim(-1, 2)
    ax.set_aspect('equal')

    return fig, ax

def add_caption_and_show(fig):
    # Add caption below figure
    fig.text(0.5, 0.02, 'Fig. 0', ha='center', fontsize=14, weight='bold')
    plt.show()

if __name__ == "__main__":
    fig, ax = create_plot()
    add_caption_and_show(fig)
