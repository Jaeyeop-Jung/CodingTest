import math

n, t, = map(int, input().split())
arr = [int(input()) for _ in range(n)]

arr.sort()
dp = [math.inf] * (t + 1)
dp[0] = 0
for i in arr:
    for j in range(i, t + 1):
        dp[j] = min(dp[j], dp[j - i] + 1)
print(dp[t] if dp[t] != math.inf else -1)