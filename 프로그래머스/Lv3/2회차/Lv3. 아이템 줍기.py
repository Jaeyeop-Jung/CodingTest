# TODO 아이디어는 맞았는데 구현이 또 틀림

import math

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def dfs(board, visited, x, y, cnt, itemX, itemY):
    if x == itemX and y == itemY:
        global result
        result = min(result, cnt // 2)
        return
    for i in range(4):
        movedX = x + dx[i]
        movedY = y + dy[i]
        if not 0 <= movedX < 102 or not 0 <= movedY < 102:
            continue
        if board[movedY][movedX] == 0:
            continue
        if visited[movedY][movedX]:
            continue
        visited[movedY][movedX] = True
        dfs(board, visited, movedX, movedY, cnt + 1, itemX, itemY)
        visited[movedY][movedX] = False

result = math.inf
def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[0] * 102 for i in range(102)]
    for lx, ly, rx, ry in rectangle:    # 전체 다 채우기
        for x in range(lx * 2, 2 * rx + 1):
            for y in range(ly * 2, 2 * ry + 1):
                board[y][x] = 1

    for lx, ly, rx, ry in rectangle:    # 겹치는 부분 빼기
        for x in range(lx * 2 + 1, 2 * rx):
            for y in range(ly * 2 + 1, 2 * ry):
                board[y][x] = 0

    visited = [[False] * 102 for i in range(102)]
    dfs(board, visited, characterX * 2, characterY * 2, 0, itemX * 2, itemY * 2)

    return result


print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))
