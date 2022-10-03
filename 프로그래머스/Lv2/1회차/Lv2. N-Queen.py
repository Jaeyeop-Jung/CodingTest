# TODO 틀림

result = 0

def takeQueen(row, column, visited):
    visited[row][column] = True

    # 아래 줄
    for i in range(row, len(visited)):
        visited[i][column] = True

    tempRow, tempColumn = row, column
    # 왼쪽 대각선
    while True:
        movedRow, movedColumn = tempRow + 1, tempColumn - 1
        if not 0 <= movedRow < len(visited) or not 0 <= movedColumn < len(visited):
            break
        visited[movedRow][movedColumn] = True
        tempRow, tempColumn = movedRow, movedColumn

    tempRow, tempColumn = row, column
    # 오른쪽 대각선
    while True:
        movedRow, movedColumn = tempRow + 1, tempColumn + 1
        if not 0 <= movedRow < len(visited) or not 0 <= movedColumn < len(visited):
            break
        visited[movedRow][movedColumn] = True
        tempRow, tempColumn = movedRow, movedColumn

def exportQueen(row, column, visited):
    # 아래 줄
    for i in range(row, len(visited)):
        visited[i][column] = False

    tempRow, tempColumn = row, column
    # 왼쪽 대각선
    while True:
        movedRow, movedColumn = tempRow + 1, tempColumn - 1
        if not 0 <= movedRow < len(visited) or not 0 <= movedColumn < len(visited):
            break
        visited[movedRow][movedColumn] = False
        tempRow, tempColumn = movedRow, movedColumn

    tempRow, tempColumn = row, column
    # 오른쪽 대각선
    while True:
        movedRow, movedColumn = tempRow + 1, tempColumn + 1
        if not 0 <= movedRow < len(visited) or not 0 <= movedColumn < len(visited):
            break
        visited[movedRow][movedColumn] = False
        tempRow, tempColumn = movedRow, movedColumn


def dfs(n, row, column, visited):
    if row + 1 == n:
        global result
        result += 1
        return

    takeQueen(row, column, visited)
    for i in range(n):
        if visited[row + 1][i] is False:
            dfs(n, row + 1, i, [[visited[j][k] for k in range(len(visited[j]))] for j in range(n)])
            # dfs(n, row + 1, i, visited)
            # exportQueen(row + 1, i, visited)


def solution(n):
    for i in range(n):
        visited = [[False] * n for i in range(n)]
        dfs(n, 0, i, visited)
    return result

print(solution(4))
