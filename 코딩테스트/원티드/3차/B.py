import sys
input = sys.stdin.readline
from collections import deque

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

n, m, = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

result = 0
visited = [[False] * m for _ in range(n)]
for r in range(n):
    for c in range(m):
        if visited[r][c] or arr[r][c] == 1:
            continue
        q = deque()
        q.append([r, c])
        while q:
            curR, curC, = q.popleft()
            for i in range(4):
                movedR, movedC = (curR + dR[i]) % n, (curC + dC[i]) % m
                if visited[movedR][movedC] or arr[movedR][movedC] == 1:
                    continue
                visited[movedR][movedC] = True
                q.append([movedR, movedC])
        result += 1

print(result)