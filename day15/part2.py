with open('input.txt') as file:
    s = file.read().strip()
grid, path = s.split('\n\n')
path = path.replace('\n', '')
expansion = {".": "..", "O": "[]", "#": "##", "@": "@."}
grid = [list("".join(expansion[char] for char in line))
        for line in grid.split('\n')]
ROWS, COLS = len(grid), len(grid[0])
cr = cc = 0
for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c] == '@':
            cr, cc = r, c
for move in path:
    dr = {'^': -1, 'v': 1}.get(move, 0)
    dc = {'>': 1, '<': -1}.get(move, 0)
    obs = [(cr, cc)]
    go = True
    for r, c in obs:
        tr = r + dr
        tc = c + dc
        if (tr, tc) in obs: continue
        sym = grid[tr][tc]
        if sym == '#':
            go = False
            break
        if sym == '[':
            obs.append((tr, tc))
            obs.append((tr, tc + 1))
        if sym == ']':
            obs.append((tr, tc))
            obs.append((tr, tc - 1))
    if not go: continue
    grid_copy = [list(row) for row in grid]
    grid[cr][cc] = '.'
    grid[cr + dr][cc + dc] = '@'
    for br, bc in obs[1:]:
        grid[br][bc] = '.'
    for br, bc in obs[1:]:
        grid[br + dr][bc + dc] = grid_copy[br][bc]
    cr += dr
    cc += dc
ans = sum(100 * r + c for r in range(ROWS) for c in range(COLS) if grid[r][c] == '[')
print(ans)
        