def calculate(num):
    avg = sum(num)/len(num)
    ls = []
    for i in range(len(num)):
        if num[i] > avg:
            ls.append(num[i])
    return avg, ls


num1 = input(
    "Please input numbers,and press the Enter to end.(gap with ,)\n").split(',')
num2 = list(map(int, num1))
a = calculate(num2)
print(a)
