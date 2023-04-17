import math


def isPrime(n):
    a = 0
    m = int(pow(n, 0.5))+1
    for i in range(2, m+1):
        if n % i == 0:
            break
        elif n % i != 0 and i == m:
            a = 1
    return (a)


def f(n):
    ls = []
    for i in range(2, n+1):
        a = isPrime(i)
        if a == 0:
            continue
        elif a == 1:
            ls.append(i)
    l = ls[-10:]
    sum = 0
    for j in l:
        sum += j
    return sum


p = int(input())
print(f(p))
