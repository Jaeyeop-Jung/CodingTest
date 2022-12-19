# TODO 틀림

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [[0] * m for _ in range(n)]
for c in range(m):
    dp[0][c] = 1

for r in range(1, n):
    if r % 2 == 1:
        dp[r][0] = dp[r - 1][1]
        for c in range(1, m - 1):
            dp[r][c] = (dp[r - 1][c - 1] + dp[r - 1][c + 1]) % 1000000007
        dp[r][-1] = dp[r - 1][-2]
    else:
        dp[r][0] = dp[r - 1][0] + dp[r - 1][1]
        for c in range(1, m - 1):
            dp[r][c] = (dp[r - 1][c - 1] + dp[r - 1][c] + dp[r - 1][c + 1]) % 1000000007
        dp[r][-1] = dp[r - 1][-1] + dp[r - 1][-2]


print(sum(dp[-1]) % 1000000007)
