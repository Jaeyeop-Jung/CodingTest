n = int(input())
k = int(input())

dp = [[0] * 1001 for _ in range(1001)]
dp[1] = [0] + [1] + [0] * 999
dp[2] = [0] + [2] + [0] * 999
dp[3] = [0] + [3] + [0] * 999
dp[4] = [0] + [4] + [2] + [0] * 998
for i in range(5, 1001):
    dp[i][1] = i

for i in range(5, n + 1):
    for j in range(2, k + 1):
        dp[i][j] = (dp[i - 1][j] + dp[i - 2][j - 1]) % 1_000_000_003

print(dp[n][k])