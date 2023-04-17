try:
    TempStr = input()  # 获取输入
    if TempStr[-1] in ['F', 'f']:  # 判断字符串最后一个是否是'F'或'f'
        C = int((eval(TempStr[:-1]) - 32) / 1.8)  # 计算
        # 输出两位小数
        print("What is the temperature?The converted temperature is {}C".format(C))
    elif TempStr[-1] in ['C', 'c']:
        F = int(1.8 * (eval(TempStr[:-1])) + 32)
        print("What is the temperature?The converted temperature is {}F".format(F))
    else:
        print("What is the temperature?End with 'C','c','F','f'")  # 输入不对
except NameError:  # 捕捉NameError错误
    print('What is the temperature?Input error')
