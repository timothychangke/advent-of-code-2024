from collections import deque
with open('input.txt') as file:
    s = file.read().strip()
grid = [[int(x) for x in row] for row in s.split('\n')]
ROWS, COLS = len(grid), len(grid[0])
trailheads = [(r, c) for r in range(ROWS) for c in range(COLS) if grid[r][c] == 0]

def bfs(x, y):
    seen = {(x, y): 1}
    q = deque([(x, y)])
    trails = 0
    while q:
        cx, cy = q.popleft()
        if grid[cx][cy] == 9:
            trails += seen[(cx, cy)]
        for nx, ny in [(cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)]:
           if nx not in range(ROWS) or ny not in range(COLS): continue
           if grid[cx][cy] + 1 != grid[nx][ny]: continue
           if (nx, ny) in seen:
               seen[(nx, ny)] += seen[(cx, cy)]
               continue
           seen[(nx, ny)] = seen[(cx, cy)]
           q.append((nx, ny))
    return trails
ans = sum(bfs(r, c) for r, c in trailheads)
print(ans)