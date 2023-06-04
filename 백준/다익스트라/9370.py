import heapq
import math
import sys

input = sys.stdin.readline

def dijkstra(start):
    heap = [[0, start]]
    distance = [int(1e9)] * (n + 1)
    distance[start] = 0
    while heap:
        dist, cur, = heapq.heappop(heap)
        if distance[cur] < dist:
            continue
        for next, cost in graph[cur]:
            totalCost = cost + dist
            if totalCost < distance[next]:
                distance[next] = totalCost
                heapq.heappush(heap, [totalCost, next])
    return distance

# def dijkstra(start, g, h):
#     heap = [[0, start, [start]]]
#     distance = [math.inf] * (n + 1)
#     distance[start] = 0
#     routes = [[] for _ in range(n + 1)]
#     while heap:
#         dist, cur, route = heapq.heappop(heap)
#         if distance[cur] <= dist:
#             continue
#         for next, cost in graph[cur]:
#             totalCost = cost + dist
#             if totalCost <= distance[next]:
#                 distance[next] = totalCost
#                 newRoute = route[:] + [next]
#                 heapq.heappush(heap, [totalCost, next, newRoute])
#                 routes[next] = newRoute
#     return routes


test_case = int(input())
for _ in range(test_case):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, d, = map(int, input().split())
        graph[a].append([b, d])
        graph[b].append([a, d])
        if (a == g and b == h) or (a == h and b == g):
            betweenGAndH = d

    targets = [int(input()) for _ in range(t)]
    targets.sort()
    res = []
    for target in targets:
        distance = dijkstra(s)
        distanceFromG = dijkstra(g)
        distanceFromH = dijkstra(h)

        origin = distance[target]
        gToH = distance[g] + betweenGAndH + distanceFromH[target]
        hToG = distance[h] + betweenGAndH + distanceFromG[target]

        if gToH <= origin or hToG <= origin:
            res.append(target)

        # routes = dijkstra(s, g, h)
        # if g in routes[target] and h in routes[target]:
        #     res.append(target)

    print(*res)


