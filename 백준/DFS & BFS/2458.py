from collections import deque
from collections import defaultdict
import sys

input = sys.stdin.readline

n, m, = map(int, input().split())
parent = defaultdict(list)
child = defaultdict(list)
for _ in range(m):
    c, p = map(int, input().split())
    parent[c - 1].append(p - 1)
    child[p - 1].append(c - 1)

def check(graph, start):
    q = deque()
    for next in graph[start]:
        q.append(next)
        visited[next] = True
    while q:
        cur = q.popleft()
        for next in graph[cur]:
            if not visited[next]:
                q.append(next)
                visited[next] = True

res = 0
for i in range(n):
    visited = [False] * n
    visited[i] = True
    check(parent, i)
    check(child, i)
    if all(visited):
        res += 1

print(res)