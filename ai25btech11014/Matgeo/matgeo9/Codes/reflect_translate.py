from sympy import Matrix

P = Matrix([4, 1])
R_mat = Matrix([[0, 1], [1, 0]])
R = R_mat * P

T = Matrix([2, 0])
F = R + T

print("Reflected point:", R)
print("Final point:", F)
