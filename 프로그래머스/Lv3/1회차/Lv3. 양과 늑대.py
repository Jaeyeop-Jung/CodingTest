
result = 0

def dfs(info, graph, neighbor, visited, sheep, wolf, n, cnt):
    if info[n] == 0:
        sheep += 1
    else:
        wolf += 1
    visited[n] = cnt

    for i in graph[n]:
        if i not in neighbor:
            neighbor.append(i)

    for i in neighbor:
        if visited[i] == 0:
            if (info[i] == 1 and wolf + 1 < sheep) or info[i] == 0:
                dfs(info, graph, neighbor, visited, sheep, wolf, i, cnt + 1)
                visited[i] = 0
                for j in graph[i]:
                    neighbor.remove(j)

    global result
    result = max(result, sheep)

def solution(info, edges):
    graph = [[] for i in range(len(info))]
    for start, end in edges:
        graph[start].append(end)
        # graph[end].append(start)

    visited = [0] * len(info)
    dfs(info, graph, [], visited, 0, 0, 0, 1)


    return result

print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
print(solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))