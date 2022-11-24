# TODO 틀림

import math

dRow = [0, 1, 0, -1]
dColumn = [1, 0, -1, 0]
dGaroRotate = [[[1, 0], [0, 1]], [[-1, 0], [0, 1]], [[1, 0], [0, -1]], [[-1, 0], [0, -1]]]
dSeroRotate = [[[0, 1], [1, 0]], [[0, -1], [1, 0]], [[0, -1], [-1, 0]], [[0, 1], [-1, 0]]]

def isFar(one, other):
    if abs(one[0] - other[0]) + abs(one[1] - other[1]) == 0:
        return True
    return False

def dfs(n, board, visited, one, other, cnt):
    if one == [n - 1, n - 1] or other == [n - 1, n - 1]:
        global result
        result = min(result, cnt)
        return
    if cnt == 1:
        print('h')
    for i in range(len(dRow)):
        movedOne = [one[0] + dRow[i], one[1] + dColumn[i]]
        movedOther = [other[0] + dRow[i], other[1] + dColumn[i]]
        if not 0 <= movedOne[0] < n or not 0 <= movedOne[1] < n or not 0 <= movedOther[0] < n or not 0 <= movedOther[1] < n:
            continue
        if visited[movedOne[0]][movedOne[1]] and visited[movedOther[0]][movedOther[1]]:
            continue
        if board[movedOne[0]][movedOne[1]] == 1 or board[movedOther[0]][movedOther[1]] == 1:
            continue
        visited[movedOne[0]][movedOne[1]] = True
        visited[movedOther[0]][movedOther[1]] = True
        dfs(n, board, visited, movedOne, movedOther, cnt + 1)
        visited[movedOne[0]][movedOne[1]] = False
        visited[movedOther[0]][movedOther[1]] = False

    if one[0] == other[0]:  # 가로
        for i in range(len(dGaroRotate)):
            movedOne = [one[0], one[1]]
            for j in range(len(dGaroRotate[i])):
                movedOne = [movedOne[0] + dGaroRotate[i][j][0], movedOne[1] + dGaroRotate[i][j][1]]
                if board[movedOne[0]][movedOne[1]] == 1:
                    break
            else:
                if isFar(movedOne, other): continue
                if not 0 <= movedOne[0] < n or not 0 <= movedOne[1] < n: continue
                if visited[movedOne[0]][movedOne[1]] and visited[other[0]][other[1]]: continue
                visited[movedOne[0]][movedOne[1]] = True
                visited[other[0]][other[1]] = True
                dfs(n, board, visited, movedOne, other, cnt + 1)
                visited[movedOne[0]][movedOne[1]] = False
                visited[other[0]][other[1]] = False
        for i in range(len(dGaroRotate)):
            movedOther = [other[0], other[1]]
            for j in range(len(dGaroRotate[i])):
                movedOther = [movedOther[0] + dGaroRotate[i][j][0], movedOther[1] + dGaroRotate[i][j][1]]
                if board[movedOther[0]][movedOther[1]] == 1:
                    break
            else:
                if isFar(one, movedOther): continue
                if visited[one[0]][one[1]] and visited[movedOther[0]][movedOther[1]]: continue
                visited[one[0]][one[1]] = True
                visited[movedOther[0]][movedOther[1]] = True
                dfs(n, board, visited, one, movedOther, cnt + 1)
                visited[one[0]][one[1]] = False
                visited[movedOther[0]][movedOther[1]] = False
    else:   # 세로
        for i in range(len(dSeroRotate)):
            movedOne = [one[0], one[1]]
            for j in range(len(dSeroRotate[i])):
                movedOne = [movedOne[0] + dSeroRotate[i][j][0], movedOne[1] + dSeroRotate[i][j][1]]
                if not 0 <= movedOne[0] < n or not 0 <= movedOne[1] < n or board[movedOne[0]][movedOne[1]] == 1:
                    break
            else:
                if isFar(movedOne, other): continue
                if not 0 <= movedOne[0] < n or not 0 <= movedOne[1] < n: continue
                if visited[movedOne[0]][movedOne[1]] and visited[other[0]][other[1]]: continue
                visited[movedOne[0]][movedOne[1]] = True
                visited[other[0]][other[1]] = True
                dfs(n, board, visited, movedOne, other, cnt + 1)
                visited[movedOne[0]][movedOne[1]] = False
                visited[other[0]][other[1]] = False
        for i in range(len(dSeroRotate)):
            movedOther = [other[0], other[1]]
            for j in range(len(dSeroRotate[i])):
                movedOther = [movedOther[0] + dSeroRotate[i][j][0], movedOther[1] + dSeroRotate[i][j][1]]
                if board[movedOther[0]][movedOther[1]] == 1:
                    break
            else:
                if isFar(one, movedOther): continue
                if visited[one[0]][one[1]] and visited[movedOther[0]][movedOther[1]]: continue
                visited[one[0]][one[1]] = True
                visited[movedOther[0]][movedOther[1]] = True
                dfs(n, board, visited, one, movedOther, cnt + 1)
                visited[one[0]][one[1]] = False
                visited[movedOther[0]][movedOther[1]] = False




result = math.inf
def solution(board):
    one = [0, 0]
    other = [0, 1]
    visited = [[False] * len(board) for _ in range(len(board))]
    visited[0][1], visited[0][0] = True, True
    n = len(board)
    dfs(n, board, visited, one, other, 0)


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))