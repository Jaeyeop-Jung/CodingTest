# TODO 틀림 잘 생각해봐 맞을 수 있다

import math

n = int(input())
dp = [math.inf] * (n + 1)
dp[0] = 0
for i in range(1, n + 1):
    for j in range(1, int(i ** 0.5) + 1):
        dp[i] = min(dp[i], dp[i - j ** 2] + 1)

print(dp[-1])
