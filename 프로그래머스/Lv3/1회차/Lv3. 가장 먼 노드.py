from collections import deque

def solution(n, edge):
    result = [0] * n
    graph = [[] * n for i in range(n)]
    for start, end in edge:
        graph[start - 1].append(end - 1)
        graph[end - 1].append(start - 1)
    visited = [False] * n

    q = deque()
    q.append([0, 0])
    while q:
        idx, cnt = q.popleft()
        visited[idx] = True
        result[idx] = cnt
        for i in graph[idx]:
            if visited[i] is False:
                q.append([i, cnt + 1])
                visited[i] = True
    return result.count(max(result))


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))