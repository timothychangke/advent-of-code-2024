from collections import Counter

with open('input.txt') as f:
    s = f.read().strip()
    
left, right = set(), []
res = 0

for line in s.split('\n'):
    l, r = line.split()
    left.add(int(l))
    right.append(int(r))
for k, v in Counter(right).items():
    if k in left:
        res += k * v
print(res)
