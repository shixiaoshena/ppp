m = 0
n = 0
p = 0
q = 0
k = 0
a = int(input())

if a % 2 == 0:
    k += 1
if n > 4 and n <= 12:
    k += 1
if k == 2:
    m = 1
if k > 0:
    n = 1
if k == 1:
    p = 1
if k == 0:
    q = 1

print(m, end=' ')
print(n, end=' ')
print(p, end=' ')
print(q)
