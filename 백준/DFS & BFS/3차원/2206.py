import math
from collections import deque

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

n, m = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(n)]


visited = [[[math.inf, math.inf] for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1
q = deque()
q.append([0, 0, 2, False])
while q:
    r, c, cost, broken, = q.popleft()
    for i in range(4):
        movedR, movedC = r + dR[i], c + dC[i]
        if not 0 <= movedR < n or not 0 <= movedC < m:
            continue

        if arr[movedR][movedC] == 1 and not broken and cost < visited[movedR][movedC][1]:
            visited[movedR][movedC][1] = cost
            q.append([movedR, movedC, cost + 1, True])
        elif arr[movedR][movedC] == 0 and broken and cost < visited[movedR][movedC][1]:
            visited[movedR][movedC][1] = cost
            q.append([movedR, movedC, cost + 1, broken])
        elif arr[movedR][movedC] == 0 and not broken and cost < visited[movedR][movedC][0]:
            visited[movedR][movedC][0] = cost
            q.append([movedR, movedC, cost + 1, broken])

res = min(visited[-1][-1])
print(res if res != math.inf else -1)