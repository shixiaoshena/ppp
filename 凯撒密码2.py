n, s = input().split(' ', 1)
res = ''
for i in s:
    if i.isalpha():
        t = ord(i)+int(n)
        if (i.islower() and t > ord('z')) or (i.isupper() and t > ord('Z')):
            t -= 26
        res += chr(t)
    else:
        res += i
print(res)
