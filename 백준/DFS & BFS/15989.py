
t = int(input())
dp = [0] * 10001
dp[0] = 1
for i in range(1, 4):
    for j in range(i, len(dp)):
        dp[j] += dp[j - i]

for _ in range(t):
    target = int(input())
    print(dp[target])