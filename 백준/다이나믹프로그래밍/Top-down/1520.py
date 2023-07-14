# TODO 조금 더 디테일하게 생각해봐 맞을 수 있따

import sys

sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

n, m, = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def dfs(arr, dp, r, c, cur):
    if r == n - 1 and c == m - 1:
        return 1
    if dp[r][c] != -1:
        return dp[r][c]

    dp[r][c] = 0
    for i in range(4):
        movedR, movedC = r + dR[i], c + dC[i]
        if not 0 <= movedR < n or not 0 <= movedC < m:
            continue
        if arr[movedR][movedC] < cur:
            dp[r][c] += dfs(arr, dp, movedR, movedC, arr[movedR][movedC])
    return dp[r][c]

print(dfs(arr, [[-1] * m for _ in range(n)], 0, 0, arr[0][0]))