# from collections import deque
#
# GARO = 0
# SERO = 1
# DIAGONAL = 2
#
# garo = [[0, 1, 0, 1, GARO], [0, 1, 1, 1, DIAGONAL]]
# sero = [[1, 0, 1, 0, SERO], [1, 0, 1, 1, DIAGONAL]]
# diagonal = [[1, 1, 0, 1, GARO], [1, 1, 1, 0, SERO], [1, 1, 1, 1, DIAGONAL]]
#
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
#
# def wall(curRight, nextRight, d):
#     curR, curC, = curRight
#     nextR, nextC = nextRight
#     if nextR - curR == 0 and nextC - curC == 1:
#         if arr[nextR][nextC] == 1:
#             return True
#     elif nextR - curR == 1 and nextC - curC == 0:
#         if arr[nextR][nextC] == 1:
#             return True
#     else:
#         if arr[nextR][nextC] == 1 or arr[nextR - 1][nextC] == 1 or arr[nextR][nextC - 1] == 1:
#             return True
#     return False
#
#
# # def dfs(left, right, d):
# #     if right[0] == n - 1 and right[1] == n - 1:
# #         global result
# #         result += 1
# #         return
# #
# #     if d == GARO:
# #         for i in range(len(garo)):
# #             leftDr, leftDc, rightDr, rightDc, nextD = garo[i]
# #             leftR, leftC, = left
# #             rightR, rightC = right
# #             nextLeftR, nextLeftC = leftR + leftDr, leftC + leftDc
# #             nextRightR, nextRightC = rightR + rightDr, rightC + rightDc
# #             if not 0 <= nextLeftR < n or not 0 <= nextLeftC < n:
# #                 continue
# #             if not 0 <= nextRightR < n or not 0 <= nextRightC < n:
# #                 continue
# #             if wall(right, [nextRightR, nextRightC], nextD):
# #                 continue
# #             dfs([nextLeftR, nextLeftC], [nextRightR, nextRightC], nextD)
# #
# #     if d == SERO:
# #         for i in range(len(sero)):
# #             leftDr, leftDc, rightDr, rightDc, nextD = sero[i]
# #             leftR, leftC, = left
# #             rightR, rightC = right
# #             nextLeftR, nextLeftC = leftR + leftDr, leftC + leftDc
# #             nextRightR, nextRightC = rightR + rightDr, rightC + rightDc
# #             if not 0 <= nextLeftR < n or not 0 <= nextLeftC < n:
# #                 continue
# #             if not 0 <= nextRightR < n or not 0 <= nextRightC < n:
# #                 continue
# #             if wall(right, [nextRightR, nextRightC], nextD):
# #                 continue
# #             dfs([nextLeftR, nextLeftC], [nextRightR, nextRightC], nextD)
# #
# #     if d == DIAGONAL:
# #         for i in range(len(diagonal)):
# #             leftDr, leftDc, rightDr, rightDc, nextD = diagonal[i]
# #             leftR, leftC, = left
# #             rightR, rightC = right
# #             nextLeftR, nextLeftC = leftR + leftDr, leftC + leftDc
# #             nextRightR, nextRightC = rightR + rightDr, rightC + rightDc
# #             if not 0 <= nextLeftR < n or not 0 <= nextLeftC < n:
# #                 continue
# #             if not 0 <= nextRightR < n or not 0 <= nextRightC < n:
# #                 continue
# #             if wall(right, [nextRightR, nextRightC], nextD):
# #                 continue
# #             dfs([nextLeftR, nextLeftC], [nextRightR, nextRightC], nextD)
# #
#
# dp = [[0] * n for _ in range(n)]
# dp[0][1] = 1
# q = deque()
# q.append([0, 0, 0, 1, GARO])
# while q:
#     leftR, leftC, rightR, rightC, d, = q.popleft()
#     if d == GARO:
#         for i in range(len(garo)):
#             leftDr, leftDc, rightDr, rightDc, nextD = garo[i]
#             nextLeftR, nextLeftC = leftR + leftDr, leftC + leftDc
#             nextRightR, nextRightC = rightR + rightDr, rightC + rightDc
#             if not 0 <= nextLeftR < n or not 0 <= nextLeftC < n:
#                 continue
#             if not 0 <= nextRightR < n or not 0 <= nextRightC < n:
#                 continue
#             if wall([rightR, rightC], [nextRightR, nextRightC], nextD):
#                 continue
#             dp[nextRightR][nextRightC] += dp[rightR][rightC]
#             q.append([rightR, rightC, nextRightR, nextRightC, nextD])
#     elif d == SERO:
#         for i in range(len(sero)):
#             leftDr, leftDc, rightDr, rightDc, nextD = sero[i]
#             nextLeftR, nextLeftC = leftR + leftDr, leftC + leftDc
#             nextRightR, nextRightC = rightR + rightDr, rightC + rightDc
#             if not 0 <= nextLeftR < n or not 0 <= nextLeftC < n:
#                 continue
#             if not 0 <= nextRightR < n or not 0 <= nextRightC < n:
#                 continue
#             if wall([rightR, rightC], [nextRightR, nextRightC], nextD):
#                 continue
#             dp[nextRightR][nextRightC] += dp[rightR][rightC]
#             q.append([rightR, rightC, nextRightR, nextRightC, nextD])
#     else:
#         for i in range(len(diagonal)):
#             leftDr, leftDc, rightDr, rightDc, nextD = diagonal[i]
#             nextLeftR, nextLeftC = leftR + leftDr, leftC + leftDc
#             nextRightR, nextRightC = rightR + rightDr, rightC + rightDc
#             if not 0 <= nextLeftR < n or not 0 <= nextLeftC < n:
#                 continue
#             if not 0 <= nextRightR < n or not 0 <= nextRightC < n:
#                 continue
#             if wall([rightR, rightC], [nextRightR, nextRightC], nextD):
#                 continue
#             dp[nextRightR][nextRightC] += dp[rightR][rightC]
#             q.append([rightR, rightC, nextRightR, nextRightC, nextD])
#
# print(dp[-1][-1])

GARO = 0
SERO = 1
DIAGONAL = 2

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
dp[0][0][GARO] = 1
dp[0][1][GARO] = 1
for r in range(n):
    for c in range(2, n):
        if arr[r][c] == 1:
            continue
        dp[r][c][GARO] += dp[r][c - 1][GARO]
        dp[r][c][GARO] += dp[r][c - 1][DIAGONAL]

        dp[r][c][SERO] += dp[r - 1][c][SERO]
        dp[r][c][SERO] += dp[r - 1][c][DIAGONAL]

        if arr[r - 1][c] == 1 or arr[r][c - 1] == 1:
            continue
        dp[r][c][DIAGONAL] += dp[r - 1][c - 1][GARO]
        dp[r][c][DIAGONAL] += dp[r - 1][c - 1][SERO]
        dp[r][c][DIAGONAL] += dp[r - 1][c - 1][DIAGONAL]

print(sum(dp[-1][-1]))