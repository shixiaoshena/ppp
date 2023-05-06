def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1


num = int(input())
for i in range(2, num+1):
    if isPrime(i) == 1:
        print(i, end=" ")
