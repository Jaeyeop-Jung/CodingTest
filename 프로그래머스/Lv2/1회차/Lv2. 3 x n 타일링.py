# TODO 틀림

def solution(n):
    if n % 2 == 1:
        return 0
    if n == 2:
        return 3
    dp = [0] * (n + 1)
    dp[2] = 3
    for i in range(4, n + 1, 2):
        dp[i] = i * 2 + 3
    return dp[n]

print(solution(6))