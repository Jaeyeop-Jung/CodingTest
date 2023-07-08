
# def dfs(schedules, dp, cur):
#     if len(schedules) <= cur:
#         return 0
#     if dp[cur] != 0:
#         return dp[cur]
#
#     dp[cur] = max(dp[cur], dfs(schedules, dp, cur + 1), dfs(schedules, dp, cur + 2) + schedules[cur])
#     return dp[cur]
#
# def solution(schedules):
#
#     dp = [0] * len(schedules)
#     return dfs(schedules, dp, 0)

def solution(schedules):

    dp = [0] * len(schedules)
    for i in range(len(schedules)):
        dp[i] = max(dp[i], dp[i - 1], dp[i - 2] + schedules[i])
    return max(dp)

print(solution([30, 30, 60, 90, 60, 15, 15, 60]))
