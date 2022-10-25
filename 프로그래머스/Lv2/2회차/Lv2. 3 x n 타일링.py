# TODO 틀림

def solution(n):
    if n % 2 == 1:
        return 0

    dp = [0] * (n + 1)
    dp[2] = 3
    dp[4] = 11
    for i in range(6, n + 1):
        if i % 2 == 0:
            dp[i] = (dp[i - 2] * 4 - dp[i - 4]) % 1000000007
    return dp[n]

print(solution(5))