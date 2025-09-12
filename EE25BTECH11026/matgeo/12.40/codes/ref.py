import ctypes
import sympy as sp

# Load library
lib = ctypes.CDLL("./libref_solver.so")

# Prepare result buffer (3x3 = 9 doubles)
result = (ctypes.c_double * 9)()
lib.solve_ref(result)

# Convert to SymPy Matrix
ref = sp.Matrix(3, 3, result)
print("Row Echelon Form (REF):")
sp.pprint(ref)

