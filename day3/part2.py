import re
with open('input.txt') as f:
    s = f.read().strip()

valid = re.findall(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))", s)

res = 0
flag = True
for x in valid:
    if x == 'do()':
        flag = True
    elif x == 'don\'t()':
        flag = False
    else:
        if (flag):
            numbers = re.findall(r'\d+', x)
            x, y = list(map(int, numbers))
            res += x * y
print(res)
