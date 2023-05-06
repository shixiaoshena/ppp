count=0
def hanoi(N, A, B, C):
  global count
  if N == 1: # 将A座上剩下的第N个盘子移动到C座上
    print("[STEP{:>4}] {}->{}".format(count+1, A, C)) # 打印移动步骤
    count+=1
  else:
    hanoi(N-1, A, C, B) # 借助C座将N-1个盘子从A座移动到B座
    print("[STEP{:>4}] {}->{}".format(count+1, A, C))
    count+=1
    hanoi(N-1, B, A, C)
if __name__ == "__main__":
#输入要移动的盘子个数
  n = int(input())
hanoi(n, 'A', 'B', 'C'); # 调用递归函数5
#print('{0:<5}'.format('aa')) # 占5个字符空间，0是format参数中的变量索引




