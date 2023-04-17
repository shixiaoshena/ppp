n = int(input())
a = []
b = [0]*n
for j in range(n):
    a.append(b[:])
max = n*n
min = 1
x, y = 0, 0
while min <= max:
    for i in range(n):
        a[y][x] = min
        x += 1
        min += 1
    x -= 1
    n -= 1
    y += 1
    for l in range(n):
        a[y][x] = min
        min += 1
        y += 1
    y -= 1
    x -= 1
    for r in range(n):
        a[y][x] = min
        x -= 1
        min += 1
    y -= 1
    x += 1
    n -= 1
    for k in range(n):
        a[y][x] = min
        y -= 1
        min += 1
    y += 1
    x += 1
with open("file.out", 'w') as file:
    for m in a:
        for f in m:
            file.write("%5d" % f)
        file.write("\n")
