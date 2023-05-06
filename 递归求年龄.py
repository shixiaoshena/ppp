def getAge(n, x):
    if n == 1:
        return 3
    if n == 2:
        return x
    return getAge(n-1, x)+getAge(n-2, x)
#递归法求年龄

flag = 0
f1 = 3
x, n = map(int, input().split(','))
l = [x, f1]#创建空列表
for i in range(3, n+1):#年龄需大于3小于等于n
    a = getAge(i, x)
    if a > 120:
        flag = i
        break
    else:
        l.insert(0, a)
if flag != 0:
    print('Age', flag, 'is larger than 120!')
print(l)
