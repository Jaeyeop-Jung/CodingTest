# TODO 틀림

def solution(n, money):
    dp = [1] + [0] * n

    for i in money:
        for j in range(i, n + 1):
            dp[j] += dp[j - i]

    return dp[n]

print(solution(5, [1, 2, 5]))