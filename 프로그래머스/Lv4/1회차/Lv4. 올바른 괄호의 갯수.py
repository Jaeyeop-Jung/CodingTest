# TODO 틀림 아이디어는 조금 비슷했는데... 더 생각해봐

def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 5
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 5
    for i in range(4, n + 1):
        dp[i] = sum(dp) - i
    return dp[-1]

# print(solution(2))
print(solution(14))