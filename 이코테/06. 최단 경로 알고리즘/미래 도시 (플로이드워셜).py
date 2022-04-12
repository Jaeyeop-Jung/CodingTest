import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if i == j:
            graph[i][j] = 0
x, k = map(int, input().split())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            graph[i][k] = min(graph[i][k], graph[i][j] + graph[j][k])

distance = graph[1][k] + graph[k][x]
if distance >= INF:
    print(-1)
else:
    print(distance)