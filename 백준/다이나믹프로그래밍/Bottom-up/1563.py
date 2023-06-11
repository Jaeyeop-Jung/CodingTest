# TODO 틀림 잘 생각해봐

from collections import deque

n = int(input())

dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]
q = deque()
q.append((0, 0, 0))
for i in range(n + 1):
    dp[i][0][0] += dp[i - 1][0][0]

