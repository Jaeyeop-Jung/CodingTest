
def dfs(graph, visited, node, cnt):
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            dfs(graph, visited, i, cnt + 1)
            visited[i] = False
    global result
    result = max(result, visited.count(True))

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    graph = [[] for i in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)

    result = 0
    for i in range(n):
        visited = [False] * n
        dfs(graph, visited, i, 1)

    print('#' + str(test_case) + ' ' + str(result))