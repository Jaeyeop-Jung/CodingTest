import math
from collections import deque

def inRange(cur):
    if 1 <= cur <= f:
        return True
    return False

f, s, g, u, d, = map(int, input().split())
visited = [math.inf] * (f + 1)
visited[s] = 0
q = deque()
q.append([s + u, 1])
q.append([s - d, 1])
while q:
    cur, cost, = q.popleft()
    if inRange(cur):
        if inRange(cur + u) and visited[cur + u] == math.inf:
            q.append([cur + u, cost + 1])
            visited[cur + u] = cost + 1
        if inRange(cur - d) and visited[cur - d] == math.inf:
            q.append([cur - d, cost + 1])
            visited[cur - d] = cost + 1

print(visited[g] if visited[g] != math.inf else 'use the stairs')

