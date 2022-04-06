n = int(input())
dp = [5001] * (n + 1)

dp[0] = 0
dp[3] = 1
for i in range(5, n + 1):
    if dp[i - 3] != 5001:
        dp[i] = min(dp[i], dp[i - 3] + 1)
    if dp[i - 5] != 5001:
        dp[i] = min(dp[i], dp[i - 5] + 1)

if dp[n] == 5001:
    print(-1)
else:
    print(dp[n])