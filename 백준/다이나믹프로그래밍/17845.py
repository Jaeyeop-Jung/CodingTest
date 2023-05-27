import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]

dp = [0] * (n + 1)
for score, cost in arr:
    for i in range(n, cost - 1, -1):
        dp[i] = max(dp[i], dp[i - cost] + score)

print(dp[-1])