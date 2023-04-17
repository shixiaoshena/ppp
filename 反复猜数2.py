import random
max_time = int(input("请输入最大猜数次数:"))
number = random.randint(0, 100)
i = 0
n = int(input("请输入你要猜的数:"))
i += 1
while n != number and i < max_time:
    if n > number:
        n = int(input("larger than expected, please input a new number:"))
    else:
        n = int(input("less than expected, please input a new number:"))
    i += 1
if n == number:
    print("you win, total {} time".format(i))
else:
    print("there is no more chance")
    print(number)
