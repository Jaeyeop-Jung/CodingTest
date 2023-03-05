from collections import deque

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
cnt = 1
for r in range(n):
    for c in range(m):
        if not visited[r][c] and arr[r][c] == 1:
            q = deque()
            q.append([r, c])
            visited[r][c] = True
            arr[r][c] = cnt
            while q:
                curR, curC, = q.popleft()
                for i in range(4):
                    movedR, movedC = curR + dR[i], curC + dC[i]
                    if not 0 <= movedR < n or not 0 <= movedC < m:
                        continue
                    if visited[movedR][movedC] or arr[movedR][movedC] == 0:
                        continue
                    visited[movedR][movedC] = True
                    arr[movedR][movedC] = cnt
                    q.append([movedR, movedC])
            cnt += 1

graph = []
for r in range(n):
    for c in range(m):
        if arr[r][c] != 0:
            for i in range(4):
                nextR, nextC = r, c
                dist = 0
                while True:
                    nextR, nextC = nextR + dR[i], nextC + dC[i]
                    dist += 1
                    if not 0 <= nextR < n or not 0 <= nextC < m:
                        break
                    if arr[nextR][nextC] == arr[r][c]:
                        break
                    if arr[nextR][nextC] != 0:
                        if 2 <= dist - 1:
                            graph.append([arr[r][c], arr[nextR][nextC], dist - 1])
                        break

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

graph.sort(key=lambda x: x[2])
parent = [i for i in range(cnt)]
result = 0
for u, v, cost in graph:
    if find_parent(parent, u) != find_parent(parent, v):
        union_parent(parent, u, v)
        result += cost

for i in range(len(parent)):
    find_parent(parent, i)
if len(set(parent)) == 2:
    print(result)
else:
    print(-1)