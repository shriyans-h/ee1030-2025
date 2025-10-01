import subprocess

input_str = "4 1"

result = subprocess.run(
    ['./reflect_translate'],  # Make sure this matches your compiled C binary
    input=input_str,
    capture_output=True,
    text=True
)

print(result.stdout.strip())
