with open('input.txt') as file:
    s = file.read().strip()
arr = [int(x) for x in s.split(' ')]
cache = {}
def dp(num, step):
    result = 0
    if step == 0:
        return 1
    if (num, step) not in cache:
        if num == 0:
            result = dp(1, step - 1)
        elif len(str(num)) % 2 == 0:
            num = str(num)
            result += dp(int(num[:len(num)//2]), step - 1)
            result += dp(int(num[len(num)//2:]), step - 1)
        else:
            result = dp(2024 * num, step - 1)
        cache[(num, step)] = result
    return cache[(num, step)]
ans = 0
for x in arr:
   ans += dp(x, 2)
print(ans)
    
            
    
    