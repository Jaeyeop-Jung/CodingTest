import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

m, n = map(int, input().split())
inp = []
for i in range(n):
    inp.append(input())
graph = [[] for i in range(n * m + 1)]
for i in range(1, n * m + 1):
    if i - m > 0:  # 위
        graph[i].append([i - m, int(inp[(i - 1 - m) // m][(i - 1) % m])])
    if i + m < n * m + 1:  # 아래
        graph[i].append([i + m, int(inp[(i - 1 + m) // m][(i - 1) % m])])
    if i % m != 0:  # 오른쪽
        graph[i].append([i + 1, int(inp[i // m][i % m])])
    if (i - 1) % m != 0:  # 왼쪽
        graph[i].append([i - 1, int(inp[(i - 1) // m][(i - 1) % m - 1])])

distance = [INF] * (n * m + 1)

def dijkstra(start):
    heap = []

    heapq.heappush(heap, [0, start])
    distance[start] = 0
    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, [cost, i[0]])

dijkstra(1)

print(distance[len(distance) - 1])