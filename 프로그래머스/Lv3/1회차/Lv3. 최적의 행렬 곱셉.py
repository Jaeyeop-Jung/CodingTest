# TODO 틀림 

import math

def solution(matrix_sizes):
    dp = [[math.inf for i in range(len(matrix_sizes))] for j in range(len(matrix_sizes))]
    for i in range(len(matrix_sizes)):
        dp[i][i] = 0

    for gap in range(1, len(dp)):
        for start in range(len(matrix_sizes)):
            end = start + gap
            if len(matrix_sizes) <= end:
                break
            if gap == 1:
                dp[start][end] = min(dp[start][end], matrix_sizes[start][0] * matrix_sizes[start][1] * matrix_sizes[end][1])
                continue
            for sep in range(start, end):
                dp[start][end] = min(dp[start][end], dp[start][sep] + dp[sep + 1][end] + matrix_sizes[start][0] * matrix_sizes[sep][1] * matrix_sizes[end][1])

    return dp[0][-1]

print(solution([[5,3],[3,10],[10,6]]))
