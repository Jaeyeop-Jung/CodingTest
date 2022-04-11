import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline


result = []
while True:

    n = int(input())
    if n == 0:
        break

    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))

    def dijkstra():
        heap = []
        distance = []
        for i in range(n):
            distance.append([INF] * n)
        dRow = [0, 0, 1, -1]
        dColumn = [1, -1, 0, 0]

        heapq.heappush(heap, [graph[0][0], 0, 0])
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

    result.append(dijkstra()[n-1][n-1])

for i in range(len(result)):
    print(f'Problem {i+1}: {result[i]}')