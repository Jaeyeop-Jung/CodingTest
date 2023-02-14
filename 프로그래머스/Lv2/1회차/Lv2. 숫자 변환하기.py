import math


def solution(x, y, n):
    dp = [math.inf] * 1000001
    dp[x] = 0
    for i in range(x, y + 1):
        if dp[i] != math.inf:
            if i * 2 < 1000001:
                dp[i * 2] = min(dp[i * 2], dp[i] + 1)
            if i * 3 < 1000001:
                dp[i * 3] = min(dp[i * 3], dp[i] + 1)
            if i + n < 1000001:
                dp[i + n] = min(dp[i + n], dp[i] + 1)

    return dp[y] if dp[y] != math.inf else -1

print(solution(10, 40, 5))
print(solution(10, 40, 30))
print(solution(2, 5, 4))