with open('input.txt') as file:
    s = file.read().strip()
grid_string, path = s.split('\n\n')
grid = [list(row) for row in grid_string.split('\n')]
path = "".join(path.splitlines())
ROW, COL = len(grid), len(grid[0])

cr, cc = 0, 0
for i in range(ROW):
    for j in range(COL):
        if grid[i][j] == '@':
            cr, cc = i, j
for p in path:

    dc = {'<': -1, '>': 1}.get(p, 0)
    dr = {'^': -1, 'v': 1}.get(p, 0)
    tr, tc = cr, cc
    go = True
    obs = []
    while True:
        tr += dr
        tc += dc
        sym = grid[tr][tc]
        if sym == '#':
            go = False
            break
        if sym == 'O':
            obs.append((tr, tc))
        if sym == '.':
            break
    if not go:
        continue
    grid[cr][cc] = '.'
    grid[cr + dr][cc + dc] = '@'
    for br, bc in obs:
        grid[br + dr][bc + dc] = 'O'
    cr += dr
    cc += dc

for row in grid:
    print(*row, sep='')

ans = sum((100 * i + j) for i in range(ROW)
          for j in range(COL) if grid[i][j] == 'O')
print(ans)
