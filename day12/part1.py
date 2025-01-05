from collections import deque
with open('input.txt') as file:
    s = file.read().strip()
grid = [list(row) for row in s.split('\n')]
ROWS, COLS = len(grid), len(grid[0])
seen = set()
regions = []
for r in range(ROWS):
    for c in range(COLS):
        if (r, c) in seen:
            continue
        seen.add((r, c))
        q = deque([(r, c)])
        region = set()
        region.add((r, c))
        crop = grid[r][c]
        while q:
            cr, cc = q.popleft()
            for nr, nc in [(cr + 1, cc), (cr - 1, cc), (cr, cc + 1), (cr, cc - 1)]:
                if nr not in range(ROWS) or nc not in range(COLS):
                    continue
                if grid[nr][nc] != crop:
                    continue
                if (nr, nc) in region:
                    continue
                region.add((nr, nc))
                q.append((nr, nc))
        regions.append(region)
        seen = seen | region


def perimeter(region):
    res = 0
    for (r, c) in region:
        res += 4
        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if (nr, nc) in region:
                res -= 1
    return res


ans = sum(len(region) * perimeter(region) for region in regions)
print(ans)
