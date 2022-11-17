# TODO 틀림

import math
from collections import deque

dRow = [0, 1, 0, -1]
dColumn = [1, 0, -1, 0]
dDiagonalRow = [1, 1, -1, -1]
dDiagonalColumn = [1, -1, -1, 1]

def find(board, str):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == str:
                return [i, j]

def bfs(board, r, c, tR, tC):
    q = deque()
    distance = [[math.inf] * len(board[i]) for i in range(len(board))]
    q.append([r, c, 0])
    distance[r][c] = 0

    while q:
        row, column, cost, = q.popleft()
        distance[row][column] = cost
        for i in range(len(dRow)):
            movedR = row + dRow[i]
            movedC = column + dColumn[i]
            if not 0 <= movedR < len(board) or not 0 <= movedC < len(board[0]):
                continue
            if cost + 2 < distance[movedR][movedC]:
                distance[movedR][movedC] = cost + 2
                q.append([movedR, movedC, cost + 2])
        for i in range(len(dDiagonalRow)):
            movedR = row + dDiagonalRow[i]
            movedC = column + dDiagonalColumn[i]
            if not 0 <= movedR < len(board) or not 0 <= movedC < len(board[0]):
                continue
            if cost + 3 < distance[movedR][movedC]:
                distance[movedR][movedC] = cost + 3
                q.append([movedR, movedC, cost + 3])
    return distance[tR][tC]

# def solution(numbers):
#     board = [['1', "2", '3'], ['4', '5', '6'], ['7', '8', '9'], ['*', '0', '#']]
#     left = [1, 0]
#     right = [1, 2]
#
#     result = 0
#     for i in range(len(numbers)):
#         tR, tC = find(board, numbers[i])
#         if (left[0] == tR and left[1] == tC) or (right[0] == tR and right[1] == tC):
#             result += 1
#             continue
#         leftCost = bfs(board, left[0], left[1], tR, tC)
#         rightCost = bfs(board, right[0], right[1], tR, tC)
#         if leftCost < rightCost:
#             result += leftCost
#             left = [tR, tC]
#         else:
#             result += rightCost
#             right = [tR, tC]
#     return result

result = math.inf
def dfs(board, numbers, i, left, right, cnt):
    if len(numbers) == i:
        global result
        result = min(result, cnt)
        return

    tR, tC = find(board, numbers[i])
    leftCost = bfs(board, left[0], left[1], tR, tC)
    rightCost = bfs(board, right[0], right[1], tR, tC)
    if leftCost == 0 and rightCost == 0:
        dfs(board, numbers, i + 1, [tR, tC], right, cnt + 1)
        dfs(board, numbers, i + 1, left, [tR, tC], cnt + 1)
    elif leftCost == 0:
        dfs(board, numbers, i + 1, [tR, tC], right, cnt + 1)
    elif rightCost == 0:
        dfs(board, numbers, i + 1, left, [tR, tC], cnt + 1)
    elif leftCost == rightCost:
        dfs(board, numbers, i + 1, [tR, tC], right, cnt + leftCost)
        dfs(board, numbers, i + 1, left, [tR, tC], cnt + rightCost)
    elif leftCost < rightCost:
        dfs(board, numbers, i + 1, [tR, tC], right, cnt + leftCost)
    else:
        dfs(board, numbers, i + 1, left, [tR, tC], cnt + rightCost)


def solution(numbers):
    board = [['1', "2", '3'], ['4', '5', '6'], ['7', '8', '9'], ['*', '0', '#']]
    left = [1, 0]
    right = [1, 2]

    dfs(board, numbers, 0, left, right, 0)

    return result


# print(solution('1756'))
# print(solution('5123'))
print(solution('1469#76'))
# print(solution('59'))