def findFalseCoin(coins, start, n):
    if n == 1: 
        print(f"Fake coin:{start}")
        return
    group_a, group_b, group_c = group(coins)
    result = compare(group_a, group_b)
    if result == 'right': 
        findFalseCoin(group_a, start, n // 2)
    elif result == 'left': 
        findFalseCoin(group_b, start + n // 2, n // 2)
    elif result == 'equal' and len(group_c) == 0:
        print("Fake coin is not found")
    elif result == 'equal' and len(group_c) == 1:
        print(f"Fake coin:{group_c[0]}")
        
def group(coins):
    n = len(coins)
    group_a = coins[0 : n // 2]
    group_b = coins[n // 2 : n // 2 * 2]
    group_c = coins[n // 2 * 2 : n]#余数堆,最大为一
    if len(group_c) == 1: 
        group_c[0] = n - 1
    return group_a, group_b, group_c
 
def compare(first_group, second_group):
    sum1, sum2 = sum(first_group), sum(second_group)
    if sum1 == sum2: 
        result = 'equal'
    elif sum1 < sum2: 
        result = 'right'
    else: 
        result = 'left'
    return result
 
coins = list(map(int,input().split(',')))
findFalseCoin(coins,0,len(coins))
#主要思路：先将硬币分堆，如果是奇数，则余数需要另外成组