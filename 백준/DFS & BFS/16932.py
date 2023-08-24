import sys
from collections import deque

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

input = sys.stdin.readline

n, m, = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]
dic = {}
cnt = 1
for r in range(n):
    for c in range(m):
        if visited[r][c] == 0 and arr[r][c] == 1:
            visited[r][c] = cnt
            q = deque([[r, c]])
            temp = 1
            while q:
                curR, curC, = q.popleft()
                for i in range(4):
                    movedR, movedC = curR + dR[i], curC + dC[i]
                    if not 0 <= movedR < n or not 0 <= movedC < m:
                        continue
                    if visited[movedR][movedC] != 0 or arr[movedR][movedC] == 0:
                        continue
                    visited[movedR][movedC] = cnt
                    q.append([movedR, movedC])
                    temp += 1
            dic[cnt] = temp
            cnt += 1

res = 0
for r in range(n):
    for c in range(m):
        if arr[r][c] == 0:
            temp = 1
            involve = set()
            for i in range(4):
                movedR, movedC = r + dR[i], c + dC[i]
                if not 0 <= movedR < n or not 0 <= movedC < m:
                    continue
                if arr[movedR][movedC] == 1 and visited[movedR][movedC] not in involve:
                    temp += dic[visited[movedR][movedC]]
                    involve.add(visited[movedR][movedC])
            res = max(res, temp)

print(res)