# TODO 틀림 예외를 잘 생각해봐 거의 맞았다

import math
import sys

input = sys.stdin.readline

c, n, = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x: x[1])
dp = [math.inf] * 1201
dp[0] = 0
for i in range(n):
    cost, people = arr[i]
    for j in range(people, 1201):
        dp[j] = min(dp[j], dp[j - people] + cost)

print(min(dp[c:]))
