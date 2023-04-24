import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
dic = defaultdict(list)
for i in range(n):
    color, size, = map(int, input().split())
    dic[size].append([i, color])

dp = [0] * (n + 1)
total = 0
result = [0] * n

keys = sorted(dic.keys())
for size in keys:
    tempTotal = 0
    tempDp = []
    for i, color in dic[size]:
        tempTotal += size
        tempDp.append(color)
        result[i] = total - dp[color]
    total += tempTotal
    for color in tempDp:
        dp[color] += size

for res in result:
    print(res)
