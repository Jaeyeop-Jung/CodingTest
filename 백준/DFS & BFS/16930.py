# TODO 틀림 아이디어는 맞음 잘 구현해봐

import math
from collections import deque
import sys
input = sys.stdin.readline

dRow = [0, 1, 0, -1]
dColumn = [1, 0, -1, 0]

n, m, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(input().strip()))
sr, sc, er, ec = map(int, input().split())
sr -= 1; sc -= 1; er -= 1; ec -= 1

board = [[math.inf] * m for _ in range(n)]
q = deque()
q.append([sr, sc, 0])
board[sr][sc] = 0
while q:
    r, c, cnt = q.popleft()
    if r == er and c == ec:
        print(board[r][c])
        exit()
    for i in range(4):
        movedR, movedC = r, c
        for _ in range(k):
            movedR += dRow[i]
            movedC += dColumn[i]
            if not 0 <= movedR < n or not 0 <= movedC < m:
                break
            if arr[movedR][movedC] == '#':
                break
            if board[movedR][movedC] == cnt + 1:
                continue
            elif board[movedR][movedC] < cnt + 1:
                break
            board[movedR][movedC] = cnt + 1
            q.append([movedR, movedC, cnt + 1])

if board[er][ec] == math.inf:
    print(-1)
else:
    print(board[er][ec])