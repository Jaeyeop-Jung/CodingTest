# TODO 틀림 다음엔 맞을 수 있다

import math
import sys

sys.setrecursionlimit(3000)
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

def dfs(dp, idx, space):
    if idx == len(arr):
        return 0
    if (idx, space) in dp:
        return dp[(idx, space)]

    dp[(idx, space)] = math.inf
    if space + arr[idx] + 1 <= m:
        dp[(idx, space)] = min(dp[(idx, space)], dfs(dp, idx + 1, space + arr[idx] + 1))
    dp[(idx, space)] = min(dp[(idx, space)], dfs(dp, idx + 1, arr[idx]) + (m - space) ** 2)
    return dp[(idx, space)]


dp = {}
print(dfs(dp, 1, arr[0]))