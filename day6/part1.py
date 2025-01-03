with open('input.txt') as file:
    s = file.read().strip()
grid = [list(row) for row in s.split('\n')]
ROWS, COLS = len(grid), len(grid[0])
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cx, cy = 0, 0
for i in range(ROWS):
    for j in range(COLS):
        if grid[i][j] in "<>^v":
            cx, cy = i, j
seen = set()
seen.add((cx, cy))
direction_c = 0
while cx in range(ROWS) and cy in range(COLS):
    seen.add((cx, cy))
    while True:
        directions = dirs[direction_c]
        nx, ny = cx + directions[0], cy + directions[1]
        if nx in range(ROWS) and ny in range(COLS) and grid[nx][ny] == '#':
            direction_c = (direction_c + 1) % 4
        else:
            cx, cy = nx, ny
            break
ans = len(seen)
print(ans) 