# TODO 틀림 https://kimjingo.tistory.com/216

dRow = [0, 1, 0, -1]
dColumn = [1, 0, -1, 0]

def dfs(cycle, grid, direction, row, column, cnt):
    if cycle[row][column][direction] == 1:
        return cnt + 1
    cycle[row][column][direction] = True
    idx = direction
    if grid[row][column] == 'L':
        idx = (direction - 1) % 4
        idx = (idx - 2) % 4
        movedRow = row + dRow[idx]
        movedColumn = column + dColumn[idx]
    elif grid[row][column] == 'R':
        idx = (direction + 1) % 4
        idx = (idx - 2) % 4
        movedRow = row + dRow[idx]
        movedColumn = column + dColumn[idx]
    else:
        movedRow = row + dRow[direction]
        movedColumn = column + dColumn[direction]
    if movedRow >= len(grid):
        movedRow = 0
    elif movedRow <= -1:
        movedRow = len(grid) - 1
    if movedColumn >= len(grid[0]):
        movedColumn = 0
    elif movedColumn <= -1:
        movedColumn = len(grid[0]) - 1
    return dfs(cycle, grid, idx, movedRow, movedColumn, cnt + 1)

def solution(grid):
    result = []
    cycle = [[[False] * 4 for i in range(len(grid[0]))] for j in range(len(grid))]
    for direction in range(4):
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if cycle[row][column][direction] == 1:
                    continue
                result.append(dfs(cycle, grid, direction, row, column, -1))
    result.sort()
    return result

solution(["S"])