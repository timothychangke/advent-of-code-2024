with open('input.txt') as f:
    s = f.read().strip()

res = 0
grid = [list(line) for line in s.split('\n')]
ROWS, COLS = len(grid), len(grid[0])
adjacent = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for i in range(ROWS):
    for j in range(COLS):
        for dx, dy in adjacent:
            cx, cy = i, j
            string = ""
            for _ in range(4):
                if cx not in range(ROWS) or cy not in range(COLS):
                    break
                string += grid[cx][cy]
                cx += dx
                cy += dy
            if string == 'XMAS':
                res += 1
print(res)