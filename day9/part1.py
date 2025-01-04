with open('input.txt') as file:
    s = file.read().strip()
n = []
c = 0
for i, char in enumerate(s):
    x = int(char)
    if i % 2 == 0:
        n += [c] * x
        c += 1
    else:
        n += ['.'] * x
dots = [i for i, x in enumerate(n) if x == '.']
for i in dots:
    i = int(i)
    while n[-1] == '.': n.pop()
    if len(n) <= i: break
    n[i] = n.pop()
ans = sum(i * int(x) for i, x in enumerate(n) if x != '.')
print(ans)

