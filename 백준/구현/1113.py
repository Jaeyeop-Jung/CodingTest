# TODO 틀림 거의 다 맞았는데 다시 잘 생각하고 풀어봐

import sys
from collections import deque

input = sys.stdin.readline

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

n, m, = map(int, input().split())
arr = [list(map(int, list(input().strip()))) for _ in range(n)]

res = 0
visited = [[False] * m for _ in range(n)]
for r in range(1, n - 1):
    for c in range(1, m - 1):
        tempRes = 0
        if visited[r][c]:
            continue
        for height in range(arr[r][c], 10):
            tempVisited = [[False] * m for _ in range(n)]
            flag = False
            tempVisited[r][c] = True
            q = deque()
            q.append((r, c))
            temp = height - arr[r][c]
            while q:
                curR, curC, = q.popleft()
                for d in range(4):
                    movedR, movedC = curR + dR[d], curC + dC[d]
                    if not 0 <= movedR < n or not 0 <= movedC < m:
                        flag = True
                        break
                    if height <= arr[movedR][movedC] or tempVisited[movedR][movedC]:
                        tempVisited[movedR][movedC] = True
                        continue
                    q.append((movedR, movedC))
                    temp += height - arr[movedR][movedC]
                    tempVisited[movedR][movedC] = True
                if flag:
                    break
            if flag:
                break
            tempRes = max(tempRes, temp)
            resVisited = tempVisited
        if tempRes == 0:
            continue
        for vR in range(n):
            for vC in range(m):
                visited[vR][vC] |= resVisited[vR][vC]
        res += tempRes

print(res)