from ctypes import * 
import matplotlib.pyplot as plt

# Load the C shared library
lib = CDLL("./2.9.1.so")  # Ensure path matches your compiled output

class Point(Structure):
    _fields_ = [("x", c_int), ("y", c_int)]

triangle = (Point * 3)()
square = (Point * 4)()

lib.get_triangle(triangle)
lib.get_square(square)

tri_x = [triangle[i].x for i in range(3)] + [triangle[0].x]
tri_y = [triangle[i].y for i in range(3)] + [triangle[0].y]

sqr_x = [square[i].x for i in range(4)] + [square[0].x]
sqr_y = [square[i].y for i in range(4)] + [square[0].y]

plt.figure(figsize=(8, 8))
plt.plot(tri_x, tri_y, 'r-', label='Triangle')
plt.plot(sqr_x, sqr_y, 'b-', label='Square')

# Annotate triangle points
labels_tri = ['A', 'Q', 'C']
for i in range(3):
    plt.text(triangle[i].x, triangle[i].y, labels_tri[i])

# Annotate square points
labels_sqr = ['P', 'Q', 'R', 'S']
for i in range(4):
    plt.text(square[i].x, square[i].y, labels_sqr[i])

plt.scatter([0], [0], marker='x', color='black')
plt.text(0, 0, 'O', fontsize=12)
plt.xlim(-700, 300)
plt.ylim(-100, 900)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Solution plot')
plt.grid(True)
plt.legend()
plt.show()


