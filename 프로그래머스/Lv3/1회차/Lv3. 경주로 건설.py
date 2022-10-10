# TODO 틀림 많이 어렵다. 생각을 깊게 해봐야됌 https://school.programmers.co.kr/questions/30355

import math
from collections import deque

dRow = [0, 1, 0, -1]
dColumn = [1, 0, -1, 0]

def solution(board):
    q = deque()
    price = [[[math.inf] * 4 for j in range(len(board))] for i in range(len(board[0]))]
    q.append([0, 0, 0, -1])

    while q:
        row, column, cost, direction = q.popleft()
        if row == len(board) - 1 and column == len(board[0]) - 1:
            continue

        for i in range(len(dRow)):
            movedRow, movedColumn = row + dRow[i], column + dColumn[i]
            if not 0 <= movedRow < len(board) or not 0 <= movedColumn < len(board[movedRow]):
                continue

            if direction == i or direction == -1:
                nextCost = cost + 100
            else:
                nextCost = cost + 600
            if price[movedRow][movedColumn][i] < nextCost or board[movedRow][movedColumn] == 1:
                continue

            q.append([movedRow, movedColumn, nextCost, i])
            price[movedRow][movedColumn][i] = nextCost

    return min(price[-1][-1])

print(solution([[0,0,0],[0,0,0],[0,0,0]]))
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))
