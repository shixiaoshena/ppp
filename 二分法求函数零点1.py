def fun(x):
    return x**5-15*x**4+85*x**3-225*x**2+274*x-121


n = int(input())
if fun(1.5) < 0:
    a, b = 1.5, 2.4
else:
    a, b = 2.4, 1.5
while True:
    mid = (a+b)/2
    if abs(fun(mid)) < 10**-n:
        break
    elif fun(mid) < 0:
        a = mid
    else:
        b = mid
print("{:.6f}".format(mid))
