# TODO 틀림 이건 외워야됨

import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
now = [0, 0, 0]
for _ in range(n - 1):
    u, v, w, = map(int, input().split())
    graph[u].append([v, w])
    graph[v].append([u, w])
    if now[2] < w:
        now = [u, v, w]

for i in range(1, n + 1):
    if graph[i]:
        graph[i].sort(key=lambda x: -x[1])

# def dijkstra(start):
#     h = []
#     heapq.heappush(h, [0, start])
#     distance = [0] + [math.inf] * n
#     distance[start] = 0
#     while h:
#         dist, now, = heapq.heappop(h)
#         if distance[now] < dist:
#             continue
#         for v, w in graph[now]:
#             totalCost = dist + w
#             if totalCost < distance[v]:
#                 distance[v] = totalCost
#                 heapq.heappush(h, [totalCost, v])
#     return distance
#
#
# result = 0
# for i in range(1, n + 1):
#     result = max(result, max(dijkstra(i)))

visited = [False] * (n + 1)
visited[now[0]] = True
visited[now[1]] = True
result = now[2]
now = now[0]
while True:
    temp = now
    for v, w in graph[now]:
        if not visited[v]:
            result += w
            now = v
            visited[v] = True
            break
    if temp == now:
        break

print(result)