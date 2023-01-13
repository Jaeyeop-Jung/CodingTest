# TODO 틀림 https://summa-cum-laude.tistory.com/35

import sys
import heapq
input = sys.stdin.readline

dR = [0, 1, 0 ,-1]
dC = [1, 0, -1, 0]

n, m, = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]
dp[0][0] = 1
q = [[-arr[0][0], 0, 0]]
while q:
    h, r, c, = heapq.heappop(q)
    for i in range(4):
        movedR, movedC = r + dR[i], c + dC[i]
        if not 0 <= movedR < n or not 0 <= movedC < m:
            continue
        if arr[movedR][movedC] < arr[r][c]:
            if dp[movedR][movedC] == 0:
                heapq.heappush(q, [-arr[movedR][movedC], movedR, movedC])
            dp[movedR][movedC] += dp[r][c]

print(dp[-1][-1])
