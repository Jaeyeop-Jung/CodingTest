# TODO 틀림 아깝다 풀 수 있을 텐데

from collections import deque

dR = [-1, 0, 1]
dC = [1, 1, 1]

r, c, = map(int, input().split())
board = [list(input()) for _ in range(r)]

result = 0
q = deque([[i, 0] for i in range(r)])
visited = [[False] * c for _ in range(r)]
while q:
    curR, curC, = q.popleft()
    if curC == c - 1:
        result += 1
        continue
    for i in range(len(dR)):
        movedR, movedC = curR + dR[i], curC + dC[i]
        if not 0 <= movedR < r or not 0 <= movedC < c:
            continue
        if board[movedR][movedC] == 'x' or visited[movedR][movedC]:
            continue
        q.append([movedR, movedC])
        visited[movedR][movedC] = True

print(result)
