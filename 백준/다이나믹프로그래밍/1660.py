import math

n = int(input())
prefix = [1]
added = 3
cur = 3
while prefix[-1] <= n:
    prefix.append(cur + prefix[-1])
    cur += added
    added += 1
prefix.pop()
prefix.reverse()

def dfs(prefix, dp, cost):
    if cost == 0:
        return 0
    if dp[cost] != math.inf:
        return dp[cost]

    for i in prefix:
        if i <= cost:
            dp[cost] = min(dp[cost], dfs(prefix, dp, cost - i) + 1)

    return dp[cost]



dp = [math.inf] * (n + 1)
print(dfs(prefix, dp, n))

# dp = [math.inf] * (n + 1)
# dp[0] = 0
# for i in prefix:
#     for cost in range(i, n + 1):
#         dp[cost] = min(dp[cost], dp[cost - i] + 1)
#
# print(dp[-1])
