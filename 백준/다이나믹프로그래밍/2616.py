# TODO 틀림

import math
import sys

input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))
m = int(input())

total = [arr[0]]
for i in range(1, n + 1):
    total.append(total[-1] + arr[i])

dp = [[-math.inf] * (n + 1) for _ in range(4)]
for i in range(m + 1):
    dp[i][0] = 0
for i in range(m + 1):
    dp[i][1] = 0
dp[1][1] = arr[1]
for i in range(n + 1):
    dp[0][i] = 0

for i in range(1, 4):
    for j in range(2, n + 1):
        for sep in range(m, -1, -1):
            before = j - sep
            dp[i][j] = max(dp[i][j], dp[i][before], dp[i - 1][before] + total[j] - total[before])

print(dp[-1][-1])