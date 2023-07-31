import math
import sys
from collections import deque

input = sys.stdin.readline

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

n, m, t, = map(int, input().split())
arr = []
for r in range(n):
    temp = list(map(int, input().split()))
    for c in range(m):
        if temp[c] == 2:
            gR, gC = r, c
    arr.append(temp)

q = deque()
visited = [[math.inf] * m for _ in range(n)]
visited[0][0] = 0
q.append([0, 0, 0])
while q:
    r, c, cost, = q.popleft()
    for i in range(4):
        movedR, movedC = r + dR[i], c + dC[i]
        if not 0 <= movedR < n or not 0 <= movedC < m:
            continue
        if arr[movedR][movedC] == 1 or visited[movedR][movedC] != math.inf:
            continue
        visited[movedR][movedC] = cost + 1
        q.append([movedR, movedC, cost + 1])

noGram = visited[-1][-1]
withGram = visited[gR][gC] + (n - 1 - gR) + (m - 1 - gC)

res = min(noGram, withGram)
print(res if res <= t else 'Fail')