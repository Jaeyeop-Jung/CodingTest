# TODO 틀림 할 수 있다 거의 맞음

n = int(input())
dp = [0] * (n + 1)
if 2 <= n:
    dp[2] = 1
    flag = False
    for i in range(3, n + 1):
        if flag:
            dp[i] = dp[i - 1] * i + 1
            flag = False
        else:
            dp[i] = dp[i - 1] * i - 1
            flag = True
        dp[i] %= 1000000000
print(dp[n])