import copy
import sys
from collections import deque

input = sys.stdin.readline

dRow = [0, 0, 1, -1]
dColumn = [1, -1, 0, 0]

def dfs(graph, v, visitedLocation, visitedAlphabet, count):
    global result
    result = max(result, count)
    for i in range(len(dRow)):
        movedRow = v[0] + dRow[i]
        movedColumn = v[1] + dColumn[i]
        if not 0 <= movedRow < row or not 0 <= movedColumn < column:
            continue
        if visitedLocation[movedRow][movedColumn] is False and not graph[movedRow][movedColumn] in visitedAlphabet:
            # visitedAlphabet.add(graph[movedRow][movedColumn])
            # visitedLocation[movedRow][movedColumn] = True
            alphabet_copy = copy.deepcopy(visitedAlphabet)
            alphabet_copy.add(graph[movedRow][movedColumn])
            location_copy = [[] * column for _ in range(row)]
            for j in range(len(graph)):
                    location_copy[j] = visitedLocation[j][:]

            location_copy[movedRow][movedColumn] = True
            dfs(graph, [movedRow, movedColumn], location_copy, alphabet_copy, count + 1)
            # visitedAlphabet.remove(graph[movedRow][movedColumn])
            # visitedLocation[movedRow][movedColumn] = False

def bfs(graph, v, count):
    global result
    count += 1
    queue = set()
    queue.add((v[0], v[1], count, graph[v[0]][v[1]]))

    while queue:
        x, y, cnt, alphabet = queue.pop()
        result = max(result, cnt)
        for i in range(len(dRow)):
            movedRow = x + dRow[i]
            movedColumn = y + dColumn[i]
            if not 0 <= movedRow < row or not 0 <= movedColumn < column:
                continue
            if graph[movedRow][movedColumn] not in alphabet:
                queue.add((movedRow, movedColumn, cnt + 1, alphabet + graph[movedRow][movedColumn]))


row, column = map(int, input().split())
graph = [list(input()) for _ in range(row)]
visited = [[False] * column for _ in range(row)]
result = 0

newVisitedAlphabet = set()
newVisitedAlphabet.add(graph[0][0])
visited[0][0] = True

# dfs(graph, [0, 0], visited, newVisitedAlphabet, 1)
bfs(graph, [0, 0], 0)
print(result)