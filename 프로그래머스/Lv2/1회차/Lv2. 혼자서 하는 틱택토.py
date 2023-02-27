
dR = [0, 1, 1, 1, 0, -1, -1, -1]
dC = [1, 1, 0, -1, -1, -1, 0, 1]

def isEnd(board, target):
    for r in range(3):
        for c in range(3):
            if board[r][c] == target:
                curR, curC = r, c
                for i in range(len(dR)):
                    for j in range(2):
                        movedR, movedC, = curR + dR[i], curC + dC[i]
                        if not 0 <= movedR < 3 or not 0 <= movedC < 3:
                            break
                        if not board[movedR][movedC] == target:
                            break
                        curR, curC = movedR, movedC
                    else:
                        return True
    return False


def solution(board):
    oCnt, xCnt = 0, 0
    for i in board:
        oCnt += i.count('O')
        xCnt += i.count('X')

    if oCnt == xCnt:
        if not isEnd(board, 'O'):
            return 1
        else:
            return 0
    elif oCnt == xCnt + 1:
        if not isEnd(board, 'X'):
            return 1
        else:
            return 0
    else:
        return 0


print(solution(["O.X", ".O.", "..X"]))
print(solution(["OOO", "...", "XXX"]))
print(solution(["...", ".X.", "..."]))
print(solution(["...", "...", "..."]))
