import math
import sys
from collections import deque

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [list(map(int, list(input().strip()))) for _ in range(n)]

visited = [[[math.inf] * (k + 1) for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 0
q = deque()
q.append([0, 0, 0, 0])
while q:
    r, c, cost, broken, = q.popleft()
    if r == n - 1 and c == m - 1:
        print(cost + 1)
        exit()
    for i in range(4):
        movedR, movedC = r + dR[i], c + dC[i]
        if not 0 <= movedR < n or not 0 <= movedC < m:
            continue

        if arr[movedR][movedC] == 0 and cost + 1 < visited[movedR][movedC][broken]:
            q.append([movedR, movedC, cost + 1, broken])
            visited[movedR][movedC][broken] = cost + 1

        if arr[movedR][movedC] == 1 and broken < k and cost + 1 < visited[movedR][movedC][broken + 1]:
            q.append([movedR, movedC, cost + 1, broken + 1])
            visited[movedR][movedC][broken + 1] = cost + 1

print(-1)

