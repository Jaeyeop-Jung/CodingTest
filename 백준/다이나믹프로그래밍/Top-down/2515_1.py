# TODO 틀림

import sys
from bisect import bisect_left

sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def dfs(height, score, dp, idx, cur):
    if idx == n:
        return 0
    if (idx, cur) in dp:
        return dp[(idx, cur)]

    dp[(idx, cur)] = 0
    # 선택
    next = bisect_left(height, height[idx] + m)
    if idx < next <= n:
        dp[(idx, cur)] = max(dp[(idx, cur)], dfs(height, score, dp, next, height[idx]) + score[idx])

    # 선택 안함
    dp[(idx, cur)] = max(dp[(idx, cur)], dfs(height, score,  dp, idx + 1, cur))

    return dp[(idx, cur)]

dp = {}
arr.sort()
height = [i[0] for i in arr]
score = [i[1] for i in arr]
print(dfs(height, score, dp, 0, 0))