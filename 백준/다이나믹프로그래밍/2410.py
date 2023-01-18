import math

n = int(input())
dp = [1] * (n + 1)

for cur in range(1, int(math.log2(n)) + 1):
    sep = 2 ** cur
    for i in range(sep, len(dp)):
        dp[i] = (dp[i] + (dp[i - sep])) % 1000000000

# for r in range(1, len(dp)):
#     for c in range(len(dp[r])):
#         dp[r][c] = (dp[r - 1][c] + dp[r][c - (2 ** r)]) % 1000000000

print(dp[-1])