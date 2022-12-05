# TODO 틀림 풀 수 있어 잘 생각해봐




false = 0
true = 1
wait = 2

def solution(n, path, order):
    graph = [[] for _ in range(n)]
    for u, v in path:
        graph[u].append(v)
        graph[v].append(u)
    before = {u: v for u, v in order}
    after = {u: v for v, u in order}
    visited = [false] * n

    q = deque()
    q.append(0)
    visited[0] = true
    while q:
        cur = q.popleft()
        if cur == before.get(after.get(cur)):
            visited[cur] = wait
        else:
            for next in graph[cur]:
                if visited[next] == false:
                    q.append(next)
                    visited[next] = true
                    if next in before:
                        if visited[before[next]] == wait:
                            visited[before[next]] = true
                            q.append(before[next])
                        before[next] = 0

    if visited.count(true) == n:
        return True
    return False

print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]))
print(solution(9, [[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]], [[4,1],[5,2]]))
print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[4,1],[8,7],[6,5]]))
