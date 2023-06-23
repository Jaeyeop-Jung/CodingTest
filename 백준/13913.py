# TODO 틀림 잘 생각해봐 아깝다

import math
from collections import deque

n, k = map(int, input().split())

q = deque()
q.append([n, 0])
visited = [math.inf] * 100_001
visited[n] = -1
while q:
    cur, cnt = q.popleft()

    if cur == k:
        print(cnt)
        path = []
        while visited[cur] != -1:
            path.append(cur)
            cur = visited[cur]
        path.append(n)
        print(*reversed(path))

    if 0 <= cur - 1 and visited[cur - 1] == math.inf:
        q.append([cur - 1, cnt + 1])
        visited[cur - 1] = cur
    if cur + 1 <= 100_000 and visited[cur + 1] == math.inf:
        q.append([cur + 1, cnt + 1])
        visited[cur + 1] = cur
    if cur * 2 <= 100_000 and visited[cur * 2] == math.inf:
        q.append([cur * 2, cnt + 1])
        visited[cur * 2] = cur

