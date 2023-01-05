# TODO 틀림 하지만 맞을 수 있다 다 함

import sys
input = sys.stdin.readline
from collections import deque

dRow = [0, 1, 0, -1]
dColumn = [1, 0, -1, 0]

snake = 1
apple = 2

n = int(input())
board = [[0] * n for _ in range(n)]
i = int(input())
for _ in range(i):
    r, c, = map(int, input().split())
    board[r-1][c-1] = apple
turn = {}
i = int(input())
for _ in range(i):
    time, direction = input().split()
    turn[int(time)] = direction

time = 0
d = 0
r, c = 0, 0
tail = deque()
board[r][c] = snake
while True:
    movedR, movedC = r + dRow[d], c + dColumn[d]
    if not 0 <= movedR < n or not 0 <= movedC < n:
        break
    if board[movedR][movedC] == snake:
        break
    tail.append([r, c])
    if board[movedR][movedC] == apple:
        time += 1
        if time in turn:
            if turn[time] == 'L':
                d -= 1
                if d < 0:
                    d = 3
            else:
                d += 1
                d %= 4
        r, c = movedR, movedC
        board[movedR][movedC] = snake
        continue
    board[movedR][movedC] = snake
    tailR, tailC = tail.popleft()
    board[tailR][tailC] = 0
    time += 1
    if time in turn:
        if turn[time] == 'L':
            d -= 1
            if d < 0:
                d = 3
        else:
            d += 1
            d %= 4
    r, c = movedR, movedC

print(time + 1)