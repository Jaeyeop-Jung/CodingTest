import heapq
import math

dR = [[1, -1], [0, 0], [0, 1, 0, -1]]
dC = [[0, 0], [1, -1], [1, 0, -1, 0]]

n, m = map(int, input().split())
sR, sC, eR, eC = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[[math.inf, math.inf, math.inf] for _ in range(m)] for _ in range(n)]

h = []
dp[sR - 1][sC - 1][0] = 0
heapq.heappush(h, [0, sR - 1, sC - 1, 0])
while h:
    cost, curR, curC, turn = heapq.heappop(h)
    for i in range(len(dR[turn])):
        movedR, movedC = curR + dR[turn][i], curC + dC[turn][i]
        if not 0 <= movedR < n or not 0 <= movedC < m:
            continue
        if arr[movedR][movedC] == -1 or dp[movedR][movedC][(turn + 1) % 3] <= cost + arr[movedR][movedC]:
            continue
        heapq.heappush(h, [cost + arr[movedR][movedC], movedR, movedC, (turn + 1) % 3])
        dp[movedR][movedC][(turn + 1) % 3] = cost + arr[movedR][movedC]

result = min(dp[eR - 1][eC - 1])
print(result if result != math.inf else -1)