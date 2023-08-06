import sys

input = sys.stdin.readline

# n, s, m, = map(int, input().split())
# arr = list(map(int, input().split()))
n, s, m = 50, 500, 1000
arr = [i for i in range(1, 51)]
cnt = 0

dp = [[False] * (m + 1) for _ in range(n)]

res = -1
def dfs(arr, dp, idx, cur):
    if idx == n:
        global res
        res = max(res, cur)
        return True
    if dp[idx][cur]:
        return True

    dp[idx][cur] = True
    if arr[idx] + cur <= m:
        dfs(arr, dp, idx + 1, cur + arr[idx])
    if 0 <= cur - arr[idx]:
        dfs(arr, dp, idx + 1, cur - arr[idx])
    return dp[idx][cur]

dfs(arr, dp, 0, s)
print(res)
