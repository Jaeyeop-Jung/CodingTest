
dRow = [1, 1, 1]
dColumn = [-1, 0, 1]

result = 0

def dfs(n, board, r, c):
    if r == n - 1:
        global result
        result += 1
        return
    board[r][c] = False

    for i in range(3):
        movedR = r + dRow[i]
        movedC = c + dColumn[i]
        while 0 <= movedR < n and 0 <= movedC < n:
            board[movedR][movedC] = False
            movedR += dRow[i]
            movedC += dColumn[i]


    for i in range(n):
        if board[r + 1][i]:
            dfs(n, [j[:] for j in board], r + 1, i)
            board[r + 1][i] = True

def solution(n):
    board = [[True] * n for i in range(n)]
    for i in range(n):
        dfs(n, [i[:] for i in board], 0, i)
    return result

print(solution(4))
