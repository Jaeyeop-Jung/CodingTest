import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [int(input()) for _ in range(m)]

dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1
for i in range(2, n + 1):
    dp[i] = dp[i - 2] + dp[i - 1]

result = 1
cnt = 0
for i in range(1, n + 1):
    if i not in arr:
        cnt += 1
    else:
        result *= dp[cnt]
        cnt = 0
if cnt != 0:
    result *= dp[cnt]
print(result)
