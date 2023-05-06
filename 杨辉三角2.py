triangle = [[1]]#定义每一行的第一个元素，其余元素通过上一行左右两个元素相加
n = eval(input())
for i in range(1, n):
    swap = triangle[i-1]+[0]
    mul = [1]
    for j in range(len(swap)-1):
        mul.append(swap[j]+swap[j+1])
    triangle.append(mul)
for i in range(n):  # 按照等边三角形格式输出
    s = " "*(n-1-i)
    for j in triangle[i]:
        s = s+str(j)+" "  # 控制每行每个元素的间隔
    print(s)
