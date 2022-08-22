# TODO 틀림 https://jae04099.tistory.com/entry/%EB%B0%B1%EC%A4%80-7576-%ED%86%A0%EB%A7%88%ED%86%A0-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%95%B4%EC%84%A4%ED%8F%AC%ED%95%A8

from collections import deque

dRow = [0, 0, 1, -1]
dColumn = [1, -1, 0, 0]

m, n = map(int, input().split())
graph = []
queue = deque()
for i in range(n):
    inp = list(map(int, input().split()))
    for j in range(len(inp)):
        if inp[j] == 1:
            queue.append([i, j])
    graph.append(inp)

def bfs():
    while queue:
        popRow, popColumn = queue.popleft()
        for i in range(len(dRow)):
            movedRow = popRow + dRow[i]
            movedColumn = popColumn + dColumn[i]
            if not 0 <= movedRow < n or not 0 <= movedColumn < m:
                continue
            if graph[movedRow][movedColumn] == 0:
                graph[movedRow][movedColumn] = graph[popRow][popColumn] + 1
                queue.append([movedRow, movedColumn])

bfs()

result = -1
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
        result = max(result, j)
print(result - 1)
