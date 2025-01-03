with open('input.txt') as file:
    rules_string, data_string = file.read().strip().split('\n\n')
    data_arr = data_string.split('\n')
    
ans = 0
rules = []
for rule in rules_string.split('\n'):
    x, y = rule.split('|')
    rules.append((x, y))
for data in data_arr:
    arr = [int(d) for d in data.split(',')]
    g = True
    for x, y in rules:
        if int(x) in arr and int(y) in arr and arr.index(int(x)) > arr.index(int(y)):
            g = False
            break
    if g:
        ans += arr[len(arr)// 2]





    