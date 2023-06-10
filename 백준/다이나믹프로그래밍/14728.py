import sys

input = sys.stdin.readline

n, t, = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def dfs(arr, dp, idx, time):
    if idx == len(arr):
        return 0
    if dp[idx][time] != -1:
        return dp[idx][time]

    cur = dfs(arr, dp, idx + 1, time)
    if time + arr[idx][0] <= t:
        cur = max(cur, dfs(arr, dp, idx + 1, time + arr[idx][0]) + arr[idx][1])
    dp[idx][time] = cur
    return dp[idx][time]

dp = [[-1] * 10001 for _ in range(n)]
print(dfs(arr, dp, 0, 0))
