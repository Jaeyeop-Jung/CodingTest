import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(arr, dp, idx):
    if idx >= len(arr):
        return 0
    if dp[idx] != -1:
        return dp[idx]

    # 선택
    dp[idx] = max(dp[idx], dfs(arr, dp, idx + 2) + arr[idx])

    # 안선택
    dp[idx] = max(dp[idx], dfs(arr, dp, idx + 1))

    return dp[idx]

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(n)]
    nextArr = []
    for r in range(n):
        nextArr.append(dfs(arr[r][:], [-1] * m, 0))

    dp = [-1] * n
    print(dfs(nextArr, dp, 0))
