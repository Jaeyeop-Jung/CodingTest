# TODO 틀림 잘 생각해봐라

# from string import ascii_lowercase
#
# arr = list(input())
#
# alphabet = ascii_lowercase
# res = 0
# cur = 0
# for alpha in alphabet:
#     if alpha not in arr:
#         continue
#
#     rIndex = len(arr) - arr[-1::-1].index(alpha) - 1
#     lIndex = arr.index(alpha)
#     for i in range(len(arr)):
#         if arr[i] == alpha:
#             res += 1
#             arr[i] = ''
#     if abs(cur - rIndex) < abs(cur - lIndex):
#         res += abs(cur - rIndex) + rIndex - lIndex
#         cur = lIndex
#     else:
#         res += abs(cur - lIndex) + rIndex - lIndex
#         cur = rIndex
#
# print(res)
import math
from string import ascii_lowercase

arr = list(input())

alphabet = ascii_lowercase

n = len(set(arr))
dp = [[[math.inf] * 2 for _ in range(2)] for _ in range(n)]
for alpha in alphabet:
    if alpha not in arr:
        continue

