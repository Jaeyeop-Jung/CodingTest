import math


# def solution(n):
#     if n == 1:
#         return 1
#
#     dp = [math.inf] * (n + 1)
#     dp[1] = 1
#     for i in range(2, n + 1):
#         if i % 2 == 0:
#             dp[i] = dp[i // 2]
#         else:
#             dp[i] = dp[i // 2] + 1
#     return dp[n]

def solution(n):
    num = n
    result = 0
    while num != 0:
        if num % 2 == 0:
            num //= 2
        else:
            num -= 1
            result += 1
    return result
print(solution(10))