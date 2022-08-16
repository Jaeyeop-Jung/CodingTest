import math

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

dp = [math.inf] * (m + 1)
dp[m] = 0
for i in range(len(dp) - 1, 0, -1):
    for j in arr:
        if i - j >= 0:
            dp[i - j] = min(dp[i - j], dp[i] + 1)

if dp[0] == math.inf:
    print(-1)
else:
    print(dp[0])
