import sys

input = sys.stdin.readline

def dfs(dp, w, h):
    if w == 0 and h == 0:
        return 1
    if (w, h) in dp:
        return dp[(w, h)]

    dp[(w, h)] = 0
    if 0 < w:
        dp[(w, h)] += dfs(dp, w - 1, h + 1)
    if 0 < h:
        dp[(w, h)] += dfs(dp, w, h - 1)
    return dp[(w, h)]

while True:
    t = int(input())
    if t == 0:
        break

    print(dfs({}, t, 0))