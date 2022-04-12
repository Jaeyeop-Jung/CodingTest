import sys
import heapq
INF = int(1e9)
# input = sys.stdin.readline

n = int(input())
graph = []
for i in range(n): # 입력
    graph.append(list(input()))

for i in range(len(graph)): # 0과 1을 교체 후 int형으로 변경
    for j in range(len(graph[i])):
        if graph[i][j] == '1':
            graph[i][j] = 0
        else:
            graph[i][j] = 1

def dijkstra():
    heap = []
    distance = [[INF] * n for i in range(n)]
    dRow = [0, 0, 1, -1]
    dColumn = [1, -1, 0, 0]

    heapq.heappush(heap, [0, 0, 0])
    distance[0][0] = 0
    while heap:
        dist, row, column = heapq.heappop(heap)

        if distance[row][column] < dist:
            continue

        for i in range(4):
            movedRow, movedColumn = row + dRow[i], column + dColumn[i]
            if movedRow < 0 or n <= movedRow or movedColumn < 0 or n <= movedColumn:
                continue

            cost = dist + graph[movedRow][movedColumn]
            if cost < distance[movedRow][movedColumn]:
                distance[movedRow][movedColumn] = cost
                heapq.heappush(heap, [cost, movedRow, movedColumn])

    return distance


print(dijkstra()[n-1][n-1])
