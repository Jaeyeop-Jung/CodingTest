#
# n, k = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
#
# def dfs(arr, dp, idx, weight):
#     if idx == len(arr):
#         return 0
#     if k < weight:
#         return 0
#     if dp[idx][weight] != 0:
#         return dp[idx][weight]
#
#     dp[idx][weight] = max(dfs(arr, dp, idx + 1, weight), dfs(arr, dp, idx + 1, weight + arr[idx][0]) + arr[idx][1])
#     return dp[idx][weight]
#
#
# dp = [[0] * 100_002 for _ in range(n)]
# dfs(arr, dp, 0, 0)
#

def dfs(dp, depth, weight):
    global ans

    if weight > K:
        return -100000000

    if depth == N:
        return 0

    if dp[depth][weight] != -1:
        return dp[depth][weight]

    dp[depth][weight] = max(dfs(dp, depth + 1, weight), dfs(dp, depth + 1, weight + bag[depth][0]) + bag[depth][1])

    return dp[depth][weight]


N, K = map(int, input().split())

bag = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[-1] * (K + 1) for _ in range(N + 1)]
ans = 0

print(dfs(dp, 0, 0))