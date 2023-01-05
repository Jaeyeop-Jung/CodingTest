# TODO 틀림 할 수 있다

from collections import deque

dRow = [0, 1, 0, -1]
dColumn = [1, 0, -1, 0]

miroR, miroC, = map(int, input().split())
board = []
start = []
fire = []
for r in range(miroR):
    temp = input()
    tempAdd = []
    for c in range(len(temp)):
        if temp[c] == '#':
            tempAdd.append(-1)
            continue
        elif temp[c] == 'J':
            start = [r, c]
        elif temp[c] == 'F':
            fire.append([r, c])
        tempAdd.append(-2)
    board.append(tempAdd)

# 지훈이 도망
q = deque()
for fR, fC in fire:
    q.append([fR, fC, 0, 'F'])
    board[fR][fC] = 0
q.append([start[0], start[1], 0, 'J'])
visited = [[False] * miroC for _ in range(miroR)]
while q:
    r, c, cnt, t = q.popleft()
    if t == 'J':
        for i in range(4):
            movedR, movedC = r + dRow[i], c + dColumn[i]
            if not 0 <= movedR < miroR or not 0 <= movedC < miroC:
                print(cnt + 1)
                exit()
            if board[movedR][movedC] == -1 or board[movedR][movedC] != -2:
                continue
            if visited[movedR][movedC]:
                continue
            q.append([movedR, movedC, cnt + 1, 'J'])
            visited[movedR][movedC] = True
    else:
        for i in range(4):
            movedR, movedC = r + dRow[i], c + dColumn[i]
            if not 0 <= movedR < miroR or not 0 <= movedC < miroC:
                continue
            if board[movedR][movedC] == -1:
                continue
            if board[movedR][movedC] == -2:
                board[movedR][movedC] = cnt + 1
                q.append([movedR, movedC, cnt + 1, 'F'])

print('IMPOSSIBLE')