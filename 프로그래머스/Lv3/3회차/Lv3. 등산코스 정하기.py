import heapq
import math


def dijkstra(n, graph, gates, summits):
    distance = [math.inf] * (n + 1)
    h = []
    for gate in gates:
        distance[gate] = 0
        h.append((0, gate))
    while h:
        dist, cur, = heapq.heappop(h)

        if distance[cur] < dist:
            continue

        for next, cost in graph[cur]:
            totalCost = max(dist, cost)
            if totalCost < distance[next]:
                distance[next] = totalCost
                if next not in summits and next not in gates:
                    heapq.heappush(h, (totalCost, next))
    return distance

def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n + 1)]
    for u, v, w in paths:
        graph[u].append((v, w))
        graph[v].append((u, w))

    tempGates = {}
    for gate in gates:
        tempGates[gate] = 1

    tempSummits = {}
    for summit in summits:
        tempSummits[summit] = 1

    res = []
    distance = dijkstra(n, graph, tempGates, tempSummits)
    for summit in summits:
        res.append((summit, distance[summit]))

    res.sort(key=lambda x: (x[1], x[0]))
    return res[0]


print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))
print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))
print(solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]))