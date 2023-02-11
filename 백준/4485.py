# TODO 틀림 잘 생각해라 풀 수 있음


import math
import sys
from collections import deque

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

input = sys.stdin.readline

t = 1
while True:
    n = int(input())
    if n == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(n)]
    dp = [[math.inf] * n for _ in range(n)]

    q = deque()
    q.append([0, 0])
    dp[0][0] = arr[0][0]
    while q:
        r, c = q.popleft()
        for i in range(len(dR)):
            movedR, movedC = r + dR[i], c + dC[i]
            if not 0 <= movedR < n or not 0 <= movedC < n:
                continue
            if dp[movedR][movedC] <= dp[r][c] + arr[movedR][movedC]:
                continue
            dp[movedR][movedC] = dp[r][c] + arr[movedR][movedC]
            q.append([movedR, movedC])

    print(f'Problem {t}: {dp[-1][-1]}')
    t += 1