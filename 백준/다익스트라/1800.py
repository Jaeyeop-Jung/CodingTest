# TODO 틀림 아이디어를 잘 고민해봐

# import math
# import sys
#
# input = sys.stdin.readline
#
# n, p, k = map(int, input().split())
#
# graph = [[] for _ in range(n + 1)]
# for i in range(p):
#     u, v, w = map(int, input().split())
#     graph[u].append([v, w])
#     graph[v].append([u, w])
#
# def dfs(graph, visited, cur, route):
#     global result
#     if visited[n]:
#         sortedRoute = list(sorted(route))
#         result = min(result, sortedRoute[-k - 1])
#     for next, value in graph[cur]:
#         if not visited[next]:
#             visited[next] = True
#             route.append(value)
#             dfs(graph, visited, next, route)
#             visited[next] = False
#             route.pop()
#
#
# result = math.inf
# visited = [False] * (n + 1)
# visited[1] = True
# dfs(graph, visited, 1, [])
#
# print(result)
import math
import sys
import heapq
input = sys.stdin.readline

n, p, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(p):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
    graph[v].append([u, w])

def dijkstra(boundary):
    heap = []
    useCoupon = [math.inf] * (n + 1)
    useCoupon[1] = 0
    heapq.heappush(heap, [0, 1])
    while heap:
        dist, cur, = heapq.heappop(heap)
        if useCoupon[cur] < dist:
            continue
        for next, nextCost in graph[cur]:
            if boundary < nextCost:
                if dist + 1 < useCoupon[next]:
                    useCoupon[next] = dist + 1
                    heapq.heappush(heap, [dist + 1, next])
            else:
                if dist < useCoupon[next]:
                    useCoupon[next] = dist
                    heapq.heappush(heap, [dist, next])
    return useCoupon[n]

start = 0
end = 1000000
while start <= end:
    mid = (start + end) // 2
    temp = dijkstra(mid)
    if temp <= k:
        end = mid - 1
    else:
        start = mid + 1

print(start)