from collections import defaultdict
with open('input.txt') as file:
    s = file.read().strip()
grid = [list(row) for row in s.split('\n')]
ROWS, COLS = len(grid), len(grid[0])
freq = defaultdict(list)
for i in range(ROWS):
    for j in range(COLS):
        if grid[i][j] != '.':
            freq[grid[i][j]].append((i, j))
s = set()
for arr in freq.values():
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                continue
            x1, y1 = arr[i]
            x2, y2 = arr[j]
            xdiff, ydiff = x2 - x1, y2 - y1
            r, c = x1, y1
            while r in range(ROWS) and c in range(COLS):
                s.add((r, c))
                r += xdiff
                c += ydiff
ans = len(s)
print(ans)
