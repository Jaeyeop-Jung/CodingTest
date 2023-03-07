# TODO 틀림 잘 생각해봐 맞을 수 있다

n = int(input())
dp = [0] * (n + 1)
dp[0] = 1
dp[2] = 1
for i in range(4, n + 1, 2):
    for j in range(i - 2, -1, -2):
        dp[i] += dp[j] * dp[i - 2 - j]
        dp[i] %= 987654321

print(dp[n])