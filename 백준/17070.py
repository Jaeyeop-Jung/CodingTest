# import sys
#
# input = sys.stdin.readline
#
# HORIZONTAL = 0
# VERTICAL = 1
# DIAGONAL = 2
# dxy = ((0, 1), (1, 0), (1, 1))
#
# n = int(input())
# house = [list(map(int, input().split())) for _ in range(n)]
# # if arr[-1][-1] == 1:
# #     print(0)
# #     exit()
#
# def inRange(r, c):
#     if not 0 <= r < n or not 0 <= c < n:
#         return False
#     return True
#
# def solve(x, y, shape):
#     if x == n - 1 and y == n - 1:
#         return 1
#     if dp[x][y][shape] != -1:
#         return dp[x][y][shape]
#
#     ret = 0
#     if shape == HORIZONTAL or shape == DIAGONAL:
#         nx, ny = x + dxy[HORIZONTAL][0], y + dxy[HORIZONTAL][1]
#         if nx < n and ny < n and house[nx][ny] == 0:
#             ret += solve(x + dxy[HORIZONTAL][0], y + dxy[HORIZONTAL][1], HORIZONTAL)
#
#     if shape == VERTICAL or shape == DIAGONAL:
#         nx, ny = x + dxy[VERTICAL][0], y + dxy[VERTICAL][1]
#         if nx < n and ny < n and house[nx][ny] == 0:
#             ret += solve(x + dxy[VERTICAL][0], y + dxy[VERTICAL][1], VERTICAL)
#
#     nx, ny = x + dxy[DIAGONAL][0], y + dxy[DIAGONAL][1]
#     if nx < n and ny < n and house[nx][ny] == 0 and house[nx - 1][ny] == 0 and house[nx][ny - 1] == 0:
#         ret += solve(x + dxy[DIAGONAL][0], y + dxy[DIAGONAL][1], DIAGONAL)
#     dp[x][y][shape] = ret
#     return ret
#
# dp = [[[-1] * 3 for _ in range(n)] for _ in range(n)]
# print(solve(0, 1, HORIZONTAL))

import sys

input = sys.stdin.readline

garo = 0
diagonal = 1
sero = 2

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


def inRange(r, c):
    if not 0 <= r < n or not 0 <= c < n:
        return False
    return True


def dfs(arr, dp, r, c, direction):
    if r == n - 1 and c == n - 1:
        return 1
    if dp[r][c][direction] != -1:
        return dp[r][c][direction]

    ret = 0
    if direction == garo:
        if inRange(r, c + 1) and arr[r][c + 1] == 0:
            ret += dfs(arr, dp, r, c + 1, garo)
        if inRange(r + 1, c + 1) and arr[r + 1][c + 1] == 0 and arr[r + 1][c] == 0 and arr[r][c + 1] == 0:
            ret += dfs(arr, dp, r + 1, c + 1, diagonal)
    elif direction == diagonal:
        if inRange(r, c + 1) and arr[r][c + 1] == 0:
            ret += dfs(arr, dp, r, c + 1, garo)
        if inRange(r + 1, c + 1) and arr[r + 1][c + 1] == 0 and arr[r + 1][c] == 0 and arr[r][c + 1] == 0:
            ret += dfs(arr, dp, r + 1, c + 1, diagonal)
        if inRange(r + 1, c) and arr[r + 1][c] == 0:
            ret += dfs(arr, dp, r + 1, c, sero)
    else:
        if inRange(r + 1, c + 1) and arr[r + 1][c + 1] == 0 and arr[r + 1][c] == 0 and arr[r][c + 1] == 0:
            ret += dfs(arr, dp, r + 1, c + 1, diagonal)
        if inRange(r + 1, c) and arr[r + 1][c] == 0:
            ret += dfs(arr, dp, r + 1, c, sero)
    dp[r][c][direction] = ret
    return dp[r][c][direction]


dp = [[[-1] * 3 for _ in range(n)] for _ in range(n)]
print(dfs(arr, dp, 0, 1, garo))