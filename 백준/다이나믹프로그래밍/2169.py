import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0, 0] for _ in range(m)] for _ in range(n)]
cur = 0
for i in range(m):
    cur += arr[0][i]
    dp[0][i][0] = cur
    dp[0][i][1] = cur

for r in range(1, n):
    dp[r][0][0] = max(dp[r - 1][0]) + arr[r][0]
    for c in range(1, m):
        dp[r][c][0] = max(dp[r][c - 1][0], max(dp[r - 1][c])) + arr[r][c]

    dp[r][-1][1] = max(dp[r - 1][-1]) + arr[r][-1]
    for c in range(m - 2, -1, -1):
        dp[r][c][1] = max(dp[r][c + 1][1], max(dp[r - 1][c])) + arr[r][c]

print(max(dp[-1][-1]))