import math
from collections import deque
import sys

input = sys.stdin.readline

dRow = [0, 1, 0, -1]
dColumn = [1, 0, -1, 0]

q = deque()
m, n = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(len(arr[i])):
        if arr[i][j] == 1:
            q.append([i, j, 0])

visited = [[math.inf] * m for i in range(n)]
while q:
    r, c, cost, = q.popleft()
    visited[r][c] = min(visited[r][c], cost)
    for i in range(len(dRow)):
        movedR = r + dRow[i]
        movedC = c + dColumn[i]
        if not 0 <= movedR < n or not 0 <= movedC < m:
            continue
        if arr[movedR][movedC] == -1 or visited[movedR][movedC] != math.inf:
            continue
        if visited[movedR][movedC] < cost + 1:
            continue
        q.append([movedR, movedC, cost + 1])
        visited[movedR][movedC] = min(visited[movedR][movedC], cost + 1)

result = 0
for r in range(len(visited)):
    for c in range(len(visited[r])):
        if arr[r][c] == -1:
            continue
        if visited[r][c] == math.inf:
            print(-1)
            exit()
        result = max(result, visited[r][c])
print(result)