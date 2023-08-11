# TODO 틀림

import math
import random
import sys
from collections import defaultdict
from collections import deque
import heapq

input = sys.stdin.readline

n, m, k = map(int, input().split())
jewel = set()
for _ in range(k):
    jewel.add(int(input()))
graph = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# n, m, k = 100, 1000, 14
# jewel = set(i for i in range(14))
# graph = defaultdict(set)
# for _ in range(1000):
#     while True:
#         start = random.randrange(1, 101)
#         end = random.randrange(1, 101)
#         if end in graph[start]:
#             continue
#         graph[start].add((end, random.randrange(1, 15)))
#         break

h = []
dist = [-math.inf] * (n + 1)
dist[1] = math.inf
heapq.heappush(h, (math.inf, 1))
while h:
    pathCost, cur = heapq.heappop(h)
    if pathCost < dist[cur]:
        continue
    for next, nextCost in graph[cur]:
        totalCost = min(nextCost, pathCost)
        if dist[next] < totalCost:
            heapq.heappush(h, (totalCost, next))
            dist[next] = totalCost

visited = defaultdict(set)
q = deque()
q.append((1, 0))
visited[1].add(0)
resCnt = 0

while q:
    # resCnt = max(resCnt, len(q))
    cur, curJewel,  = q.popleft()
    if cur == 1 and bin(curJewel).count('1') == k - 1:
        break
    for next, limit in graph[cur]:
        if curJewel in visited[next]:
            continue
        count = bin(curJewel).count('1')
        if limit < count:
            continue

        if next in jewel and next != 1:
            nextJewel = curJewel | (1 << (next - 1))
        else:
            nextJewel = curJewel

        nextPickCnt = bin(nextJewel).count('1')
        if nextPickCnt <= dist[next]:
            visited[next].add(nextJewel)
            q.append((next, nextJewel))

        if count <= dist[next]:
            visited[next].add(curJewel)
            q.append((next, curJewel))

res = max(visited[1])
print(bin(res).count('1') + 1 if 1 in jewel else bin(res).count('1'))
# print(resCnt)





# import math
# import random
# import sys
# from collections import defaultdict
# from collections import deque
# import heapq
#
# input = sys.stdin.readline
#
# n, m, k = map(int, input().split())
# jewel = set()
# for _ in range(k):
#     jewel.add(int(input()))
# graph = defaultdict(list)
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))
#     graph[b].append((a, c))
#
# # n, m, k = 100, 1000, 14
# # jewel = set(i for i in range(1, 15))
# # graph = defaultdict(set)
# # for _ in range(1000):
# #     while True:
# #         start = random.randrange(1, 101)
# #         end = random.randrange(1, 101)
# #         if end in graph[start]:
# #             continue
# #         graph[start].add((end, random.randrange(1, 15)))
# #         break
#
# def dijkstra(start):
#     h = []
#     dist = [-math.inf] * (n + 1)
#     dist[start] = math.inf
#     heapq.heappush(h, (math.inf, start))
#     while h:
#         pathCost, cur = heapq.heappop(h)
#         if pathCost < dist[cur]:
#             continue
#         for next, nextCost in graph[cur]:
#             totalCost = min(nextCost, pathCost)
#             if dist[next] < totalCost:
#                 heapq.heappush(h, (totalCost, next))
#                 dist[next] = totalCost
#     return dist
#
# dist = [[]]
# for i in range(1, n + 1):
#     dist.append(dijkstra(i))
#
# visited = defaultdict(set)
# q = deque()
# q.append((1, 0))
# visited[1].add(0)
# resCnt = 0
#
# while q:
#     cur, curJewel,  = q.popleft()
#     for next in jewel:
#         # 이미 있는 보석
#         if curJewel & (1 << (next - 1)):
#             continue
#         # 그 곳까지 못감
#         count = bin(curJewel).count('1')
#         if dist[cur][next] < count:
#             continue
#
#         if count + 1 <= dist[next][1]:
#             nextJewel = curJewel | (1 << (next - 1))
#             q.append((next, nextJewel))
#             visited[next].add(nextJewel)
#
#         # 집
#         if count + 1 <= dist[next][1]:
#             visited[1].add(nextJewel)
#
#
# res = max(visited[1])
# # print(bin(res).count('1') + 1 if 1 in jewel else bin(res).count('1'))
# print(bin(res).count('1'))