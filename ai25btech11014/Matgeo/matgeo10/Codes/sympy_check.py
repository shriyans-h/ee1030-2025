from sympy import Matrix, symbols

# Define symbolic variables
a, b, c = symbols('a b c')

# Define vectors
A = Matrix([a, a, c])
B = Matrix([1, 0, 1])
C = Matrix([a, c, b])

# Compute difference vectors
AB = A - B
CB = C - B

# Form matrix and reduce
M = Matrix.hstack(AB, CB)
rref, _ = M.rref()

# Check rank
if rref[2,1] == 0:
    print("Vectors lie in a plane")
else:
    print("Not coplanar")
	
