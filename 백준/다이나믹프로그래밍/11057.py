# TODO 틀림

n = int(input())

dp = [0] * (n + 1)
dp[0] = 0
dp[1] = 10
for i in range(2, n + 1):
    total = dp[i - 1]
    temp = dp[i - 1]
    for j in range(10):
        temp -= 10 ** (i - 1)
        total += temp
    dp[i] = total

print(dp[-1])
