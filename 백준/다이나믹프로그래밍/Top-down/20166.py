# import sys
#
# input = sys.stdin.readline
#
# dR = [0, 1, 1, 1, 0, -1, -1, -1]
# dC = [1, 1, 0, -1, -1, -1, 0, 1]
#
# def dfs(arr, dp, r, c, cnt):
#     if cnt == len(target):
#         return 1
#     if dp[r][c][cnt] != -1:
#         return dp[r][c][cnt]
#
#     dp[r][c][cnt] = 0
#     for i in range(len(dR)):
#         movedR, movedC = r + dR[i], c + dC[i]
#         movedR %= n
#         movedC %= m
#         if arr[movedR][movedC] == target[cnt]:
#             dp[r][c][cnt] += dfs(arr, dp, movedR, movedC, cnt + 1)
#     return dp[r][c][cnt]
#
#
# n, m, k = map(int, input().split())
# arr = [list(input().strip()) for _ in range(n)]
# for _ in range(k):
#     dp = [[[-1] * 6 for _ in range(m)] for _ in range(n)]
#     target = input().strip()
#     res = 0
#     for r in range(n):
#         for c in range(m):
#             if arr[r][c] == target[0]:
#                 res += dfs(arr, dp, r, c, 1)
#     print(res)

import sys

input = sys.stdin.readline

dR = [0, 1, 1, 1, 0, -1, -1, -1]
dC = [1, 1, 0, -1, -1, -1, 0, 1]

def dfs(arr, dp, r, c, cur):
    rest = target[len(cur):]
    if cur == target:
        return 1
    if rest in dp[r][c]:
        return dp[r][c][rest]

    dp[r][c][rest] = 0
    for i in range(len(dR)):
        movedR, movedC = r + dR[i], c + dC[i]
        movedR %= n
        movedC %= m
        if arr[movedR][movedC] == target[len(cur)]:
            dp[r][c][rest] += dfs(arr, dp, movedR, movedC, cur + target[len(cur)])
    return dp[r][c][rest]


n, m, k = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
dp = [[{} for _ in range(m)] for _ in range(n)]
for _ in range(k):
    target = input().strip()
    res = 0
    for r in range(n):
        for c in range(m):
            if arr[r][c] == target[0]:
                res += dfs(arr, dp, r, c, arr[r][c])
    print(res)