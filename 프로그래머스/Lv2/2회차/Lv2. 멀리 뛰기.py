
def solution(n):
    if n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = (dp[i - 2] + dp[i - 1]) % 1234567
    return dp[n]

print(solution(4))
print(solution(3))
print(solution(2))
print(solution(2000))