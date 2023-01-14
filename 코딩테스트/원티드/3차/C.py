import sys

input = sys.stdin.readline

n, m, c, = map(int, input().split())
score = [list(map(int, input().split())) for _ in range(c)]
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# DP에서 0행 x열, x행 0열 초기화
dp = [[0] * m for _ in range(n)]
for column in range(m):
    dp[0][column] = score[a[0] - 1][b[column] - 1]
for row in range(n):
    dp[row][0] = score[a[row] - 1][b[0] - 1]


for row in range(1, n):
    for column in range(1, m):
        dp[row][column] = max(
            dp[row - 1][column],
            dp[row][column - 1],
            dp[row - 1][column - 1] + score[a[row] - 1][b[column] - 1],
            dp[row - 1][column - 1] + score[b[column] - 1][a[row] - 1]

        )

print(dp[-1][-1])
