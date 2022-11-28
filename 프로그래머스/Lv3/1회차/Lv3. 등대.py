# TODO 틀림

from collections import deque

def solution(n, lighthouse):
    graph = {i: [i, []] for i in range(1, n + 1)}
    for u, v in lighthouse:
        if u < v:
            graph[v][0] = u
            graph[u][1].append(v)
        else:
            graph[u][0] = v
            graph[v][1].append(u)
    q = deque()
    for key in graph:
        if len(graph[key][1]) == 0:
            q.append(key)

    light = set()
    result = 0
    while q:
        leaf = q.popleft()
        parent = graph[leaf][0]
        if leaf in light:
            continue
        result += 1
        for parent_leaf in graph[parent][1]:
            light.add(parent_leaf)
        light.add(parent)
        q.append(parent)

    return result

# print(solution(8, [[1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [5, 7], [5, 8]]))
# print(solution(10, [[4, 1], [5, 1], [5, 6], [7, 6], [1, 2], [1, 3], [6, 8], [2, 9], [9, 10]]))
print(solution(16, [[1,4], [1,5], [1,2], [1,3], [5,6], [6,7], [6,8], [8,11], [8,12], [12,13], [12,14], [2,9], [9,10],[10,15],[10,16]]))



