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
        region = {(r, c)}
        q = deque([(r, c)])
        crop = grid[r][c]
        while q:
            cr, cc = q.popleft()
            for nr, nc in [(cr + 1, cc), (cr - 1, cc), (cr, cc - 1), (cr, cc + 1)]:
                if nr not in range(ROWS) or nc not in range(COLS):
                    continue
                if grid[nr][nc] != crop:
                    continue
                if (nr, nc) in region:
                    continue
                region.add((nr, nc))
                q.append((nr, nc))
        seen |= region
        regions.append(region)


def corners(region):
    corner_candidates = set()
    corners = 0
    for r, c in region:
        for cr, cc in [(r - 0.5, c - 0.5), (r + 0.5, c - 0.5), (r - 0.5, c + 0.5), (r + 0.5, c + 0.5)]:
            corner_candidates.add((cr, cc))
    for cr, cc in corner_candidates:
        config = [(sr, sc) in region for sr, sc in [(cr - 0.5, cc - 0.5),
                                                    (cr + 0.5, cc - 0.5), (cr - 0.5, cc + 0.5), (cr + 0.5, cc + 0.5)]]
        corner_count = sum(config)
        if corner_count == 1:
            corners += 1
        elif corner_count == 2 and (config == [True, False, False, True] or config == [False, True, True, False]):
            corners += 2
        elif corner_count == 3:
            corners += 1
    return corners

ans = sum((len(region) * corners(region) for region in regions))
print(ans)