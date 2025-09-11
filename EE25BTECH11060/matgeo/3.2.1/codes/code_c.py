import ctypes
import os

# Load shared object
lib = ctypes.CDLL(os.path.abspath("./triangle.so"))

# Define argument and return types
lib.find_triangle.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double,
                              ctypes.POINTER(ctypes.c_double),
                              ctypes.POINTER(ctypes.c_double),
                              ctypes.POINTER(ctypes.c_double)]

# Function wrapper
def find_triangle(AB, AC, BC):
    x = ctypes.c_double()
    y1 = ctypes.c_double()
    y2 = ctypes.c_double()
    
    lib.find_triangle(AB, AC, BC,
                      ctypes.byref(x), ctypes.byref(y1), ctypes.byref(y2))
    
    return x.value, y1.value, y2.value

# Example usage
if __name__ == "__main__":
    AB, AC, BC = 4.0, 9.0, 6.0   # Example
    x, y1, y2 = find_triangle(AB, AC, BC)
    
    print(f"A = (0,0)")
    print(f"B = ({AB},0)")
    print(f"C1 = ({x:.3f},{y1:.3f})")
    print(f"C2 = ({x:.3f},{y2:.3f})")
