def isPrimeNumber(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
        else:
            return True


words = list(input())
letters = {}
for i in range(len(words)):
    if words[i] not in letters:
        letters[words[i]] = 1
    else:
        letters[words[i]] += 1
maxn = max(letters, key=letters.get)
minn = min(letters, key=letters.get)
ynPrimeNumber = letters.get(maxn)-letters.get(minn)
if isPrimeNumber(ynPrimeNumber):
    print("Lucky Word")
    print(ynPrimeNumber)
else:
    print("No Answer")
    print("0")
