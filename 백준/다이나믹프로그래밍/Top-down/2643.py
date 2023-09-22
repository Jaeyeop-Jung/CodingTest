
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def dfs(arr, dp, cur):
    if dp[cur]:
        return dp[cur]

    l, r = arr[cur]
    for next in range(n):
        if cur == next:
            continue
        nL, nR = arr[next]
        if (nL <= l and nR <= r) or (nL <= r and nR <= l):
            dp[cur] = max(dp[cur], dfs(arr, dp, next) + 1)
    return dp[cur]




dp = [0] * n
for i in range(n):
    dp[i] = dfs(arr, dp, i)

print(max(dp) + 1)