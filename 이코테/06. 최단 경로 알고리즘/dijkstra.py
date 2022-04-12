
INF = 1000000000

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    visited[start] = True
    distance[start] = 0
    for i in graph[start]:
        distance[i[0]] = i[1]

    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            if distance[j[0]] > distance[now] + j[1]:
                distance[j[0]] = distance[now] + j[1]

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print(f'{i} = infinity')
    else:
        print(f'{i} = {distance[i]}')

# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2