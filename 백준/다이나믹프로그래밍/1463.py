n = int(input())
dp = [1000001] * (n + 1)

dp[1] = 0
for i in range(2, n + 1):
    dp[i] = min(dp[i], dp[i - 1] + 1)
    if i % 3 == 0:
        if dp[i // 3] != 1000001:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    if i % 2 == 0:
        if dp[i // 2] != 1000001:
            dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[n])