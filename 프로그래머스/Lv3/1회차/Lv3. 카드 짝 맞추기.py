# TODO 틀림

import math
from itertools import product
from itertools import permutations
from collections import deque

ableDirection = ['r', 'd', 'l', 'u', 'cr', 'cd', 'cl', 'cu']
direction = ['r', 'd', 'l', 'u']
dRow = [0, 1, 0, -1]
dColumn = [1, 0, -1, 0]

def move(board, r, c, d):
    if d in direction:
        index = direction.index(d)
        movedRow = r + dRow[index]
        movedColumn = c + dColumn[index]
        if not 0 <= movedRow < 4 or not 0 <= movedColumn < 4:
            return [r, c]
        return [movedRow, movedColumn]
    else:
        movedRow, movedColumn = r, c
        d = d[1]
        while True:
            index = direction.index(d)
            movedRow += dRow[index]
            movedColumn += dColumn[index]
            if not 0 <= movedRow < 4 or not 0 <= movedColumn < 4:
                return [movedRow - dRow[index], movedColumn - dColumn[index]]
            if not 1 <= movedRow <= 2 or not 1 <= movedColumn <= 2:
                return  [movedRow, movedColumn]
            if board[movedRow][movedColumn] != 0:
                return  [movedRow, movedColumn]

# def findCardAndEnter(board, r, c, target):
#     if board[r][c] == target:
#         board[r][c] = 0
#         return 1
#     minMove = math.inf
#     finalRow, finalColumn = 0, 0
#     for d1, d2, d3 in list(product(ableDirection, repeat=3)):
#         movedRow, movedColumn = r, c
#         tempBoard = [[board[row][column] for column in range(len(board[row]))] for row in range(len(board))]
#         cnt = 0
#         movedRow, movedColumn = move(tempBoard, movedRow, movedColumn, d1)
#         cnt += 1
#         if tempBoard[movedRow][movedColumn] == target:
#             tempBoard[movedRow][movedColumn] = 0
#             if cnt + 1 < minMove:
#                 minMove = cnt + 1
#                 finalRow, finalColumn = movedRow, movedColumn
#             continue
#         movedRow, c = move(tempBoard, movedRow, movedColumn, d2)
#         cnt += 1
#         if tempBoard[movedRow][movedColumn] == target:
#             tempBoard[movedRow][movedColumn] = 0
#             if cnt + 1 < minMove:
#                 minMove = cnt + 1
#                 finalRow, finalColumn = movedRow, movedColumn
#             continue
#         movedRow, movedColumn = move(tempBoard, movedRow, movedColumn, d3)
#         cnt += 1
#         if tempBoard[movedRow][movedColumn] == target:
#             tempBoard[movedRow][movedColumn] = 0
#             if cnt + 1 < minMove:
#                 minMove = cnt + 1
#                 finalRow, finalColumn = movedRow, movedColumn
#             continue
#     board[finalRow][finalColumn] = 0
#     return minMove

def bfs(board, r, c, target):
    q = deque()
    q.append([r, c, 0])

    temp = [[math.inf] * len(board[i]) for i in range(len(board))]
    while q:
        row, column, cnt = q.popleft()
        for dList in product(ableDirection, repeat=3):
            for i, d in enumerate(dList):
                movedRow, movedColumn, = move(board, row, column, d)
                if cnt + i + 1 < temp[movedRow][movedColumn]:
                    temp[movedRow][movedColumn] = cnt + i + 1
                    q.append([movedRow, movedColumn,  cnt + 1])

    minBoardValue, row, column = math.inf, 0, 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == target and temp[i][j] < minBoardValue:
                minBoardValue = temp[i][j]
                row, column = i, j
    board[row][column] = 0
    return row, column, temp[row][column] + 1

def solution(board, r, c):
    result = math.inf
    cardMax = max(map(max, board))
    card = [i for i in range(1, cardMax + 1)]
    for i in permutations(card):
        tempBoard = [[board[row][column] for column in range(len(board[row]))] for row in range(len(board))]
        cnt = 0
        tempRow, tempColumn = r, c
        for targetCard in i:
            tempRow, tempColumn, tempCnt = bfs(tempBoard, tempRow, tempColumn, targetCard)
            cnt += tempCnt
            tempRow, tempColumn, tempCnt = bfs(tempBoard, tempRow, tempColumn, targetCard)
            cnt += tempCnt
        result = min(result, cnt)

    return result

# print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))
print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1))