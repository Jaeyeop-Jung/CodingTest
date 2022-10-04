
def dfs(graph, visited, n):
    visited[n] = True
    for i in graph[n]:
        if visited[i] is False:
            dfs(graph, visited, i)

def solution(n, computers):
    result = 0
    graph = []
    for i in range(len(computers)):
        graph.append([])
        for j in range(len(computers[i])):
            if i != j and computers[i][j] == 1:
                graph[i].append(j)
    visited = [False] * len(graph)
    for i in range(len(graph)):
        if visited[i] is False:
            dfs(graph, visited, i)
            result += 1
    return result

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))