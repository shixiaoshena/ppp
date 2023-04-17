maxNumber = int(input())
ls = list(range(2, maxNumber))
# 通过比较平方根来判断
m = int(maxNumber**0.5)
for i, value in enumerate(ls):
    if value > m:
        break
    ls[i+1:] = filter(lambda x: x % value != 0, ls[i+1:])
print(ls)
