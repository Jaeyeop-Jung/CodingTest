
arr = [1,2,3,4,5]

dp = [0] * len(arr)
dp[0] = 1
dp[1] = 1
for i in range(2, len(arr)):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp)