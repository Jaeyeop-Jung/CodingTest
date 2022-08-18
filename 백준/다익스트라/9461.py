
t = int(input())
for _ in range(t):
    n = int(input())

    if 1 <= n <= 3:
        print(1)
        continue
    elif 3 <= n <= 5:
        print(2)
        continue
    else:
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 1
        dp[3] = 1
        dp[4] = 2
        dp[5] = 2
        for i in range(6, n + 1):
            dp[i] = dp[i - 5] + dp[i - 1]
        print(dp[n])

