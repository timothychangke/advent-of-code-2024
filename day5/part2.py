from functools import cmp_to_key
from collections import defaultdict
rules = []
ans = 0
with open('input.txt') as file:
    rules_string, data_string = file.read().strip().split('\n\n')
    data = data_string.split('\n')
    for rule in rules_string.split('\n'):
        x, y = rule.split('|')
        rules.append((int(x), int(y)))
order_before = defaultdict(set)
for x, y in rules:
    order_before[x].add(y)


def isGood(nums):
    for x, y in rules:
        if int(x) in arr and int(y) in arr and arr.index(x) > arr.index(y):
            return False
    return True


def compare(a, b):
    if b in order_before[a]:
        return 1
    if a in order_before[b]:
        return -1
    return 0


for d in data:
    arr = [int(n) for n in d.split(',')]
    if not isGood(arr):
        arr.sort(key=cmp_to_key(compare))
        ans += arr[len(arr)//2]
print(ans)
