# TODO 틀림 구현을 조금 더 생각해라

blocks = [
    [[0, -1], [1, -1], [1, 0], [1, 1],  [0, 1]], # ㄴ
    [[1, 0], [1, 1], [0, 1], [-1, 1],   [-1, 0]], # J
    [[-1, -1], [0, -1], [1, -1], [1, 0],    [-1, 0]], # L
    [[1, -1], [1, 0], [1, 1], [0, 1],   [0, -1]], #ㅢ
    [[0, 1], [1, 0], [1, 1], [1, 2] ,[0, 2]] # ㅗ
]

def remove(board, r, c):
    n = len(board)
    for block in blocks:
        removed = []
        movedR, movedC = r + block[0][0], c + block[0][1]
        if not 0 <= movedR < n or not 0 <= movedC < n:
            continue
        num = board[movedR][movedC]
        for i in range(len(block) - 1):
            movedR, movedC = r + block[i][0], c + block[i][1]
            if not 0 <= movedR < n or not 0 <= movedC < n:
                break
            if num != board[movedR][movedC]:
                break
            removed.append([movedR, movedC])
        else:
            movedR, movedC = r + block[-1][0], c + block[-1][1]
            if canFill(board, movedR, movedC):
                for r, c in removed:
                    board[r][c] = 0
            return True
    return False

def canFill(board, r, c):
    if board[r][c] != 0:
        return False
    for r2 in range(r):
        if board[r2][c] != 0:
            return False
    return True


def solution(board):
    n = len(board)

    result = 0
    c = 0
    while c < n:
        r = 0
        while r < n:
            if board[r][c] == 0:
                r += 1
                continue
            r = r - 1
            isRemoved = remove(board, r, c)
            if isRemoved:
                result += 1
            break

        if isRemoved:
            c = max(c - 2, 0)
            isRemoved = False
        else:
            c += 1
    return result