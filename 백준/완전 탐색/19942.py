import math
from itertools import combinations

n = int(input())
target = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]

cost = math.inf
res = []
for i in range(1, n + 1):
    for comb in combinations([j for j in range(n)], i):
        temp = [0, 0, 0, 0]
        tempCost = 0
        for idx in comb:
            each = arr[idx]
            for j in range(4):
                temp[j] += each[j]
            tempCost += each[-1]
        for j in range(4):
            if temp[j] < target[j]:
                break
        else:
            if tempCost < cost:
                res = [comb]
                cost = tempCost
            elif tempCost == cost:
                res.append(comb)

res.sort()
print(cost if cost != math.inf else -1)
if cost != math.inf:
    for i in res[0]:
        print(i + 1, end=' ')