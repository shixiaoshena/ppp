n = int(input())
s = input()
news = ''
for i in s:
    if 'a' <= i <= 'z':
        j = ord(i)
        j = ((j+n)-97) % 26+97
        i = chr(j)
    news += i
print(news)
