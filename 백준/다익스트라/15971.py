#
# import sys
#
# input = sys.stdin.readline
# import heapq
# from collections import defaultdict
# import math
# import sys
# from collections import defaultdict
# import heapq
#
# def sol1(n, graph, a, b):
#     # n, a, b, = map(int, input().split())
#     # graph = defaultdict(list)
#     # for _ in range(n - 1):
#     #     u, v, w = map(int, input().split())
#     #     graph[u - 1].append((v - 1, w))
#     #     graph[v - 1].append((u - 1, w))
#     h = []
#     distance = [math.inf] * n
#     distance[a] = 0
#     resMaxPath = 0
#     h = [[0, a, 0]]
#     while h:
#         curCost, cur, maxPath, = heapq.heappop(h)
#         if distance[cur] < cur:
#             continue
#         if cur == b:
#             resMaxPath = max(resMaxPath, maxPath)
#         for next, cost in graph[cur]:
#             totalCost = curCost + cost
#             if totalCost < distance[next]:
#                 heapq.heappush(h, [totalCost, next, max(maxPath, cost)])
#                 distance[next] = totalCost
#     return distance[b] - resMaxPath
#
#
# def sol2(n, graph, start, end):
#
#     # n, start, end = map(int, input().split())
#     INF = int(1e9)
#     # graph = defaultdict(list)
#     distance = [INF] * n
#     max_distance = [0] * n
#
#     # for _ in range(n - 1):
#     #     a, b, c = map(int, input().split())
#     #     graph[a].append((b, c))
#     #     graph[b].append((a, c))
#
#     def dijkstra(start):
#         q = []
#         # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
#         heapq.heappush(q, (0, start, 0))
#         distance[start] = 0
#
#         while q:
#             # print(q)
#             # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
#             dist, now, max_ = heapq.heappop(q)
#
#             # 현재 노드와 연결된 다른 인접한 노드들을 확인
#             for i in graph[now]:
#                 cost = dist + i[1]
#                 # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
#                 if cost < distance[i[0]]:
#                     distance[i[0]] = cost
#                     max_distance[i[0]] = max(max_, i[1])
#                     heapq.heappush(q, (cost, i[0], max(max_, i[1])))
#
#
#     dijkstra(start)
#
#     return distance[end] - max_distance[end]
#
# import random
# while True:
#     n = random.randrange(5, 6)
#     a, b = random.randrange(0, n), random.randrange(0, n)
#     graph = defaultdict(list)
#     cnt = 0
#     while cnt < n - 1:
#         start = random.randrange(0, n)
#         end = random.randrange(0, n)
#         cost = random.randrange(1, 10)
#         if start != end and end not in [i[0] for i in graph[start]]:
#             graph[start].append((end, cost))
#             graph[end].append((start, cost))
#             cnt += 1
#     res1 = sol1(n, graph, a, b)
#     res2 = sol2(n, graph, a, b)
#     if res1 != res2:
#         print(graph)
#         print(a, b)
#         print(res1, res2)
#         exit()


import math
import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

n, a, b, = map(int, input().split())
graph = defaultdict(list)
a -= 1
b -= 1

if a == b:
    print(0)
    exit()

for _ in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u - 1].append((v - 1, w))
    graph[v - 1].append((u - 1, w))

h = []
distance = [math.inf] * n
distance[a] = 0
resMaxPath = 0
h = [[0, a, 0]]
while h:
    curCost, cur, maxPath, = heapq.heappop(h)
    if distance[cur] < curCost:
        continue
    if cur == b:
        resMaxPath = max(resMaxPath, maxPath)
    for next, cost in graph[cur]:
        totalCost = curCost + cost
        if totalCost < distance[next]:
            heapq.heappush(h, [totalCost, next, max(maxPath, cost)])
            distance[next] = totalCost

print(distance[b] - resMaxPath)