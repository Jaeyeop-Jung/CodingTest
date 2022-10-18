# TODO 틀림

import sys
sys.setrecursionlimit(300000)

result = 0

def dfs(graph, visited, a, now):
    visited[now] = True
    for i in graph[now]:
        if not visited[i]:
            a[now] += dfs(graph, visited, a, i)
    global result
    result += abs(a[now])
    return a[now]


def solution(a, edges):
    if sum(a) != 0:
        return -1

    graph = [[] for i in range(len(a))]
    for start, end in edges:
        graph[start].append(end)
        graph[end].append(start)

    visited = [False] * len(a)
    dfs(graph, visited, a, 0)


    return result

print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]]))
print(solution([0,1,0], [[0,1],[1,2]]))
