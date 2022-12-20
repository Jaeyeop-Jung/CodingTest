# TODO 틀림

import math
from collections import deque
import sys

input = sys.stdin.readline

dRow = [0, 1, 0, -1]
dColumn = [1, 0, -1, 0]

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, list(input().strip()))))

q = deque()
visited = [[[math.inf] * 2 for _ in range(m)] for _ in range(n)]
q.append([0, 0, 1, 0])
visited[0][0][0] = 1
visited[0][0][1] = 1
while q:
    r, c, cnt, breakWallCnt, = q.popleft()
    if r == n - 1 and c == m - 1:
        break
    for i in range(4):
        movedR = r + dRow[i]
        movedC = c + dColumn[i]
        if not 0 <= movedR < n or not 0 <= movedC < m:
            continue
        if visited[movedR][movedC][breakWallCnt] != math.inf:
            continue
        if breakWallCnt == 0:
            if arr[movedR][movedC] == 1:
                visited[movedR][movedC][breakWallCnt + 1] = cnt + 1
                q.append([movedR, movedC, cnt + 1, breakWallCnt + 1])
            else:
                visited[movedR][movedC][breakWallCnt] = cnt + 1
                q.append([movedR, movedC, cnt + 1, breakWallCnt])
        elif breakWallCnt == 1:
            if arr[movedR][movedC] == 1:
                continue
            visited[movedR][movedC][breakWallCnt] = cnt + 1
            q.append([movedR, movedC, cnt + 1, breakWallCnt])

result = min(visited[-1][-1][0], visited[-1][-1][1])
if result == math.inf:
    print(-1)
else:
    print(result)
