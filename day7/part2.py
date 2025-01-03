import itertools

with open('input.txt') as file:
    s = file.read().strip()
ans = 0
for row in s.split('\n'):
    correct = False
    res, nums_s = row.split(': ')
    res = int(res)
    nums = [int(x) for x in nums_s.split(' ')]
    for ops in itertools.product(*[('+', "*", '||') for _ in range(len(nums) - 1)]):
        total = nums[0]
        for i in range(1, len(nums)):
            op = ops[i - 1]
            if op == '+':
                total += nums[i]
            elif op == '*':
                total *= nums[i]
            elif op == '||':
                total = int(str(total) + str(nums[i]))
        if total == res:
            correct = True
    if correct:
        ans += res
print(ans)