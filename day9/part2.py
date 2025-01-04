with open('input.txt') as file:
    s = file.read().strip()
files = {}
blanks = []
id = position = 0
for idx, size in enumerate(s):
    size = int(size)
    if idx % 2 == 0:
        files[id] = (position, size)
        id += 1
    else:
        if size != 0:
            blanks.append((position, size))
    position += size
while id > 0:
    id -= 1
    file_position, file_size = files[id]
    for idx, (blank_position, blank_size) in enumerate(blanks):
        if blank_position >= file_position:
            blanks = blanks[:idx]
            break
        if blank_size >= file_size:
            files[id] = (blank_position, file_size)
            if blank_size == file_size:
                blanks.pop(idx)
            else:
                blanks[idx] = (blank_position + file_size, blank_size - file_size)
            break
ans = 0
for id, (file_position, file_size) in files.items():
    for x in range(file_position, file_position + file_size):
        ans += id * x
print(ans)