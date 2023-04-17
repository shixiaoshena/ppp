def Prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
        else:
            return True


n = int(input())
result = []
for i in range(2, n):
    if Prime(i) == True:
        result.append(i)
print(result)
