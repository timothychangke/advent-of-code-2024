""" 
let the number of times A is pressed be a
let the number of times B is pressed be b

now let the variables be ax ay bx by a b
ax + bx = a
ax - a = -bx
a(x - 1) = -bx
a = - bx / (x - 1)
x = a/(a + b)
ay + by = b
y = b/(x + y)

ac + be = x
ad + bf = y
afc + bfe = xf
ade + bfe = ye
afc - ade = xf - ye
a = (xf - ye) / (fc - de)


"""
import re
with open('input.txt') as file:
    s = file.read().strip()

ans = 0
for play in s.split('\n\n'):
    c, d, e, f, x, y = map(int, re.findall(r"\d+", play))
    x += 10000000000000
    y += 10000000000000
    a = (x * f - y * e) / (f * c - d * e)
    b = (x - c * a) / e
    if a % 1 == b % 1 == 0:
        ans += a * 3 + b
print(ans)
    
    
    
