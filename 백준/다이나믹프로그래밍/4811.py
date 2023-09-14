# TODO 틀림

import sys
from collections import deque

input = sys.stdin.readline

while True:
    n = int(input())
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    dp[n][0] = 1
    q = deque()
    q.append((n, 0))
    while q:
        w, h, = q.popleft()

        if 0 < w:
            q.append((w - 1, h + 1))
            dp[w - 1][h + 1] += dp[w][h]
        if 0 < h:
            q.append((w, h - 1))
            dp[w][h - 1] += dp[w][h]

    print(dp[0][0])