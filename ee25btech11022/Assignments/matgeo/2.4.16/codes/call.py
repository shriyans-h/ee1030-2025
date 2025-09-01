# call.py
import ctypes

lib = ctypes.CDLL('./libcode.so')

# Perpendicularity check from C
result = lib.check_perpendicular()
print("The lines are perpendicular." if result else "The lines are not perpendicular.")

# Extract and print the points
arr = (ctypes.c_double * 12)()
lib.get_points(arr)
for i in range(4):
    print(f"Point {chr(65 + i)}: ({arr[i*3]}, {arr[i*3 + 1]}, {arr[i*3 + 2]})")

