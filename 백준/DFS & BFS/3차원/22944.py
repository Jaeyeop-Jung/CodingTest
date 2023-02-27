# TODO 틀림 잘 생각해봐 창의적으

from collections import deque

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

n, h, d, = map(int, input().split())
arr = [list(input()) for _ in range(n)]

for r in range(n):
    for c in range(n):
        if arr[r][c] == 'S':
            startR, startC = r, c
            break

result = [[[0, 0]] * n for _ in range(n)]
q = deque()
q.append([startR, startC, h, 0, 0])
arr[startR][startC] = '.'
result[startR][startC] = [0, 0]
while q:
    curR, curC, h, u, cnt = q.popleft()
    for i in range(len(dR)):
        movedR, movedC = curR + dR[i], curC + dC[i]
        if not 0 <= movedR < n or not 0 <= movedC < n:
            continue

        # 3
        if arr[movedR][movedC] == 'U':
            u = d

        # 4, 5
        tempU = u
        tempH = h
        if 0 < u:
            tempU -= 1
        else:
            tempH -= 1

        if arr[movedR][movedC] == 'E':
            print(cnt + 1)
            exit()

        if tempH == 0:
            continue

        if result[movedR][movedC][0] < tempH and result[movedR][movedC][1] <= tempU:
            q.append([movedR, movedC, tempH, tempU, cnt + 1])
            result[movedR][movedC] = [tempH, tempU]

print(-1)