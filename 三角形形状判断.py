import sys
a = list(map(int, input().split()))
a.sort()
if a[0]+a[1] <= a[2]:
    print("Not triangle")
    sys.exit(0)
if a[2]*a[2] == a[1]*a[1]+a[0]*a[0]:
    print("Right triangle")
    sys.exit(0)
if a[2]*a[2] < a[1]*a[1]+a[0]*a[0]:
    print("Acute triangle")
if a[2]*a[2] > a[1]*a[1]+a[0]*a[0]:
    print("Obtuse triangle")
if a[1] == a[0] or a[0] == a[2] or a[1] == a[2]:
    print("Isosceles triangle")
if a[0] == a[1] and a[1] == a[2]:
    print("Equilateral triangle")
