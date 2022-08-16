import chunk
import math

dRow = [-1, 0, 1]
dColumn = [1, 1, 1]

t = int(input())
for _ in range(t):
    n, m, = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = [arr[i:i + m] for i in range(0, len(arr), m)]

    dp = [[0] * m for _ in range(n)]
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    dp[2][0] = arr[2][0]
    for i in range(m):
        for j in range(n):
            for k in range(len(dRow)):
                movedRow = j + dRow[k]
                movedColumn = i + dColumn[k]
                if not 0 <= movedRow < n or not 0 <= movedColumn < m:
                    continue
                dp[movedRow][movedColumn] = max(dp[movedRow][movedColumn], dp[j][i] + arr[movedRow][movedColumn])

    print(max([j for i in range(len(dp)) for j in dp[i]]))
