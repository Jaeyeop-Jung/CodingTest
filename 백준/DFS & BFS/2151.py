# TODO 틀림 잘 생각해봐라

import math
from collections import deque

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

n = int(input())
board = [list(input()) for _ in range(n)]
wall = []
for r in range(n):
    for c in range(n):
        if board[r][c] == '#':
            wall.append((r, c))

def inRange(r, c):
    if not 0 <= r < n or not 0 <= c < n:
        return True
    return False

visited = [[[math.inf] * 4 for _ in range(n)] for _ in range(n)]
startR, startC, = wall[0]
visited[startR][startC] = [0] * 4
q = deque()
for i in range(4):
    q.append((startR, startC, 0, i))

while q:
    r, c, cnt, d, = q.popleft()

    movedR, movedC = r + dR[d], c + dC[d]
    if not inRange(movedR, movedC):
        if visited[movedR][movedC][d] == math.inf:
            if board[movedR][movedC] == '.' or board[movedR][movedC] == '#' or board[movedR][movedC] == '!':
                q.append((movedR, movedC, cnt, d))
                visited[movedR][movedC][d] = cnt
            if board[movedR][movedC] == '!':
                visited[movedR][movedC][(d + 1) % 4] = cnt + 1
                q.append((movedR, movedC, cnt + 1, (d + 1) % 4))
                visited[movedR][movedC][(d - 1) % 4] = cnt + 1
                q.append((movedR, movedC, cnt + 1, (d - 1) % 4))

        else:
            if cnt < visited[movedR][movedC][d] and (board[movedR][movedC] == '.' or board[movedR][movedC] == '#' or board[movedR][movedC] == '!'):
                q.append((movedR, movedC, cnt, d))
                visited[movedR][movedC][d] = cnt
            if cnt + 1 < visited[movedR][movedC][(d + 1) % 4] and board[movedR][movedC] == '!':
                visited[movedR][movedC][(d + 1) % 4] = cnt + 1
                q.append((movedR, movedC, cnt + 1, (d + 1) % 4))
            if cnt + 1 < visited[movedR][movedC][(d - 1) % 4] and board[movedR][movedC] == '!':
                visited[movedR][movedC][(d - 1) % 4] = cnt + 1
                q.append((movedR, movedC, cnt + 1, (d - 1) % 4))

tR, tC = wall[-1]
print(min(visited[tR][tC]))