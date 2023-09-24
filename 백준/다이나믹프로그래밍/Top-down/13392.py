# TODO 틀림 거의 맞았는데 잘 생각해봐라

# import math
# import random
# import sys
#
# sys.setrecursionlimit(10 ** 6)
#
#
#
# def sol1(n, arr,target):
#     def dfs(target, arr, dp, l, idx):
#         if idx == n:
#             return 0
#         if dp[idx][l] != math.inf:
#             return dp[idx][l]
#
#         cur = arr[idx] + l
#         # 왼쪽
#         if cur <= target[idx]:
#             diff = abs(target[idx] - cur)
#         else:
#             diff = abs(10 - cur) + target[idx]
#         dp[idx][l] = min(dp[idx][l], dfs(target, arr, dp, (l + diff) % 10, idx + 1) + diff)
#
#         # 오른쪽
#         if target[idx] <= cur:
#             diff = cur - target[idx]
#         else:
#             diff = cur + 10 - target[idx]
#         dp[idx][l] = min(dp[idx][l], dfs(target, arr, dp, l, idx + 1) + diff)
#
#         return dp[idx][l]
#
#     dp = [[math.inf] * 10 for _ in range(n)]
#     return dfs(target, arr, dp, 0, 0)
#
# def sol2(n, arr, res):
#     def go(idx, left):
#         # Base Case : 모두 돌린경우
#         if idx == n:
#             return 0
#         # Memoization
#         if dp[idx][left] != -1:
#             return dp[idx][left]
#         dp[idx][left] = 9876543210
#         # 위층에서 돌린 만큼 현재 숫자 재정의
#         if left:
#             now = (arr[idx] + left) % 10
#         else:
#             now = arr[idx]
#         # 점화식
#         dp[idx][left] = min(dp[idx][left], go(idx + 1, (left + left_cache[now][res[idx]]) % 10) + left_cache[now][res[idx]])
#         dp[idx][left] = min(dp[idx][left], go(idx + 1, left) + right_cache[now][res[idx]])
#         return dp[idx][left]
#
#     # left_cache : 현재 수가 i, 맞춰야 하는 수가 j일 때 왼쪽으로 몇칸 돌려야 하는지를 저장하는 2차원 배열
#     left_cache = [[-1] * 10 for _ in range(10)]
#
#     # right_cache : 현재 수가 i, 맞춰야 하는 수가 j일 때 오른쪽으로 몇칸 돌려야 하는지를 저장하는 2차원 배열
#     right_cache = [[-1] * 10 for _ in range(10)]
#     for i in range(10):
#         for j in range(10):
#             temp = 0
#             while True:
#                 if (i + temp) % 10 == j:
#                     break
#                 temp += 1
#             left_cache[i][j] = temp
#             temp = 0
#             while True:
#                 if (i - temp) % 10 == j:
#                     break
#                 temp += 1
#             right_cache[i][j] = temp
#
#     # 입력부 및 정답출력
#     # n = int(sys.stdin.readline())
#     dp = [[-1] * 10 for _ in range(n)]
#     # arr = list(map(int, sys.stdin.readline().rstrip()))
#     # res = list(map(int, sys.stdin.readline().rstrip()))
#     return go(0, 0)
#
# cnt = 0
# while True:
#     flag = False
#     n = 10000
#     arr, res = [], []
#     for _ in range(n):
#         arr.append(random.randrange(0, 10))
#         res.append(random.randrange(0, 10))
#     res1 = sol1(n, arr, res)
#     res2 = sol1(n, arr, res)
#     if res1 != res2:
#         print(n)
#         print(arr)
#         print(res)
#         print(res1)
#         print(res2)
#         break
#     cnt += 1

import math
import sys

sys.setrecursionlimit(10 ** 6)

n = int(input())
arr = list(map(int, list(input())))
target = list(map(int, list(input())))

def dfs(target, arr, dp, l, idx):
    if idx == n:
        return 0
    if dp[idx][l] != math.inf:
        return dp[idx][l]

    cur = (arr[idx] + l) % 10
    # 왼쪽
    if cur <= target[idx]:
        diff = abs(target[idx] - cur)
    else:
        diff = abs(10 - cur) + target[idx]
    dp[idx][l] = min(dp[idx][l], dfs(target, arr, dp, (l + diff) % 10, idx + 1) + diff)

    # 오른쪽
    if target[idx] <= cur:
        diff = cur - target[idx]
    else:
        diff = cur + 10 - target[idx]
    dp[idx][l] = min(dp[idx][l], dfs(target, arr, dp, l, idx + 1) + diff)

    return dp[idx][l]

dp = [[math.inf] * 10 for _ in range(n)]
print(dfs(target, arr, dp, 0, 0))