import sys

sys.setrecursionlimit(3000)

input = sys.stdin.readline

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def dfs(dp, r, c, d):
    if (r, c, d) in dp:
        return dp[(r, c, d)]

    cur = 0
    for i in range(4):
        movedR, movedC = r + dR[i], c + dC[i]
        if not 0 <= movedR < n or not 0 <= movedC < n:
            continue
        if arr[r][c] < arr[movedR][movedC]:
            cur = max(cur, dfs(dp, movedR, movedC, i) + 1)
    dp[(r, c, d)] = cur
    return cur

dp = {}
res = 0
for r in range(n):
    for c in range(n):
        for d in range(4):
            res = max(res, dfs(dp, r, c, d))

print(res + 1)
