import heapq

INF = 1000000000

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n + 1)
heap = []

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    heapq.heappush(heap, [0, start])
    distance[start] = 0
    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            # visited를 사용하지 않는 대신 만약 INF가 아니고 dist가 distance[now]보다 크다면,
            # 이미 다른 길을 거쳐서 방문했던 적이 있는(더 단거리 경로가 있는) 상황이기 때문에 넘긴다.
            continue
        for i in graph[now]:
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(heap, [cost, i[1]])


dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print(f'{i} = infinity')
    else:
        print(f'{i} = {distance[i]}')

# 6 11
# 1
# 1 2 2
# 1 5 3
# 1 1 4
# 2 3 3
# 2 2 4
# 3 3 2
# 3 5 6
# 4 3 3
# 4 1 5
# 5 1 3
# 5 2 6