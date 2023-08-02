from collections import deque

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

q = deque()
visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
for r in range(n):
    for c in range(m):
        if arr[r][c] == '*':
            q.append([r, c, 0, 0])
            visited[r][c][0] = True

for r in range(n):
    for c in range(m):
        if arr[r][c] == 'S':
            q.append([r, c, 0, 1])
            visited[r][c][1] = True

while q:
    r, c, cost, cur = q.popleft()
    for i in range(4):
        movedR, movedC = r + dR[i], c + dC[i]
        if not 0 <= movedR < n or not 0 <= movedC < m:
            continue
        if visited[movedR][movedC][cur] or arr[movedR][movedC] == 'X' or (cur == 0 and arr[movedR][movedC] == 'D'):
            continue

        if cur == 0:
            visited[movedR][movedC][0] = True
            q.append([movedR, movedC, cost + 1, cur])
        else:
            if arr[movedR][movedC] == 'D':
                print(cost + 1)
                exit()
            if visited[movedR][movedC][0]:
                continue
            visited[movedR][movedC][1] = True
            q.append([movedR, movedC, cost + 1, 1])

print('KAKTUS')