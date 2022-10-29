
def dfs(graph, visited, computer):
    visited[computer] = True
    for i in graph[computer]:
        if not visited[i]:
            dfs(graph, visited, i)

def solution(n, computers):
    result = 0
    graph = [[] for i in range(n)]
    for i in range(len(computers)):
        for j in range(len(computers)):
            if i != j and computers[i][j] == 1:
                graph[i].append(j)

    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            result += 1
            dfs(graph, visited, i)
    return result

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))