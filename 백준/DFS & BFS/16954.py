# TODO 틀림 조금 더 최적화 할 방법을 찾아봐라

dR = [0, 0, 1, 1, 1, 0, -1, -1, -1]
dC = [0, 1, 1, 0, -1, -1, -1, 0, 1]

def down(board):
    newBoard = [['.'] * 8]
    for i in range(7):
        newBoard.append(board[i][:])
    return newBoard

def dfs(board, r, c, cnt):
    if cnt == 8:
        print(1)
        exit()
    newBoard = down(board)
    for i in range(len(dR)):
        movedR, movedC = r + dR[i], c + dC[i]
        if not 0 <= movedR < 8 or not 0 <= movedC < 8:
            continue
        if newBoard[movedR][movedC] == '#' or board[movedR][movedC] == '#':
            continue
        dfs(newBoard, movedR, movedC, cnt + 1)

arr = [list(input()) for _ in range(8)]
dfs(arr, 7, 0, 0)
print(0)