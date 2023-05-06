import sys
x_str = input()
if ('.' in x_str) or (not x_str.isdigit()):
    print("illegal input")
    sys.exit()
x = int(x_str)


def f(x):
    if x < 5:
        return x
    elif x >= 15:
        return x-6
    else:
        return x+6


print(f(x))
