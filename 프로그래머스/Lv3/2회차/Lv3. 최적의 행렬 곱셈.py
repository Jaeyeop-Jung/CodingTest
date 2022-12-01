# TODO 틀림

# import math
#
# def dfs(matrix, cur, total):
#     if not matrix:
#         global result
#         result = min(result, total)
#         return
#
#     for i in range(len(matrix)):
#         if matrix[i][1] == cur[0]:
#             dfs(matrix[:i] + matrix[i + 1:], [matrix[i][0], cur[1]], total + matrix[i][0] * cur[0] * cur[1])
#         elif cur[1] == matrix[i][0]:
#             dfs(matrix[:i] + matrix[i + 1:], [cur[0], matrix[i][1]], total + cur[0] * cur[1] * matrix[i][1])
#
# result = math.inf
# def solution(matrix_sizes):
#     for i in range(len(matrix_sizes)):
#         cur = matrix_sizes[i]
#         dfs(matrix_sizes[:i] + matrix_sizes[i + 1:], cur, 0)
#     return result
import math


def solution(matrix_sizes):
    n = len(matrix_sizes)
    dp = [[math.inf for i in range(n)] for j in range(n)]
    for i in range(len(dp)):
        dp[i][i] = 0
    for i in range(n):
        for start in range(n - i):
            end = start + i
            for k in range(start, end):
                dp[start][end] = min(dp[start][end], dp[start][k] + dp[k + 1][end] + (matrix_sizes[start][0] * matrix_sizes[k][1] * matrix_sizes[end][1]))
    return dp[0][-1]

print(solution([[5,3],[3,10],[10,6]]))




