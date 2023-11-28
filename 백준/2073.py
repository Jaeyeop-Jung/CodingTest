# TODO 틀림

import math
import sys

input = sys.stdin.readline

d, p, = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(p)]

def recur(arr, dp, idx, value, length):
    if idx == p:
        if
        return value
    if (idx, length) in dp:
        return dp[(idx, length)]

    # 선택
    dp[(idx, length)] = value
    if length + arr[idx][0] <= d:
        dp[(idx, length)] = max(dp[(idx, length)], recur(arr, dp, idx + 1, min(value, arr[idx][1]), length + arr[idx][0]))

    # 안선택
    dp[(idx, length)] = max(dp[(idx, length)], recur(arr, dp, idx + 1, value, length))

    return dp[(idx, length)]


print(recur(arr, {}, 0, math.inf, 0))