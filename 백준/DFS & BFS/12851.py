# TODO 틀림 잘 생각해봐 맞출 수 있어

import math
from collections import deque

n, k = map(int, input().split())

if k < n:
    print(abs(k - n))
    print(1)
    exit()

board = [[math.inf, 0] for _ in range(100001)]

q = deque()
q.append([n, 0])
board[n][0] = 0
board[n][1] = 1
while q:
    cur, cnt = q.popleft()
    move = cur - 1
    if 0 <= move <= 100000:
        if cnt + 1 == board[move][0]:
            board[move][1] += board[cur][1]
        elif cnt + 1 < board[move][0]:
            board[move][0] = cnt + 1
            board[move][1] = board[cur][1]
            q.append([move, cnt + 1])

    move = cur + 1
    if 0 <= move <= 100000:
        if cnt + 1 == board[move][0]:
            board[move][1] += board[cur][1]
        elif cnt + 1 < board[move][0]:
            board[move][0] = cnt + 1
            board[move][1] = board[cur][1]
            q.append([move, cnt + 1])

    move = cur * 2
    if 0 <= move <= 100000:
        if cnt + 1 == board[move][0]:
            board[move][1] += board[cur][1]
        elif cnt + 1 < board[move][0]:
            board[move][0] = cnt + 1
            board[move][1] = board[cur][1]
            q.append([move, cnt + 1])

print(board[k][0])
print(board[k][1])
