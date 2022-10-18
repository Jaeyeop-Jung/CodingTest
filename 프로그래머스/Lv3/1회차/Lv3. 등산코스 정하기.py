# TODO 틀림

import heapq
import math

def solution(n, paths, gates, summits):
    result = [-1, math.inf]
    graph = [[] for i in range(n)]
    gates = [i - 1 for i in gates]
    summits = [i - 1 for i in summits]
    summits.sort()

    for start, end, cost in paths:
        graph[start - 1].append([cost, end - 1])
        if end -1 not in summits:
            graph[end - 1].append([cost, start - 1])
    dic = {}
    for i in range(n):
        dic[i] = False
    for i in gates:
        dic[i] = 1
    for i in summits:
        dic[i] = 2

    distance = [math.inf] * n
    for gate in gates:
        h = []
        heapq.heappush(h, [0, gate])
        distance[gate] = 0

        while h:
            dist, now = heapq.heappop(h)
            if distance[now] < dist:
                continue
            for cost, next in graph[now]:
                nextDist = max(dist, cost)
                if nextDist < distance[next] and dic[next] != 1:
                    distance[next] = nextDist
                    if dic[next] != 2:
                        heapq.heappush(h, [nextDist, next])

        for i in summits:
            if distance[i] < result[1]:
                result = [i + 1, distance[i]]

    return result


# print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
# print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))
# print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))
# print(solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]))
print(solution(5, [[1, 5, 1], [5, 3, 1], [3, 4, 1], [4, 2, 1]], [1, 2], [3, 4]))