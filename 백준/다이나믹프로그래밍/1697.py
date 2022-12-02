# TODO 틀림

import math
import sys

input = sys.stdin.readline

n, k, = map(int, input().split())

if k < n:
    print(abs(k - n))
else:
    dp = [math.inf] * 100001
    dp[n] = 0
    for i in range(n - 1, -1, -1):
        dp[i] = dp[i + 1] + 1

    for i in range(n + 1, k + 1):
        if i % 2 == 0:
            dp[i] = min(dp[i - 1] + 1, dp[i // 2] + 1)
        else:
            dp[i] = min(dp[i -1] + 1, dp[(i - 1) // 2] + 2, dp[(i + 1) // 2] + 2)

    print(dp[k])
