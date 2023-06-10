# TODO 틀림

# from collections import deque
# from itertools import permutations
#
# n = int(input())
# arr = list(map(int, input().split()))
#
# q = deque()
# q.append([arr[:], 0])
# visited = {tuple(arr[:]): True}
# while q:
#     remain, cnt, = q.popleft()
#     if all([i <= 0 for i in remain]):
#         print(cnt)
#         exit()
#
#     comb = [i for i in range(len(remain))]
#     for i in permutations(comb, len(remain)):
#         newRemain = remain[:]
#         damage = 9
#         for idx, v in enumerate(i):
#             if 0 < newRemain[v]:
#                 newRemain[v] -= damage
#                 damage //= 3
#         if tuple(newRemain) not in visited:
#             q.append([newRemain, cnt + 1])
#             visited[tuple(newRemain)] = True
#

import math
from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))

def dfs(dp, cur, cnt):
    if all([i <= 0 for i in cur]):
        return 0
    if tuple(cur) in dp:
        return dp[tuple(cur)]

    minimum = math.inf
    for i in permutations([i for i in range(len(cur))], len(cur)):
        damage = 9
        for j in i:
            cur[j] -= damage
            damage //= 3
        minimum = min(minimum, dfs(dp, cur, cnt + 1))
        damage = 9
        for j in i:
            cur[j] += damage
            damage //= 3

    dp[tuple(cur)] = minimum + 1
    return minimum + 1

dp = {}
print(dfs(dp, arr, 0))