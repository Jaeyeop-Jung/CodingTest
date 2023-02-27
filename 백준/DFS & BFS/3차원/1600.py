# TODO 틀림 dfs/bfs heap 3차원 배열 문제

import sys
from collections import deque

input = sys.stdin.readline

dR = [0, 1, 0, -1, 1, 2, 2, 1, -1, -2, -2, -1]
dC = [1, 0, -1, 0, 2, 1, -1, -2, -2, -1, 1, 2]

k = int(input())
c, r, = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]

q = deque()
visited = [[[0] * 31 for _ in range(c)] for _ in range(r)]
visited[0][0][0] = 0
q.append([0, 0, 0, 0])
while q:
    curR, curC, cnt, curK = q.popleft()
    if curR == r - 1 and curC == c - 1:
        print(cnt)
        exit()
    for i in range(4):
        movedR, movedC = curR + dR[i], curC + dC[i]
        if not 0 <= movedR < r or not 0 <= movedC < c:
            continue
        if arr[movedR][movedC] == 1 or visited[movedR][movedC][curK] != 0:
            continue
        visited[movedR][movedC][curK] = cnt + 1
        q.append([movedR, movedC, cnt + 1, curK])
    if curK < k:
        for i in range(4, len(dR)):
            movedR, movedC = curR + dR[i], curC + dC[i]
            if not 0 <= movedR < r or not 0 <= movedC < c:
                continue
            if arr[movedR][movedC] == 1 or visited[movedR][movedC][curK + 1] != 0:
                continue
            visited[movedR][movedC][curK + 1] = cnt + 1
            q.append([movedR, movedC, cnt + 1, curK + 1])
print(-1)