from collections import deque

dRow = [0, 0, 1, -1]
dColumn = [1, -1, 0, 0]

def bfs(maps, row, column, cnt):
    visited = [[False] * len(maps[0]) for i in range(len(maps))]
    result = [[-1] * len(maps[0]) for i in range(len(maps))]
    q = deque()
    q.append([row, column, cnt])

    while q:
        pop = q.popleft()
        visited[pop[0]][pop[1]] = True
        result[pop[0]][pop[1]] = pop[2]
        for i in range(len(dRow)):
            movedRow = pop[0] + dRow[i]
            movedColumn = pop[1] + dColumn[i]
            if not 0 <= movedRow < len(maps) or not 0 <= movedColumn < len(maps[0]):
                continue
            if maps[movedRow][movedColumn] == 0:
                continue
            if visited[movedRow][movedColumn] is True:
                continue
            q.append([movedRow, movedColumn, pop[2] + 1])
            visited[movedRow][movedColumn] = True
    return result


def solution(maps):
    visited = bfs(maps, 0, 0, 1)
    return visited[len(maps) - 1][len(maps[0]) - 1]


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))