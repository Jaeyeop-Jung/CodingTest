# TODO 틀림

def solution(board):
    dp = [[0] * len(board[0]) for i in range(len(board))]
    for i in range(len(board[0])):
        if board[0][i] == 1:
            dp[0][i] = 1
    for i in range(len(board)):
        if board[i][0] == 1:
            dp[i][0] = 1

    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    return max(map(max, dp)) ** 2

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(solution([[0,0,1,1],[1,1,1,1]]))