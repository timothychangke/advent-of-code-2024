with open('input.txt') as f:
    s = f.read().strip()
    
left, right = [], []
res = 0

for line in s.split('\n'):
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))
left.sort()
right.sort()
res = sum(abs(l - r) for l, r in zip(left, right))
print(res)
