import math
from collections import deque
import sys

input = sys.stdin.readline

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

n, m, k = map(int, input().split())
arr = [list(map(int, list(input().strip()))) for _ in range(n)]

visited = [[[math.inf] * (k + 1) for _ in range(m)] for _ in range(n)]
for i in range(k + 1):
    visited[0][0][i] = 1
q = deque()
q.append([0, 0, 2, 0])
while q:
    r, c, cost, broken, = q.popleft()
    for i in range(4):
        movedR, movedC = r + dR[i], c + dC[i]
        if movedR == n - 1 and movedC == m - 1:
            print(cost)
            exit()
        if not 0 <= movedR < n or not 0 <= movedC < m:
            continue

        if arr[movedR][movedC] == 0 and cost < visited[movedR][movedC][broken]:
            visited[movedR][movedC][broken] = cost
            q.append([movedR, movedC, cost + 1, broken])
        elif arr[movedR][movedC] == 1:
            if broken < k and cost < visited[movedR][movedC][broken + 1]:
                visited[movedR][movedC][broken + 1] = cost
                q.append([movedR, movedC, cost + 1, broken + 1])

res = min(visited[-1][-1])
print(res if res != math.inf else -1)
