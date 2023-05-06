# 杨辉三角对称法
n = eval(input())
triangle = [[1], [1, 1]]
for i in range(2, n):
    tmp = triangle[-1]  # 上一个列表
    cul = [1]*(i+1)
    for j in range(i//2):
        cul[j+1] = tmp[j]+tmp[j+1]  # 临界值大约是中点处，但有例外
        if i != 2j:  # 当j不为中点时
            cul[-j-2] = cul[j+1]
    triangle.append(cul)
for i in range(n):  # 按照等边三角形格式输出
    s = " "*(n-1-i)
    for j in triangle[i]:
        s = s+str(j)+" "  # 控制每行每个元素的间隔
    print(s)
