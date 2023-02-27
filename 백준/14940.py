from collections import deque

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
for r in range(n):
    for c in range(m):
        if arr[r][c] == 2:
            tR, tC = r, c
            break

q = deque()
q.append([tR, tC, 0])
result = [[-1] * m for _ in range(n)]
result[tR][tC] = 0
for r in range(n):
    for c in range(m):
        if arr[r][c] == 0:
            result[r][c] = 0
while q:
    curR, curC, cnt, = q.popleft()
    for i in range(4):
        movedR, movedC = curR + dR[i], curC + dC[i]
        if not 0 <= movedR < n or not 0 <= movedC < m:
            continue
        if result[movedR][movedC] != -1 or arr[movedR][movedC] == 0 or arr[movedR][movedC] == 2:
            continue
        result[movedR][movedC] = cnt + 1
        q.append([movedR, movedC, cnt + 1])

for i in range(n):
    print(*result[i])

