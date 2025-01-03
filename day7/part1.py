with open('input.txt') as file:
    s = file.read().strip()
ans = 0
for row in s.split('\n'):
    res, nums_s = row.split(': ')
    nums = [int(x) for x in nums_s.split(' ')]
    correct = False
    for opmask in range(1 << (len(nums) - 1)):
        current = nums[0]
        for i in range(len(nums) - 1):
            if (opmask & (1 << i)) > 0:
                current += nums[i + 1]
            else:
                current *= nums[i + 1]
        if current == int(res):
            correct = True
    if correct:
        ans += int(res)        
print(ans)