from collections import deque
with open('input.txt') as file:
    s = file.read().strip()
grid = [list(row) for row in s.split('\n')]
grid = [[int(ele) for ele in row] for row in grid]
ROWS, COLS = len(grid), len(grid)
trailheads = [(r, c) for r in range(ROWS)
              for c in range(COLS) if grid[r][c] == 0]


def bfs(x, y):
    summits = 0
    seen = set((x, y))
    q = deque([(x, y)])
    while q:
        cx, cy = q.popleft()
        for nx, ny in [(cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)]:
            if nx not in range(ROWS) or ny not in range(COLS):
                continue
            if grid[cx][cy] + 1 != grid[nx][ny]:
                continue
            if (nx, ny) in seen:
                continue
            seen.add((nx, ny))
            if grid[nx][ny] == 9:
                summits += 1
            else:
                q.append((nx, ny))
    return summits


ans = sum(bfs(r, c) for r, c in trailheads)
print(ans)
