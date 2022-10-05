# TODO 틀림 예외 케이스를 잘 생각해봐라

def solution(m, n, puddles):
    arr = [[True] * m for i in range(n)]
    for column, row in puddles:
        arr[row - 1][column - 1] = False

    dp = [[0] * m for i in range(n)]
    for i in range(1, len(dp[0])):
        if arr[0][i] is True:
            dp[0][i] = dp[0][i - 1]
    for i in range(1, len(dp)):
        if arr[i][0] is True:
            dp[i][0] = dp[i - 1][0]
    for i in range(1, len(dp)):
        for j in range(1, len(dp[i])):
            if arr[i][j] is True:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007

    print(dp)
    return dp[n - 1][m - 1]


print(solution(4, 3, [[2, 1], [1, 2]]))
# print(solution(3, 1, [[1, 1]]))