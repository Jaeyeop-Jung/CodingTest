import sys

input = sys.stdin.readline

dR = [0, 1, 1]
dC = [1, 1, 0]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]
dp[0][0] = arr[0][0]
for r in range(len(arr)):
    for c in range(len(arr[r])):
        for i in range(3):
            movedR, movedC = r + dR[i], c + dC[i]
            if not 0 <= movedR < n or not 0 <= movedC < m:
                continue
            dp[movedR][movedC] = max(dp[movedR][movedC], dp[r][c] + arr[movedR][movedC])

print(dp[-1][-1])

