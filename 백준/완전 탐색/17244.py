import math
from collections import deque
from itertools import permutations

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

m, n = map(int, input().split())

arr = []
targets = []
for r in range(n):
    temp = list(input())
    for i in range(m):
        if temp[i] == 'S':
            sR, sC = r, i
        elif temp[i] == 'X':
            targets.append((r, i))
        elif temp[i] == 'E':
            eR, eC = r, i
    arr.append(temp)
targets.append((eR, eC))

def bfs(sR, sC):
    q = deque()
    q.append((sR, sC, 0))
    visited = [[-1] * m for _ in range(n)]
    visited[sR][sC] = 0
    while q:
        r, c, cost, = q.popleft()
        for i in range(4):
            movedR, movedC = r + dR[i], c + dC[i]
            if not 0 <= movedR < n or not 0 <= movedC < m:
                continue
            if visited[movedR][movedC] != -1 or arr[movedR][movedC] == '#':
                continue
            q.append((movedR, movedC, cost + 1))
            visited[movedR][movedC] = cost + 1
    return [visited[r][c] for r, c in targets]

dist = [bfs(r, c) for r, c in targets]
start = bfs(sR, sC)
res = math.inf
for per in permutations([i for i in range(len(targets))], len(targets)):
    if per[-1] != len(targets) - 1:
        continue

    temp = start[per[0]]
    cur = per[0]
    for next in per:
        temp += dist[cur][next]
        cur = next
    res = min(res, temp)
print(res)