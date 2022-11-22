# TODO 틀림 문제를 잘 읽어라

import heapq
import math

REST = 0
GATE = 1
SUMMIT = 2

def dijkstra(n, node, graph, start):
    distance = [[math.inf, 0] for _ in range(n)]
    h = []
    heapq.heappush(h, [0, start, 0])
    while h:
        cost, cur, maxCost = heapq.heappop(h)
        if distance[cur][0] < cost:
            continue
        for nextCur, nextCost in graph[cur]:
            totalCost = cost + nextCost
            if node[nextCur] == GATE:
                continue
            if totalCost < distance[nextCur][0]:
                maxCost = max(maxCost, nextCost)
                distance[nextCur] = [totalCost, maxCost]
                heapq.heappush(h, [totalCost, nextCur, maxCost])
    return distance


def solution(n, paths, gates, summits):
    node = [REST] * n
    for gate in gates:
        node[gate-1] = GATE
    for summit in summits:
        node[summit-1] = SUMMIT
    graph = [[] * n for i in range(n)]
    for i, j, w in paths:
        graph[i-1].append([j-1, w])
        graph[j-1].append([i-1, w])

    result = [math.inf, math.inf, math.inf]
    for i in range(len(node)):
        if node[i] == GATE:
            distance = dijkstra(n, node, graph, i)
            for j in range(len(distance)):
                if node[j] == SUMMIT:
                    if distance[j][0] < result[0]:
                        result = [distance[j][0], j+1, distance[j][1]]

    return result



print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))
print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))
print(solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]))

