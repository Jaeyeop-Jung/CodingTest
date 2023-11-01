import math
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)

dR = [1, 1, 1]
dC = [-1, 0, 1]

n, m, = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[[math.inf] * 3 for _ in range(m)] for _ in range(n)]
def dfs(arr, dp, r, c, pre):
    if r == n:
        return 0
    if dp[r][c][pre] != math.inf:
        return dp[r][c][pre]

    for i in range(3):
        if i == pre:
            continue
        movedR, movedC = r + dR[i], c + dC[i]
        if 0 <= movedC < m:
            dp[r][c][pre] = min(dp[r][c][pre], dfs(arr, dp, movedR, movedC, i) + arr[r][c])
    return dp[r][c][pre]

res = math.inf
for i in range(m):
    for j in range(3):
        res = min(res, dfs(arr, dp, 0, i, j))
print(res)

for c in range(m):
    for i in range(3):
        dp[0][c][i] = arr[0][c]

for r in range(n - 1):
    for c in range(m):
        for cur in range(3):
            for next in range(3):
                if cur == next:
                    continue
                movedR, movedC = r + dR[next], c + dC[next]
                if not 0 <= movedC < m:
                    continue
                dp[movedR][movedC][next] = min(dp[movedR][movedC][next], dp[r][c][cur] + arr[movedR][movedC])

print(min(map(min, dp[-1])))