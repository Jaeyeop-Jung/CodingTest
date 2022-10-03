
def solution(land):
    if len(land) == 1:
        return max(land[0])
    dp = [[0] * len(land[i]) for i in range(len(land))]
    dp[0] = land[0][:]
    for i in range(len(dp) - 1):
        for j in range(len(dp[i])):
            for k in range(len(dp[i + 1])):
                if j != k:
                    dp[i + 1][k] = max(dp[i + 1][k], dp[i][j] + land[i + 1][k])
    return max(dp[len(dp) - 1][:])


print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))
print(solution([[1,1,1,1],[1,1,1,1],[1,1,1,1]]))