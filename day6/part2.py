with open('input.txt') as file:
    s = file.read().strip()
grid = [list(row) for row in s.split('\n')]
ROWS, COLS = len(grid), len(grid[0])
ans = 0
cx = cy = None
for i in range(ROWS):
    for j in range(COLS):
        if grid[i][j] in "^<>v":
            cx, cy = i, j
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


# place obstacles only on path positions as an optimisation to the solution runtime
def get_path():
    arr = []
    d = 0
    x, y = cx, cy
    while x in range(ROWS) and y in range(COLS):
        arr.append((x, y, d))
        dx, dy = dirs[d]
        nx, ny = x + dx, y + dy
        while nx in range(ROWS) and ny in range(COLS) and grid[nx][ny] == '#':
            d = (d + 1) % 4
            dx, dy = dirs[d]
            nx, ny = x + dx, y + dy
        x, y = nx, ny
    return arr
path = get_path()


def isGood(ax, ay):
    prev = grid[ax][ay]
    grid[ax][ay] = '#'
    x, y = cx, cy
    seen = set()
    d = 0
    while x in range(ROWS) and y in range(COLS):
        if (x, y, d) in seen:
            grid[ax][ay] = prev
            return True
        seen.add((x, y, d))
        dx, dy = dirs[d]
        nx, ny = x + dx, y + dy
        while (nx in range(ROWS)) and (ny in range(COLS)) and (grid[nx][ny] == "#"):
            d = (d + 1) % 4
            dx, dy = dirs[d]
            nx, ny = x + dx, y + dy
        x, y = nx, ny
    grid[ax][ay] = prev
    return False

s = set()
for i, j, _ in path[1:]:
    if grid[i][j] == "." and isGood(i, j):
        s.add((i, j))
print(len(s))
