import heapq
import math

graph = []
distance = []

def dijkstra(start):
    h = []
    heapq.heappush(h, [0, start])
    distance[start] = 0
    while h:
        cost, idx = heapq.heappop(h)
        if distance[idx] < cost:
            continue
        for dist, nextIdx in graph[idx]:
            newCost = cost + dist
            if newCost < distance[nextIdx]:
                distance[nextIdx] = newCost
                heapq.heappush(h, [newCost, nextIdx])

def solution(N, road, K):
    global graph
    global distance
    graph = [[] for _ in range(N + 1)]
    for i, j, k in road:
        graph[i].append([k, j])
        graph[j].append([k, i])
    distance = [math.inf] * (N + 1)
    dijkstra(1)
    return len([i for i in distance if i <= K])

print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
# print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))