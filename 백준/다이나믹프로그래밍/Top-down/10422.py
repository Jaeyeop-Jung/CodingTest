# TODO 틀림 잘 생각해봐 맞을 수 있다

# import sys
# sys.setrecursionlimit(10 ** 6)
#
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     if n % 2 == 1:
#         print(0)
#         continue
#
#     def dfs(dp, l, r):
#         if n == l + r:
#             if l == r:
#                 return 1
#             return 0
#         if (l, r) in dp:
#             return dp[(l, r)]
#
#         dp[(l, r)] = 0
#         if l <= r + n - (l + r):
#             dp[(l, r)] += dfs(dp, l + 1, r) % 1_000_000_007
#         if r + 1 <= l:
#             dp[(l, r)] += dfs(dp, l, r + 1) % 1_000_000_007
#         return dp[(l, r)] % 1_000_000_007
#
#     dp = {}
#     print(dfs(dp, 0, 0))

import sys
sys.setrecursionlimit(10 ** 6)

t = int(input())
for _ in range(t):
    n = int(input())
    if n % 2 == 1:
        print(0)
        continue

    def dfs(dp, cur):
        if n == cur:
            return 1
        if dp[cur] != 0:
            return dp[cur]

        for i in range(n, cur - 1, -2):
            dp[cur] += dfs(dp, i) * dfs(dp, i - 2)

        return dp[cur]


    dp = [0] * (n + 1)
    print(dfs(dp, 0))