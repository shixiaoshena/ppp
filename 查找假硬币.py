# 直接遍历
from math import floor


def findFalseCoin(coins, start, n):
    if n == 1:
        return start
    nHalf = floor(n/2.0)
    wL = sum(coins[start:start+nHalf])
    wR = sum(coins[start+nHalf:start+nHalf+nHalf])
    if wL < wR:
        return findFalseCoin(coins, start, nHalf)
    elif wR < wL:
        return findFalseCoin(coins, start+nHalf, nHalf)
    elif nHalf*2 < n:
        return start+n-1
    else:
        return None


coins = [100, 100, 100, 99, 100, 100, 100, 100, 100]
r = findFalseCoin(coins, 0, len(coins))
print('Fake coin:%d' % r)
