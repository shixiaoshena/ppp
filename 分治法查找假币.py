def weightCal(coins, start, end):
    sum = 0
    for i in range(start, end+1):
        sum += coins[i]
    return sum


def findFalseCoin(coins, start, n):
    if (start == n):
        print("Fake coin:{}".format(start))
        return
    if ((n-start+1) % 2 == 0):
        weight1 = weightCal(coins, start, n//2)
        weight2 = weightCal(coins, n//2+1, n)
        if (weight1 == weight2):
            print("Fake coin is not found")
            return
        elif weight1 < weight2:
            findFalseCoin(coins, start, n//2)
        else:
            findFalseCoin(coins, n//2+1, n)
    else:
        min = coins[start]
        flag = 0
        for i in range(start, n+1):
            if coins[i] < min:
                flag = 1
                min = i
                break
            elif coins[i] > min:
                flag = 1
                min = start
                break
        if flag == 1:
            print("Fake coin:{}".format(min))
        else:
            print("Fake coin is not found")
            return


coins = list(input().split(','))
coins = [int(i) for i in coins]
findFalseCoin(coins, 0, len(coins)-1)
