# TODO 틀림 

def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n] % 1234567

print(solution(4))
print(solution(3))
print(solution(2))