from collections import deque
import math

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

def bfs(maps, r, c):
    n = len(maps)
    m = len(maps[0])
    visited = [[math.inf] * m for _ in range(n)]
    visited[r][c] = 0
    q = deque([[r, c, 0]])
    while q:
        curR, curC, cost, = q.popleft()
        for i in range(4):
            movedR, movedC = curR + dR[i], curC + dC[i]
            if not 0 <= movedR < n or not 0 <= movedC < m:
                continue
            if maps[movedR][movedC] == 'X' or visited[movedR][movedC] != math.inf:
                continue
            visited[movedR][movedC] = cost + 1
            q.append([movedR, movedC, cost + 1])
    return visited


def solution(maps):
    for r in range(len(maps)):
        for c in range(len(maps[0])):
            if maps[r][c] == 'S':
                startR, startC = r, c
            elif maps[r][c] == 'L':
                lR, lC = r, c
            elif maps[r][c] == 'E':
                exitR, exitC = r, c
    result = bfs(maps, startR, startC)[lR][lC] + bfs(maps, lR, lC)[exitR][exitC]
    return result if result != math.inf else -1

print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]	))