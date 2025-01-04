with open('input.txt') as file:
    s = file.read().strip()
arr = [int(x) for x in s.split(' ')]
for _ in range(25):
    output = []
    for idx, ele in enumerate(arr):
        if ele == 0:
            output.append(1)
            continue
        ele_s = str(ele)
        if len(ele_s) % 2 == 0:
            midpoint = len(ele_s) // 2
            output.append(int(ele_s[:midpoint]))
            output.append(int(ele_s[midpoint:]))
        else:
            output.append(ele * 24)
    arr = output
ans = len(arr)
print(ans)
