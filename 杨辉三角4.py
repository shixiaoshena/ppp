def triangle(n):
    l=[]
    for i in range(n):
        if i==0:
            l.append([1])
        elif i==1:
            l.append([1,1])#完成前两行确定
        else:
            y = []
            for j  in range(i+1):
                if j==0 or j==i:
                    y.append(1)
                else:
                    y.append(l[i-1][j]+l[i-1][j-1])
            l.append(y)
    return l
 
def printf(n,m):
    for i in range(n):
        print(' '* (block * (n - i)), end='')
        for j in range(len(x[i])):
            print(' ' * (block - len(str(x[i][j]))), end='')
            print(x[i][j], end=' ' * block)
        print()#换行
 
 
n = int(input())
x=triangle(n)
maxNumber = max(x[n-1])
block = len(str(maxNumber))
printf(n, block)