import matplotlib.pyplot as plt

# Points
A = (3, 2)
B = (-2, -3)
C = (2, 3)

# Plotting lines connecting the points
plt.plot([B[0], A[0]], [B[1], A[1]], 'b-')  # Line B to A
plt.plot([B[0], C[0]], [B[1], C[1]], 'b-')  # Line B to C
plt.plot([A[0], C[0]], [A[1], C[1]], 'b-')  # Line A to C
# Mark points
plt.plot(A[0], A[1], 'ko')
plt.plot(B[0], B[1], 'ko')
plt.plot(C[0], C[1], 'ko')

# Label points
plt.text(A[0] + 0.1, A[1], 'A(3,2)')
plt.text(B[0] - 1.5, B[1], 'B(-2,-3)')
plt.text(C[0] - 1, C[1], 'C(2,3)')

# Axes labels
plt.xlabel('x')
plt.ylabel('y')

# Grid and axis lines
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.title('Graph of Points A, B, C')
plt.show()

