import matplotlib.pyplot as plt

# -------- PART 1: Input & Setup --------
x1, y1 = 3, 2
x2, y2 = -2, -3
x3, y3 = 2, 3
print("PART 1: Points -> A(3,2), B(-2,-3), C(2,3)\n")

# -------- PART 2: Check Collinearity --------
det = x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)
if det == 0:
    print("PART 2: Collinear -> No triangle formed\n")
    print("PART 4: Final Conclusion -> No triangle exists")
    exit()
else:
    print("PART 2: Not Collinear -> Triangle formed\n")

# -------- PART 3: Check Right Angle --------
AB, AC, BC = (x2-x1,y2-y1), (x3-x1,y3-y1), (x3-x2,y3-y2)
right, vertex = False, None

if AB[0]*AC[0]+AB[1]*AC[1]==0: right, vertex = True, "A"
elif AB[0]*BC[0]+AB[1]*BC[1]==0: right, vertex = True, "B"
elif AC[0]*BC[0]+AC[1]*BC[1]==0: right, vertex = True, "C"

if right: print(f"PART 3: Right-angled at {vertex}\n")
else: print("PART 3: No right angle\n")

# -------- PART 4: Final Conclusion + Plot --------
if right:
    print(f"PART 4: Final Conclusion -> Triangle formed, right-angled at {vertex}")
else:
    print("PART 4: Final Conclusion -> Triangle formed, but not right-angled")

X, Y = [x1,x2,x3,x1],[y1,y2,y3,y1]
plt.plot(X,Y,'bo-'); plt.grid(True); plt.gca().set_aspect('equal')
plt.text(x1+0.1,y1+0.1,"A"); plt.text(x2+0.1,y2+0.1,"B"); plt.text(x3+0.1,y3+0.1,"C")
plt.show()
