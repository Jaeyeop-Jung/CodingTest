#
t = int(input())
n = list()
for i in range(t):
    n.append(int(input()))

dp = list()
for i in range(max(n) + 1):
    dp.append([0, 0])

dp[0] = [1, 0]
dp[1] = [0, 1]
dp[2] = [1, 1]
dp[3] = [1, 2]
for i in range(4, len(dp)):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i - 1][1] + dp[i-2][1]

for i in n:
    print(dp[i][0], dp[i][1])