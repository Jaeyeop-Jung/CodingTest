from collections import deque

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

n, m = map(int, input().split())
arr = []
q = deque()
for r in range(n):
    temp = list(input())
    for c in range(m):
        if temp[c] == 'S':
            q.appendleft((r, c, 0, 'S'))
        elif temp[c] == 'D':
            eR, eC = r, c
        elif temp[c] == '*':
            q.append((r, c, 0, '*'))
    arr.append(temp)

while q:
    r, c, cost, t, = q.popleft()
    if arr[r][c] != t:
        continue
    for i in range(4):
        movedR, movedC = r + dR[i], c + dC[i]
        if not 0 <= movedR < n or not 0 <= movedC < m:
            continue
        if arr[movedR][movedC] == 'X':
            continue

        # 고슴도치
        if t == 'S':
            if arr[movedR][movedC] == 'D':
                print(cost + 1)
                exit()
            if arr[movedR][movedC] == '.':
                arr[movedR][movedC] = t
                q.append((movedR, movedC, cost + 1, t))

        # 물
        elif t == '*':
            if arr[movedR][movedC] == '.' or arr[movedR][movedC] == 'S':
                arr[movedR][movedC] = t
                q.append((movedR, movedC, cost + 1, t))

print('KAKTUS')