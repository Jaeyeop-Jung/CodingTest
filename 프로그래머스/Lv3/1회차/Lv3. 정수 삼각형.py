
def solution(triangle):
    if len(triangle) == 1:
        return triangle[0][0]
    dp = [[0] * len(triangle[i]) for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    for i in range(1, len(dp)):
        for j in range(len(dp[i])):
            if j == 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j] + triangle[i][j])
            elif j == len(dp[i]) - 1:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + triangle[i][j])
            else:
                dp[i][j] = max(dp[i][j], dp[i - 1][j] + triangle[i][j], dp[i - 1][j - 1] + triangle[i][j])
    return max(map(max, dp))

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
