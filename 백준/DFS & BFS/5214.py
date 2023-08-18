# TODO 틀림

import math
import sys
from collections import deque
from collections import defaultdict

input = sys.stdin.readline

n, k, m, = map(int, input().split())
graph = defaultdict(set)

for _ in range(m):
    temp = list(map(int, input().split()))
    for start in temp:
        for end in temp:
            if start == end:
                continue
            graph[start - 1].add(end - 1)
            graph[end - 1].add(start - 1)

visited = [math.inf] * n
q = deque()
visited[0] = 0
q.append((0, 0))
while q:
    cur, cost, = q.popleft()
    if cur == n - 1:
        break
    for next in graph[cur]:
        if visited[next] == math.inf:
            visited[next] = cost + 1
            q.append((next, cost + 1))

print(visited[-1] + 1 if visited[-1] != math.inf else -1)