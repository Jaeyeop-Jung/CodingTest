# TODO 틀린건 아니지만 union-find를 할 때는 마지막에 최종 parent 리스트에 부모가 들어간게 아닐 수도 있으니 한번 더 find_parent한다

# import math
# from collections import deque
#
# def bfs(graph, visited, node):
#     q = deque()
#     cnt = 1
#     q.append(node)
#
#     while q:
#         nextNode = q.popleft()
#         visited[nextNode] = True
#         for i in graph[nextNode]:
#             if not visited[i]:
#                 cnt += 1
#                 q.append(i)
#                 visited[i] = True
#     return cnt
#
#
# def solution(n, wires):
#     graph = [[] * n for i in range(n)]
#     for start, end in wires:
#         graph[start - 1].append(end - 1)
#         graph[end - 1].append(start - 1)
#
#     result = math.inf
#     for i in range(len(graph)):
#         for j in range(len(graph[i])):
#             tempGraph = [graph[n][:] for n in range(len(graph))]
#             removed = tempGraph[i][j]
#             tempGraph[i].remove(removed)
#             tempGraph[removed].remove(i)
#
#             # print('start = ', i, ' end = ', removed)
#             numberOf1 = bfs(tempGraph, [False] * n, i)
#             # print('start cnt = ', numberOf1)
#             numberOf2 = bfs(tempGraph, [False] * n, graph[i][j])
#             # print('end cnt = ', numberOf2)
#             # print('abs = ', abs(numberOf1 - numberOf2))
#             result = min(result, abs(numberOf1 - numberOf2))
#             # print('')
#
#     return result

import math

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def solution(n, wires):
    result = math.inf
    graph = [[] * n for i in range(n)]
    for start, end in wires:
        graph[start - 1].append(end - 1)
        graph[end - 1].append(start - 1)

    for i in range(len(graph)):
        for j in range(len(graph[i])):
            parent = [k for k in range(n)]
            tempGraph = [graph[r][:] for r in range(len(graph))]
            removed = graph[i][j]
            tempGraph[i].remove(removed)
            tempGraph[removed].remove(i)

            for i2 in range(len(tempGraph)):
                for j2 in range(len(tempGraph[i2])):
                    union_parent(parent, i2, tempGraph[i2][j2])

            for p in range(len(parent)):
                parent[p] = find_parent(parent, p)

            num = list(set(parent))
            result = min(result, abs(parent.count(num[0]) - parent.count(num[1])))
    return result

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(3, [[1,2], [2,3]]))