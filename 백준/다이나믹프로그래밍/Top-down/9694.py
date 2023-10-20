import heapq
import math

t = int(input())
for tc in range(1, t + 1):
    m, n = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w, = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    distance = [math.inf] * n
    distance[0] = 0
    h = [[0, 0, [0]]]
    path = []
    while h:
        dist, cur, curPath = heapq.heappop(h)
        if distance[cur] < dist:
            continue
        for next, cost in graph[cur]:
            totalCost = dist + cost
            if totalCost < distance[next]:
                heapq.heappush(h, [totalCost, next, curPath + [next]])
                distance[next] = totalCost
                if next == n - 1:
                    path = curPath + [next]

    if distance[-1] != math.inf:
        print(f'Case #{tc}: ', end='')
        print(*path)
    else:
        print(f'Case #{tc}: -1')