import math

n, k, = map(int, input().split())
arr = [int(input()) for _ in range(n)]

dp = [math.inf] * (k + 1)
dp[k] = 0
for i in range(k, -1, -1):
    for coin in arr:
        if 0 <= i - coin:
            dp[i - coin] = min(dp[i - coin], dp[i] + 1)

print(dp[0] if dp[0] != math.inf else -1)

