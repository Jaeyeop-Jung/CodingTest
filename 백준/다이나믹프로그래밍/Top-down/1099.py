# TODO 틀림

import math
import sys
from collections import Counter

input = sys.stdin.readline

target = input().strip()
n = int(input())
origin = list(set(input().strip() for _ in range(n)))
arr = [dict(Counter(origin[i])) for i in range(len(origin))]

def getDiff(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    return cnt

def dfs(dp, arr, idx):
    # if len(target) <= idx:
    #     global res
    #     res = min(res, cost)
    #     return
    #
    # cur = {}
    # for i in range(idx, len(target)):
    #     if target[i] not in cur:
    #         cur[target[i]] = 0
    #     cur[target[i]] += 1
    #
    #     available = []
    #     for j in range(len(arr)):
    #         if cur == arr[j]:
    #             available.append([j, getDiff(origin[j], target[idx:i + 1])])
    #     if available:
    #         available.sort(key=lambda x: x[1])
    #         dfs(arr, i + 1, cost + available[0][1])
    if len(target) <= idx:
        return 0
    if dp[idx] == -1:
        return math.inf
    if dp[idx] != math.inf:
        return dp[idx]

    cur = {}
    curStr = ''
    for i in range(idx, len(target)):
        if target[i] not in cur:
            cur[target[i]] = 0
        cur[target[i]] += 1
        curStr += target[i]

        for j in range(len(arr)):
            if len(curStr) == len(origin[j]) and cur == arr[j]:
                dp[idx] = min(dp[idx], dfs(dp, arr, i + 1) + getDiff(curStr, origin[j]))
    if dp[idx] == math.inf:
        dp[idx] = -1
        return math.inf
    return dp[idx]


dp = [math.inf] * len(target)
res = dfs(dp, arr, 0)
print(res if res != math.inf else -1)