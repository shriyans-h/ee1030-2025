import math

# given area
A = 5 * math.sqrt(6)
print(f"Given area = {A:.2f}")

# possible values of s
s_vals = [5, -11]

for i, s in enumerate(s_vals, start=1):
    p = s + 3   # relation
    q = 4
    r = 2
    print(f"Solution {i}: (p,q,r,s) = ({p},{q},{r},{s})")
