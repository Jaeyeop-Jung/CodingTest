import sys

sys.setrecursionlimit(3000)
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = {}

def dfs(dp, idx, cur):
    if idx == n - 1:
        if cur == arr[idx]:
            return 1
        return 0
    if (idx, cur) in dp:
        return dp[(idx, cur)]

    dp[(idx, cur)] = 0
    if 0 <= cur + arr[idx] <= 20:
        dp[(idx, cur)] += dfs(dp, idx + 1, cur + arr[idx])
    if 0 <= cur - arr[idx] <= 20:
        dp[(idx, cur)] += dfs(dp, idx + 1, cur - arr[idx])
    return dp[(idx, cur)]

print(dfs(dp, 1, arr[0]))