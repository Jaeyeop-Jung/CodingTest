# TODO 틀림

import math
import sys

input = sys.stdin.readline

n, m, = map(int, input().split())
arr = list(map(int, input().split()))

arr = {i: True for i in arr}
dp = [[math.inf] * 300 for _ in range(n + 10)]
dp[1][0] = 0
for day in range(1, n):
    for coupon in range(n * 2 - 3):
        if dp[day][coupon] == math.inf:
            continue

        if day in arr:
            dp[day + 1][coupon] = min(dp[day + 1][coupon], dp[day][coupon])
        else:
            if 3 <= coupon:
                dp[day + 1][coupon - 3] = min(dp[day + 1][coupon - 3], dp[day][coupon])
            dp[day + 1][coupon] = min(dp[day + 1][coupon], dp[day][coupon] + 10000)
            dp[day + 3][coupon + 1] = min(dp[day + 3][coupon + 1], dp[day][coupon] + 25000)
            dp[day + 5][coupon + 2] = min(dp[day + 5][coupon + 2], dp[day][coupon] + 37000)

res = math.inf
for i in range(n, len(dp)):
    for j in range(len(dp[i])):
        res = min(res, dp[i][j])
print(res if res != math.inf else 0)