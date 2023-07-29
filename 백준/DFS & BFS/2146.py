import math
import sys
from collections import deque

input = sys.stdin.readline

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

groups = []
visited = [[False] * n for _ in range(n)]
cnt = 0
for r in range(n):
    for c in range(n):
        if arr[r][c] == 1 and not visited[r][c]:
            groups.append([])
            q = deque()
            q.append([r, c])
            visited[r][c] = True
            groups[cnt].append([r, c])
            while q:
                curR, curC, = q.popleft()
                for i in range(4):
                    movedR, movedC = curR + dR[i], curC + dC[i]
                    if not 0 <= movedR < n or not 0 <= movedC < n:
                        continue
                    if visited[movedR][movedC] or arr[movedR][movedC] != 1:
                        continue
                    visited[movedR][movedC] = True
                    q.append([movedR, movedC])
                    groups[cnt].append([movedR, movedC])
            cnt += 1

res = math.inf
for group in groups:
    q = deque()
    visited = [[math.inf] * n for _ in range(n)]
    for r, c in group:
        q.append([r, c, 0])
        visited[r][c] = 0
    flag = False
    while q:
        r, c, cnt, = q.popleft()
        for i in range(4):
            movedR, movedC = r + dR[i], c + dC[i]
            if not 0 <= movedR < n or not 0 <= movedC < n:
                continue
            if visited[movedR][movedC] != math.inf:
                continue
            if arr[movedR][movedC] == 1:
                res = min(res, cnt + 1)
                flag = True
                break
            visited[movedR][movedC] = cnt + 1
            q.append([movedR, movedC, cnt + 1])
        if flag:
            break

print(res - 1)