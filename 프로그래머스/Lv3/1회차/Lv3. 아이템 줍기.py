# TODO 틀림 아이디어는 맞았음

import math
from pprint import pprint

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

result = math.inf

def add(board, rectangle):
    startX, startY, endX, endY = rectangle
    startX, startY, endX, endY = startX * 2, startY * 2, endX * 2, endY * 2
    for y in range(startY, endY + 1):
        for x in range(startX, endX + 1):
            if board[y][x] != 1:
                board[y][x] = 1

def extractBoundary(board, rectangle):
    startX, startY, endX, endY = rectangle
    startX, startY, endX, endY = startX * 2, startY * 2, endX * 2, endY * 2
    for y in range(startY + 1, endY):
        for x in range(startX + 1, endX):
            board[y][x] = 0

def dfs(board, visited, cx, cy, ix, iy, cnt):
    if cx == ix and cy == iy:
        global result
        result = min(result, cnt)

    visited[cy][cx] = True
    for i in range(len(dx)):
        movedX = cx + dx[i]
        movedY = cy + dy[i]
        if not 0 <= movedX < 51 * 2 or not 0 <= movedY < 51 * 2:
            continue
        if not visited[movedY][movedX] and board[movedY][movedX] == 1:
            dfs(board, visited, movedX, movedY, ix, iy, cnt + 1)
            visited[movedY][movedX] = False

def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[0] * 51 * 2 for _ in range(51 * 2)]

    for i in range(len(rectangle)):
        add(board, rectangle[i])
    for i in range(len(rectangle)):
        extractBoundary(board, rectangle[i])
    visited = [[False] * 51 * 2 for _ in range(51 * 2)]
    dfs(board, visited, characterX * 2, characterY * 2, itemX * 2, itemY * 2, 0)

    return result // 2

print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))