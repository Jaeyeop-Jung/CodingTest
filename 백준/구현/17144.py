import sys

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

input = sys.stdin.readline

r, c, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
cleaner = []
for curR in range(r):
    for curC in range(c):
        if board[curR][curC] == -1:
            cleaner.append([curR, curC])

def extend():
    global board
    newBoard = [[0] * c for _ in range(r)]
    for curR, curC in cleaner:
        newBoard[curR][curC] = -1
    for curR in range(r):
        for curC in range(c):
            if board[curR][curC] == -1 or board[curR][curC] == 0:
                continue
            cnt = 0
            extendDust = board[curR][curC] // 5
            for i in range(4):
                movedR, movedC = curR + dR[i], curC + dC[i]
                if not 0 <= movedR < r or not 0 <= movedC < c:
                    continue
                if newBoard[movedR][movedC] == -1:
                    continue
                cnt += 1
                newBoard[movedR][movedC] += extendDust
            newBoard[curR][curC] += board[curR][curC] - extendDust * cnt
    board = newBoard

def clean(board):
    startR, startC = cleaner[0]
    curR, curC = startR, startC
    idx = 3
    movement = [startR, c, startR, c]
    for move in movement:
        for _ in range(move):
            movedR, movedC = curR + dR[idx], curC + dC[idx]
            if not 0 <= movedR < r or not 0 <= movedC < c:
                break
            if board[movedR][movedC] == -1:
                board[curR][curC] = 0
                break
            if board[curR][curC] == -1:
                curR, curC = movedR, movedC
                continue
            board[curR][curC] = board[movedR][movedC]
            curR, curC = movedR, movedC
        idx += 1
        idx %= 4

    startR, startC = cleaner[1]
    curR, curC = startR, startC
    movement = [[r - startR, 1], [c, 0], [r - startR - 1, -1], [c, -2]]
    for move in movement:
        num, i = move
        for _ in range(num):
            movedR, movedC = curR + dR[i], curC + dC[i]
            if not 0 <= movedR < r or not 0 <= movedC < c:
                break
            if board[movedR][movedC] == -1:
                board[curR][curC] = 0
                break
            if board[curR][curC] == -1:
                curR, curC = movedR, movedC
                continue
            board[curR][curC] = board[movedR][movedC]
            curR, curC = movedR, movedC

for _ in range(t):
    extend()
    clean(board)

print(sum(map(sum, board)) + 2)
