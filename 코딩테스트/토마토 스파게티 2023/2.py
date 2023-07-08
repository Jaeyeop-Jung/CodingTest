#
# res = 0
# cnt = 0
#
# def dfs(graph, visited, limit, cur, depth):
#     global cnt
#     global res
#     for next in graph[cur]:
#         if visited[next]:
#             continue
#         if 1 == depth + 1 <= limit:
#             visited[next] = True
#             res += 5
#             dfs(graph, visited, limit, next, depth + 1)
#         elif 2 <= depth + 1 <= limit:
#             visited[next] = True
#             cnt += 1
#             res += 10
#             dfs(graph, visited, limit, next, depth + 1)
#
# def solution(relationships, target, limit):
#     graph = [[] for _ in range(101)]
#     for i in range(len(relationships)):
#         a, b, = relationships[i]
#         graph[a].append(b)
#         graph[b].append(a)
#
#     visited = [False] * 101
#     visited[target] = True
#     dfs(graph, visited, limit, target, 0)
#     return res + cnt
#

from collections import deque

def solution(relationships, target, limit):
    graph = [[] for _ in range(101)]
    for i in range(len(relationships)):
        a, b, = relationships[i]
        graph[a].append(b)
        graph[b].append(a)

    q = deque()
    cnt = 0
    res = 0
    visited = [False] * 101
    q.append([target, 0])
    visited[target] = True
    while q:
        cur, depth, = q.popleft()
        if limit <= depth:
            continue

        for next in graph[cur]:
            if visited[next]:
                continue
            if depth + 1 == 1:
                res += 5
                visited[next] = True
                q.append([next, depth + 1])
            elif 2 <= depth + 1 <= limit:
                res += 10
                cnt += 1
                visited[next] = True
                q.append([next, depth + 1])
    return res + cnt


print(solution([[1, 2], [2, 3], [2, 6], [3, 4], [4, 5]], 2, 3))
print(solution([[1, 2], [2, 3], [2, 6], [3, 4], [4, 5]], 1, 2))
#
