# import math
# import sys
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# arr = {i: True for i in arr}
#
# def dfs(arr, dp, day, one, three, five, coupon):
#     if n < day:
#         return 0
#     if (day, one, three, five, coupon) in dp:
#         return dp[(day, one, three, five, coupon)]
#
#     cur = math.inf
#     if day in arr:
#         cur = min(cur, dfs(arr, dp, day + 1, one, three, five, coupon))
#     else:
#         if 3 <= coupon:
#             cur = min(cur, dfs(arr, dp, day + 1, one, three, five, coupon - 3))
#         cur = min(cur, dfs(arr, dp, day + 1, one + 1, three, five, coupon) + 10000)
#         cur = min(cur, dfs(arr, dp, day + 3, one, three + 1, five, coupon + 1) + 25000)
#         cur = min(cur, dfs(arr, dp, day + 5, one, three, five + 1, coupon + 2) + 37000)
#     dp[(day, one, three, five, coupon)] = cur
#     return cur
#
#
# dp = {}
# print(dfs(arr, dp, 1, 0, 0, 0, 0))

import math
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr = {i: True for i in arr}

def dfs(arr, dp, day, coupon):
    if n < day:
        return 0
    if (day, coupon) in dp:
        return dp[(day, coupon)]

    cur = math.inf
    if day in arr:
        cur = min(cur, dfs(arr, dp, day + 1, coupon))
    else:
        if 3 <= coupon:
            cur = min(cur, dfs(arr, dp, day + 1, coupon - 3))
        cur = min(cur, dfs(arr, dp, day + 1, coupon) + 10000)
        cur = min(cur, dfs(arr, dp, day + 3, coupon + 1) + 25000)
        cur = min(cur, dfs(arr, dp, day + 5, coupon + 2) + 37000)
    dp[(day, coupon)] = cur
    return cur


dp = {}
print(dfs(arr, dp, 1, 0))