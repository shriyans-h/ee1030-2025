import math

print("Q. Find the slope of the lines")

# 1) Passing through (3, -2) and (-1, 4)
x1, y1 = 3, -2
x2, y2 = -1, 4
l, m = x2 - x1, y2 - y1   # direction ratios
if l != 0:
    slope1 = m / l
    print(f"1) Through (3,-2) & (-1,4): direction ratios = ({l}, {m}), slope = {slope1:.2f}")
else:
    print("1) Through (3,-2) & (-1,4): slope undefined")

# 2) Passing through (3, -2) and (7, -2)
x1, y1 = 3, -2
x2, y2 = 7, -2
l, m = x2 - x1, y2 - y1
if l != 0:
    slope2 = m / l
    print(f"2) Through (3,-2) & (7,-2): direction ratios = ({l}, {m}), slope = {slope2:.2f}")
else:
    print("2) Through (3,-2) & (7,-2): slope undefined")

# 3) Passing through (3, -2) and (3, 4)
x1, y1 = 3, -2
x2, y2 = 3, 4
l, m = x2 - x1, y2 - y1
if l != 0:
    slope3 = m / l
    print(f"3) Through (3,-2) & (3,4): direction ratios = ({l}, {m}), slope = {slope3:.2f}")
else:
    print("3) Through (3,-2) & (3,4): direction ratios = (0, {m}), slope undefined (vertical line)")

# 4) Line making inclination 60° with positive x-axis
theta = math.radians(60)
slope4 = math.tan(theta)
print(f"4) Line inclined at 60° to x-axis: slope = {slope4:.2f}")
