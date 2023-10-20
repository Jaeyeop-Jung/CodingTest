import sys
from collections import deque

input = sys.stdin.readline

n, m, target, = map(int, input().split())
child = [[] for _ in range(n + 1)]
parent = [[] for _ in range(n + 1)]
register = set()
for _ in range(m):
    a, b, = map(int, input().split())
    child[a].append(b)
    parent[b].append(a)
    register.add(a)
    register.add(b)

noJoin = n - len(register)
if target not in register:
    print(1, n)
    exit()

# 위에서 몇 등인지
q = deque()
q.append(target)
visited = [False] * (n + 1)
visited[target] = True
while q:
    cur = q.popleft()
    for next in parent[cur]:
        if not visited[next]:
            visited[next] = True
            q.append(next)
print(visited.count(True), end=' ')

# 아래에서 몇 등인지
q = deque()
q.append(target)
visited = [False] * (n + 1)
while q:
    cur = q.popleft()
    for next in child[cur]:
        if not visited[next]:
            visited[next] = True
            q.append(next)
print(n - visited.count(True))