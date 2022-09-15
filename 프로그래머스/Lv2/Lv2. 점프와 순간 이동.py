# TODO 틀림 근데 문제가 이상한듯? 7일 때 +1 점프하고 / 2를 반복하면 2로도 해결 되는데

import math
def solution(n):
    if n == 1:
        return 1

    dp = [math.inf] * (n + 1)
    dp[1] = 1
    for i in range(n + 1):
        if i % 2 == 0:
            dp[i] = min(dp[i // 2], dp[i - 1] + 1, dp[i])
        else:
            dp[i] = min(dp[i - 1] + 1, dp[i], dp[(i - 1) // 2] + 1, dp[(i + 1) // 2] + 1)
    return dp[n]


# print(solution(5))
# print(solution(6))
print(solution(5000))