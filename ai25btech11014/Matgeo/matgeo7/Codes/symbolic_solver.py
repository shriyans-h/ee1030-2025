from sympy import symbols, Matrix, Eq, solve

k = symbols('k')
A = Matrix([2, 1])
B = Matrix([k, 8])
P = (3 * A + B) / 4
n = Matrix([[2, -1]])
eq = Eq(n @ P, -1)
sol = solve(eq, k)
print(sol[0])
