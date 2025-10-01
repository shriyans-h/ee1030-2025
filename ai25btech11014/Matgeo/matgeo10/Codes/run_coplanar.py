import subprocess

# Input values for a and b
a = 4
b = 9
input_str = f"{a} {b}\n"

# Run compiled C binary
result = subprocess.run(
    ['./coplanar_check'],  # executable name
    input=input_str,
    capture_output=True,
    text=True
)

# Output result
print("Result from C program:")
print(result.stdout.strip())
