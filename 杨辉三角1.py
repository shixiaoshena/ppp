n = eval(input())  # 输入杨辉三角的总行数
triangle = [[1], [1, 1]]#先给出第1，2行
for i in range(2, n):
    pre = triangle[i-1]  # 上一行
    mul = [1]#每一行第一个元素
    for j in range(i-1):
        mul.append(pre[j]+pre[j+1])#每一行中元素等于上一行的左右两个数字之和
    mul.append(1)#添加每一行末尾数字1
    triangle.append(mul)
for i in range(n):#按照等边三角形格式输出
    s = " "*(n-1-i)
    for j in triangle[i]:
        s = s+str(j)+" "#控制每行每个元素的间隔
    print(s)
