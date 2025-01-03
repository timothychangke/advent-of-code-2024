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
        for j in range(i + 1, len(arr)):
            x1, y1 = arr[i]
            x2, y2 = arr[j]
            s.add((2 * x1 - x2, 2 * y1 - y2))
            s.add((2 * x2 - x1, 2 * y2 - y1))
print(len([0 for x, y in s if 0 <= x < ROWS and 0 <= y < COLS]))
