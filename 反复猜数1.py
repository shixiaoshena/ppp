a = 100
b = 0
while True:
    b += 1
    try:
        i = eval(input())
    except NameError:
        print('input error')
        continue
    if i > a:
        print("larger than expected")
    elif i < a:
        print("less than expected")
    else:
        print("you win")
        break
