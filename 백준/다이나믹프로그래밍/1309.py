n = int(input())
dp = [0] * (n + 1)
dp[1] = 3
if n == 1:
    print(3)
    exit()
dp[2] = 7
if n == 2:
    print(7)
    exit()
for i in range(3, len(dp)):
    dp[i] = (dp[i - 1] * 2 + dp[i - 2]) % 9901
print(dp[-1])
