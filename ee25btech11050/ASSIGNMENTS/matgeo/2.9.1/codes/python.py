import matplotlib.pyplot as plt

# Triangle points
A = (200, 800)
Q = (200, 0)
C = (-600, 0)

# Square points
P = (-200, 0)
R = (200, 400)
S = (-200, 400)

# Lists for triangle
triangle_x = [A[0], Q[0], C[0], A[0]]
triangle_y = [A[1], Q[1], C[1], A[1]]

# Lists for square
square_x = [P[0], Q[0], R[0], S[0], P[0]]
square_y = [P[1], Q[1], R[1], S[1], P[1]]

plt.figure(figsize=(8, 8))

# Plot triangle
plt.plot(triangle_x, triangle_y, 'r-', label='Triangle')

# Plot square
plt.plot(square_x, square_y, 'b-', label='Square')

# Label triangle points
plt.text(A[0], A[1], 'A')
plt.text(Q[0], Q[1], 'Q')
plt.text(C[0], C[1], 'C')

# Label square points
plt.text(P[0], P[1], 'P')
plt.text(R[0], R[1], 'R')
plt.text(S[0], S[1], 'S')

# Mark and label the origin
plt.scatter([0], [0], marker='x', color='black')
plt.text(0, 0, 'O')

# To match axes and layout
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Solution plot')
plt.xlim(-700, 300)
plt.ylim(-100, 900)
plt.grid(True)
plt.legend()
plt.show()

