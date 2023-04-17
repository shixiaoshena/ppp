m = int(input())
n = []
while m != 1:
    for i in range(2, m+1):
        while m % i == 0:
            n.append(i)
            m /= i
print(n)
