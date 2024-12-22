with open('input.txt') as f:
    s = f.read().strip()


def checkXmas(r, c):
    patterns = [[(r, c, 'A'), (r - 1, c - 1, 'M'), (r + 1, c - 1, 'M'),
                 (r - 1, c + 1, 'S'), (r + 1, c + 1, 'S')],
                [(r, c, 'A'), (r - 1, c - 1, 'M'), (r - 1, c + 1, 'M'),
                 (r + 1, c - 1, 'S'), (r + 1, c + 1, 'S')],
                [(r, c, 'A'), (r - 1, c + 1, 'M'), (r + 1, c + 1, 'M'),
                 (r - 1, c - 1, 'S'), (r + 1, c - 1, 'S')],
                [(r, c, 'A'), (r + 1, c + 1, 'M'), (r + 1, c - 1, 'M'),
                 (r - 1, c - 1, 'S'), (r - 1, c + 1, 'S')]]
    for pattern in patterns:
        if all(x in range(ROWS) and y in range(COLS) and char == grid[x][y] for x, y, char in pattern):
            return True
    return False


res = 0
grid = [list(line) for line in s.split('\n')]
ROWS, COLS = len(grid), len(grid[0])

for i in range(ROWS):
    for j in range(COLS):
        if grid[i][j] == 'A' and checkXmas(i, j):
            res += 1
print(res)
