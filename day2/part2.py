with open('input.txt') as f:
    s = f.read().strip()

res = 0

def isSafe(lvl):
    diff = [lvl[i + 1] - lvl[i] for i in range(len(lvl) - 1)]
    incC = sum(1 for d in diff if 1 <= d <= 3)
    decC = sum(1 for d in diff if -3 <= d <= -1)
    return len(diff) == incC or len(diff) == decC


for line in s.split('\n'):
    level = list(map(int,line.split()))
    if isSafe(level) or any(isSafe(level[0:i] + level[i + 1:]) for i in range(len(line))):
        res += 1
print(res)