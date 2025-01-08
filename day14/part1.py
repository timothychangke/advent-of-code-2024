import re
with open('input.txt') as file:
    s = file.read().strip()
after = []
for robot in s.split('\n'):
    px, py, vx, vy = map(int, re.findall(r"-?\d+", robot))
    after.append(((px + vx * 100) % 101, (py + vy * 100) % 103))
quads = [0] * 4
xm = (101 - 1) // 2
ym = (103 - 1) // 2
for x, y in after:
    if x == xm or y == ym: continue
    if x < xm:
        if y < ym:
            quads[0] += 1
        else:
            quads[1] += 1
    else:
        if y < ym:
            quads[2] += 1
        else:
            quads[3] += 1
ans = 1
for q in quads:
    ans *= q
print(ans) 