import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

def dijkstra(start):
    heap = []
    distance = [INF] * (n + 1)
    distance_path = [[] for i in range(n + 1)]

    heapq.heappush(heap, [0, start, [start]])
    distance[start] = 0
    while heap:
        dist, now, path = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                next_path = path + [i[0]]
                distance_path[i[0]] = next_path
                heapq.heappush(heap, [cost, i[0], next_path])

    return distance, distance_path

t = int(input())
for _ in range(t):
    n, d, c = map(int, input().split())
    graph = [[] for i in range(n + 1)]
    for i in range(d):
        a, b, s = map(int, input().split())
        graph[b].append([a, s])

    distance, distance_path = dijkstra(c)

    res_distance = 0
    res_computer_cnt = 0
    for i in distance:
        if res_distance < i and i != INF:
            res_distance = i
    for i in distance_path:
        if c in i:
            res_computer_cnt += 1
    print(res_computer_cnt + 1, res_distance)