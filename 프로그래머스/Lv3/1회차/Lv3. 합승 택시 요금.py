import heapq
import math

def dijkstra(n, graph, start):
    distance = [math.inf] * n
    h = []
    heapq.heappush(h, [0, start])
    distance[start] = 0

    while h:
        cost, des = heapq.heappop(h)
        if distance[des] < cost:
            continue
        for nextCost, nextDes in graph[des]:
            totalCost = cost + nextCost
            if totalCost < distance[nextDes]:
                distance[nextDes] = totalCost
                heapq.heappush(h, [totalCost, nextDes])
    return distance

def solution(n, s, a, b, fares):
    joinMin = math.inf
    a, b, s = a - 1, b - 1, s - 1
    graph = [[] * n for i in range(n)]
    for start, end, cost in fares:
        graph[start - 1].append([cost, end - 1])
        graph[end - 1].append([cost, start - 1])
    for i in range(n):
        tempResult = 0
        tempResult += dijkstra(n, graph, s)[i]
        temp = dijkstra(n, graph, i)
        tempResult += temp[a]
        tempResult += temp[b]
        joinMin = min(joinMin, tempResult)

    notJoin = dijkstra(n, graph, s)
    return min(joinMin, notJoin[a] + notJoin[b])

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))
