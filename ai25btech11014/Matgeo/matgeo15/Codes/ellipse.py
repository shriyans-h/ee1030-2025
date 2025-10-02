from sympy import Rational, symbols, solve, Eq

e = Rational(2, 3)
l = 5
a = symbols('a')

b2 = a**2 * (1 - e**2)
eq = Eq(2 * b2 / a, l)
a_val = solve(eq, a)[0]
b2_val = a_val**2 * (1 - e**2)

print("a =", a_val)
print("b² =", b2_val)
print("V = [[{:.6f}, 0], [0, {:.6f}]]".format(
    1 / a_val**2, 1 / b2_val))

