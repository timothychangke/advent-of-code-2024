

import re

with open('input.txt') as file:
    s = file.read().strip()

ans = 0  
for play in s.split('\n\n'):
    ax, ay, bx, by, x, y = map(int, re.findall(r"\d+", play))
    min_tokens = float("inf")
    for i in range(101):
        for j in range(101):
           if ax * i + bx * j == x and ay * i + by * j == y:
             min_tokens = min(min_tokens, i * 3 + j)   
    if min_tokens != float("inf"):
        ans += min_tokens
print(ans)        
