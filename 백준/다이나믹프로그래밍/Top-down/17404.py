import math
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def dfs(dp, start, cur, idx):
    if idx == n - 1:
        return arr[idx][cur]
    if dp[idx][cur] != math.inf:
        return dp[idx][cur]

    for next in range(3):
        if next == cur:
            continue
        if idx + 1 == n - 1:
            if next != start:
                dp[idx][cur] = min(dp[idx][cur], dfs(dp, start, next, idx + 1) + arr[idx][cur])
        else:
            dp[idx][cur] = min(dp[idx][cur], dfs(dp, start, next, idx + 1) + arr[idx][cur])
    return dp[idx][cur]

res = math.inf
for start in range(3):
    res = min(res, dfs([[math.inf] * 3 for _ in range(n)], start, start, 0))
print(res)

# res = math.inf
# for start in range(3):
#     dp = [[math.inf] * 3 for _ in range(n)]
#     dp[0][start] = arr[0][start]
#     for r in range(1, n - 1):
#         dp[r][0] = min(dp[r][0], dp[r - 1][1] + arr[r][0], dp[r - 1][2] + arr[r][0])
#         dp[r][1] = min(dp[r][1], dp[r - 1][0] + arr[r][1], dp[r - 1][2] + arr[r][1])
#         dp[r][2] = min(dp[r][2], dp[r - 1][0] + arr[r][2], dp[r - 1][1] + arr[r][2])
#     for c in range(3):
#         if start == c:
#             continue
#         dp[-1][c] = min(dp[-1][c], dp[-2][c - 1] + arr[-1][c], dp[-2][(c + 1) % 3] + arr[-1][c])
#     res = min(res, min(dp[-1]))
#
# print(res)