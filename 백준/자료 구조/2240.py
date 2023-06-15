import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

t, w = map(int, input().split())
arr = [int(input()) for _ in range(t)]

def dfs(dp, idx, location, weight):
    if idx == t:
        return 0
    if (idx, location, weight) in dp:
        return dp[(idx, location, weight)]

    dp[(idx, location, weight)] = -1
    if arr[idx] == location:
        dp[(idx, location, weight)] = max(dp[(idx, location, weight)], dfs(dp, idx + 1, location, weight) + 1)
    else:
        if weight < w:
            dp[(idx, location, weight)] = max(dp[(idx, location, weight)], dfs(dp, idx + 1, arr[idx], weight + 1) + 1)
        dp[(idx, location, weight)] = max(dp[(idx, location, weight)], dfs(dp, idx + 1, location, weight))

    return dp[(idx, location, weight)]

dp = {}
print(dfs(dp, 0, 1, 0))