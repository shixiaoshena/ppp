count = 0


def hanoi(n, src, dst, mid):
    global count
    if n == 1:
        print("[STEP   {}]{}->{}".format(count+1, src, mid))
        count += 1
    else:
        hanoi(n-1, src, dst, mid)
        print("[STEP   {}]{}->{}".format(count+1, dst, src))
        count += 1
        hanoi(n-1, mid, dst, src)


n = int(input())
hanoi(n, 'A', 'B', 'C')
