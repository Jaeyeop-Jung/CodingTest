#
# def notPick(board, r, c, boole):
#     board[r][c] = boole
#     movedR, movedC = r, c
#     while True:
#         movedR += 1
#         movedC += 1
#         if not 0 <= movedR < n or not 0 <= movedC < n:
#             break
#         board[movedR][movedC] = boole
#     movedR, movedC = r, c
#     while True:
#         movedR += 1
#         movedC -= 1
#         if not 0 <= movedR < n or not 0 <= movedC < n:
#             break
#         board[movedR][movedC] = boole
#     movedR, movedC = r, c
#     while True:
#         movedR += 1
#         if not 0 <= movedR < n or not 0 <= movedC < n:
#             break
#         board[movedR][movedC] = boole
#
#
# def dfs(board, r, c, cnt):
#     if cnt == n - 1:
#         global result
#         result += 1
#         return
#     notPick(board, r, c, False)
#     for i in range(n):
#         if board[r + 1][i]:
#             dfs([b[:] for b in board], r+1, i, cnt + 1)
#
# T = int(input())
# result = 0
# for test_case in range(1, T + 1):
#     n = int(input())
#     board = [[True] * n for i in range(n)]
#
#     for i in range(n):
#         dfs([b[:] for b in board], 0, i, 0)
#         notPick(board, 0, i, True)
#
#     print('#' + str(test_case) + ' ' + str(result))
#     result = 0


def notPick(board, r, c, boole):
    board[r][c] = boole
    movedR, movedC = r, c
    while True:
        movedR += 1
        movedC += 1
        if not 0 <= movedR < n or not 0 <= movedC < n:
            break
        board[movedR][movedC] = boole
    movedR, movedC = r, c
    while True:
        movedR += 1
        movedC -= 1
        if not 0 <= movedR < n or not 0 <= movedC < n:
            break
        board[movedR][movedC] = boole
    movedR, movedC = r, c
    while True:
        movedR += 1
        if not 0 <= movedR < n or not 0 <= movedC < n:
            break
        board[movedR][movedC] = boole

def canTake(board, r, c):
    for i in range(r):
        for j in range(n):
            if abs(i - r) == abs(j - c) and not board[i][j]:
                return False
            elif j == c and i != r and not board[i][j]:
                return False
    return True

def dfs(board, r, c, cnt):
    if cnt == n - 1:
        global result
        result += 1
        return
    board[r][c] = False
    for i in range(n):
        if canTake(board, r+1, i):
            dfs(board, r+1, i, cnt + 1)
            board[r+1][i] = True

result = 0
n = int(input())
board = [[True] * n for i in range(n)]

for i in range(n):
    dfs([b[:] for b in board], 0, i, 0)
    board[0][i] = True

print(result)
result = 0