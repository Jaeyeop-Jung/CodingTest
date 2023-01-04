# TODO 틀림 할 수 있다

import math
import sys
input = sys.stdin.readline
from collections import deque

n, m, = map(int, input().split())
board = [-1] * 101
for i in range(n):
    u, v = map(int, input().split())
    board[u] = v
for i in range(m):
    u, v = map(int, input().split())
    board[u] = v

q = deque()
q.append([1, 0])
dp = [math.inf] * 101
dp[1] = 0
while q:
    cur, cnt, = q.popleft()
    for i in range(1, 7):
        next = cur + i
        if 1 <= next <= 100 and dp[next] == math.inf:
            if board[next] != -1:
                next = board[next]
            dp[next] = cnt + 1
            q.append([next, cnt + 1])
            if next == 100:
                print(dp[100])
                exit()

print(dp[100])