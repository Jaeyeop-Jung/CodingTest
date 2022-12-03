# TODO 틀림 아이디어는 어느정도 갔는데 아깝다

# def solution(cookie):
#     dp = [[0] * len(cookie) for _ in range(len(cookie))]
#     for i in range(len(cookie)):
#         dp[i][i] = cookie[i]
#     for i in range(len(dp) - 1):
#         for j in range(i + 1, len(dp)):
#             dp[i][j] = sum(cookie[i:j + 1])
#
#     result = 0
#     for r in range(len(dp)):
#         for c in range(len(dp[r])):
#             if dp[r][c] == 0:
#                 continue
#             for r2 in range(c + 1, len(dp)):
#                 for c2 in range(r2, len(dp[r2])):
#                     if dp[r][c] < dp[r2][c2]:
#                         break
#                     if dp[r][c] == dp[r2][c2]:
#                         result = max(result, dp[r][c])
#
#     return result

def solution(cookie):
    result = 0
    for i in range(1, len(cookie)):
        son1, son2 = i - 1, i
        s1, s2 = cookie[son1], cookie[son2]
        while True:
            if s1 == s2:
                result = max(result, s1)
                son2 += 1
                if len(cookie) <= son2:
                    break
                s2 += cookie[son2]
            elif s1 < s2:
                son1 -= 1
                if son1 < 0:
                    break
                s1 += cookie[son1]
            else:
                son2 += 1
                if len(cookie) <= son2:
                    break
                s2 += cookie[son2]
    return result



print(solution([1,1,2,3]))
print(solution([1,2,4,5]))

