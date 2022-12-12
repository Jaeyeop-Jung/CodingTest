import sys
from collections import deque

dRow = [0, 1, 0, -1]
dColumn = [1, 0, -1, 0]

m, n = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(input()))

visited = [[False] * m for _ in range(n)]
result = {'W': 0, 'B': 0}
for r in range(n):
    for c in range(m):
        if not visited[r][c]:
            flag = arr[r][c]
            q = deque()
            q.append([r, c])
            visited[r][c] = True
            temp = 1
            rr = []
            while q:
                curR, curC, = q.popleft()
                visited[curR][curC] = True
                for i in range(4):
                    movedR, movedC = curR + dRow[i], curC + dColumn[i]
                    if not 0 <= movedR < n or not 0 <= movedC < m:
                        continue
                    if visited[movedR][movedC]:
                        continue
                    if arr[movedR][movedC] != flag:
                        continue
                    q.append([movedR, movedC])
                    visited[movedR][movedC] = True
                    temp += 1
            result[flag] += temp ** 2

print(result['W'])
print(result['B'])