import math
s, v = map(int, input().split())
n = 8*60+24*60
t = math.ceil(s/v)+10
n = n-t
if n >= 24*60:
    n -= 24*60
a = n % 60
b = n//60
if b < 10:
    if a < 10:
        print("0%d" % b, end=(":0"))
        print(a)
    else:
        print("0%d" % b, end=":")
        print(a)
else:
    if a < 10:
        print("%d" % b, end=(":0"))
        print(a)
    else:
        print("%d" % b, end=":")
        print(a)
