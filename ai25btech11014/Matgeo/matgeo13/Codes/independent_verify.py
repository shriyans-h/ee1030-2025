from sympy import symbols, Eq, simplify

a, b, c = symbols('a b c')

# Harmonic progression condition: 2/b = 1/a + 1/c
hp = Eq(2/b, 1/a + 1/c)

# Multiply both sides by abc
lhs = simplify(2*a*c)
rhs = simplify(a*b + b*c)

print("ab + bc =", rhs)
print("2ac =", lhs)
print("Condition holds:", lhs == rhs)
