import sys
from collections import deque

input = sys.stdin.readline

n, m, = map(int, input().split())
graph = {i: [[], []] for i in range(1, n + 1)}
for _ in range(m):
    win, lose = map(int, input().split())
    graph[win][1].append(lose)
    graph[lose][0].append(win)

res = 0
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    visited[i] = True

    # 무거운 애들
    q = deque([i])
    child = 0
    while q:
        pop = q.popleft()
        for winner in graph[pop][1]:
            if not visited[winner]:
                q.append(winner)
                child += 1
                visited[winner] = True

    # 가벼운 애들
    q = deque([i])
    parent = 0
    while q:
        pop = q.popleft()
        for winner in graph[pop][0]:
            if not visited[winner]:
                q.append(winner)
                parent += 1
                visited[winner] = True

    mid = round(n / 2)
    if mid <= parent or mid <= child:
        res += 1

print(res)