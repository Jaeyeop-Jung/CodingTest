import sys

input = sys.stdin.readline

n, m, = map(int, input().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    before, after = map(int, input().split())
    graph[before][after] = 1
    graph[after][before] = -1

for mid in range(1, n + 1):
    for start in range(1, n + 1):
        for end in range(1, n + 1):
            if (graph[start][mid] < 0 and graph[mid][end] < 0) or (graph[start][mid] > 0 and graph[mid][end] > 0):
                graph[start][end] = graph[start][mid] + graph[mid][end]

k = int(input())
for _ in range(k):
    before, after = map(int, input().split())
    if graph[before][after] == 0:
        print(0)
    elif graph[before][after] < 0:
        print(1)
    else:
        print(-1)

