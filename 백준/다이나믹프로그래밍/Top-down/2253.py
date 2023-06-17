# TODO 틀림 극한의 최적화를 해봐라

# import random
#
#
# def solve1():
#     import math
#     import sys
#
#     input = sys.stdin.readline
#
#     def dfs(dp, speed, location):
#         if n == location:
#             return 0
#         if dp[location] != math.inf:
#             return dp[location]
#
#         dp[location] = math.inf
#         if location + speed + 1 not in small and location + speed + 1 <= n:
#             dp[location] = min(dp[location], dfs(dp, speed + 1, location + speed + 1) + 1)
#         if location + speed not in small and location + speed <= n:
#             dp[location] = min(dp[location], dfs(dp, speed, location + speed) + 1)
#         if 1 <= speed - 1 and location + speed - 1 not in small and location + speed - 1 <= n:
#             dp[location] = min(dp[location], dfs(dp, speed - 1, location + speed - 1) + 1)
#
#         return dp[location]
#
#     dp = [math.inf] * (n + 1)
#     if n == 1:
#         print(0)
#         exit()
#     if 2 in small:
#         # print(-1)
#         # exit()
#         return -1
#     res = dfs(dp, 1, 2) + 1
#     # print(res if res != math.inf else -1)
#     return res if res != math.inf else -1
#
# def solve2():
#     import sys
#     input = sys.stdin.readline
#
#     dp = [[float('inf')] * (int((2 * n) ** 0.5) + 2) for _ in range(n + 1)]
#     dp[1][0] = 0
#     for i in range(2, n + 1):
#         if i in small: continue
#         for j in range(1, int((2 * i) ** 0.5) + 1):
#             dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1]) + 1
#
#     answer = min(dp[n])
#     # print(answer if answer != float('inf') else -1)
#     return answer if answer != float('inf') else -1
#
# for i in range(2, 10_000):
#     n, m = i, 0
#     small = {}
#     if solve1() != solve2():
#         print(n, m, small)
#     for j in range(1, i - 2):
#         small = {random.randint(2, i - 1): True for _ in range(random.randint(1, i - 1 - 2))}
#         res1 = solve1()
#         res2 = solve2()
#         if res1 != res2:
#             print(res1, res2)
#             print(n, m, small)
#             exit()
#

# -----------------------------------------------------------------------
import math
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m, = map(int, input().split())
small = [0] * (n + 1)
for _ in range(m):
    small[int(input())] = 1
check = False
def dfs(speed, location):
    if n == location:
        global check
        check = True
        return 0
    if dp[location][speed] != -1:
        return dp[location][speed]

    dp[location][speed] = math.inf
    for i in range(-1, 2):
        if speed + i >= 1:
            next = location + speed + i
            if next <= n and small[location] != 1:
                dp[location][speed] = min(dp[location][speed], dfs(speed + i, next) + 1)

    return dp[location][speed]

dp = [[-1] * (150) for _ in range(10001)]
res = dfs(0, 1)
print(res if check else -1)