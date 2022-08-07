from collections import deque

def bfs(graph, v, visited):
    queue = deque()
    queue.append(v)

    while queue:
        pop = queue.popleft()
        print(pop, end=' ')
        visited[pop] = True
        for i in graph[pop]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)
