import re

# Read input
with open('input.txt') as f:
    s = f.read().strip()

# Extract all mul(x, y) pattern matches
valid = re.findall(r"mul\((\d+),(\d+)\)", s)

res = 0
for x, y in valid:
    x, y = int(x), int(y)  # Convert to integers
    res += x * y  # Accumulate the product

print(res)
