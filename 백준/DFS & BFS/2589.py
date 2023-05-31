# TODO 틀림

import math
from collections import deque

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

res = 0
visited = [[False] * len(arr[i]) for i in range(n)]
for r in range(n):
    for c in range(m):
        if arr[r][c] == 'W' or visited[r][c]:
            continue
        q = deque()
        visited[r][c] = True
        q.append([r, c, 0])

        end = []
        while q:
            curR, curC, cnt, = q.popleft()
            flag = False
            for i in range(4):
                movedR, movedC = curR + dR[i], curC + dC[i]
                if not 0 <= movedR < n or not 0 <= movedC < m:
                    continue
                if visited[movedR][movedC] or arr[movedR][movedC] == 'W':
                    continue
                q.append([movedR, movedC, cnt + 1])
                visited[movedR][movedC] = True
                flag = True

            if not flag:
                end.append([curR, curC])

        q = deque()
        tempVisited = [[math.inf] * len(arr[i]) for i in range(n)]
        start = end[0]
        q.append([start[0], start[1], 0])
        tempVisited[start[0]][start[1]] = 0
        while q:
            curR, curC, cnt, = q.popleft()
            for i in range(4):
                movedR, movedC = curR + dR[i], curC + dC[i]
                if not 0 <= movedR < n or not 0 <= movedC < m:
                    continue
                if tempVisited[movedR][movedC] != math.inf or arr[movedR][movedC] == 'W':
                    continue
                q.append([movedR, movedC, cnt + 1])
                tempVisited[movedR][movedC] = cnt + 1
        for i in range(1, len(end)):
            tempR, tempC = end[i]
            res = max(res, tempVisited[tempR][tempC])

print(res)
            