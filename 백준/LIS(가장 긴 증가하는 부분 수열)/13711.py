# TODO 틀림

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# arr = [list(map(int, input().split())) for i in range(2)]
#
# dp = [[0] * (n + 1) for i in range(n + 1)]
#
#
# for i in range(n):
#     for j in range(n):
#         if arr[0][i] == arr[1][j]:
#             dp[i + 1][j + 1] = dp[i][j] + 1
#         else:
#             dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
#
# print(max(map(max, dp)))

