# import random
# import sys
# sys.setrecursionlimit(10**8)
# 
# def sol1(n, k, arr):
#     import sys
#     from collections import defaultdict
# 
#     input = sys.stdin.readline
# 
#     # n, k, = map(int, input().split())
#     # arr = [int(input()) for _ in range(n)]
# 
#     def dfs(dp, cur, coin, idx):
#         key = tuple(coin)
#         if k < cur:
#             return 0
#         if k == cur:
#             return 1
#         if key in dp[cur]:
#             return dp[cur][tuple(coin)]
# 
#         for i in range(idx, len(arr)):
#             coin[i] += 1
#             dp[cur][key] += dfs(dp, cur + arr[i], coin, i)
#             coin[i] -= 1
# 
#         return dp[cur][key]
# 
#     dp = [defaultdict(int) for _ in range(k)]
#     return dfs(dp, 0, [0] * n, 0)
# def sol2(n, k, arr):
#     # n, k = map(int, input().split())
#     # coins = []
#     # for _ in range(n):
#     #     coins.append(int(input()))
# 
#     dp = [0] * (k + 1)
#     dp[0] = 1
#     # dp[i] -> i원을 만들 때 가능한 경우의 수
#     # dp[0] -> 동전 하나를 사용하는 경우 (coin이 3일 때, dp[3 - 3] = 1로 맞춰줌으로써 0원에서 3원을 더해 3원을 만드는 경우라고 생각)
# 
#     for coin in arr:
#         for i in range(coin, k + 1):
#             # coin원 동전으로 i원 만들기 -> i - coin원을 만든 후 coin원을 추가하는 것과 같음
#             # 즉, coin원으로 동전을 만드는 경우의 수 -> dp[i - coin]원
#             possible_cases = dp[i - coin]
#             dp[i] += possible_cases
# 
#     return dp[k]
# 
# for n in range(1, 101):
#     print(n)
#     for k in range(1, 300):
#         arr = random.sample(range(1, 100), n)
#         if sol1(n, k, arr) != sol2(n, k, arr):
#             print(n, k)
#             print(arr)
#             exit()

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

dp = [0] * (k + 1)
dp[0] = 1
for i in arr:
    for cur in range(i, k + 1):
        dp[cur] += dp[cur - i]
print(dp[-1])
