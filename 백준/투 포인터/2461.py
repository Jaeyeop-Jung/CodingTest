# TODO 틀림

import math
import sys
from bisect import bisect_left

input = sys.stdin.readline

n, m, = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

res = math.inf

def dfs(idx, minValue, maxValue, pre):
    if idx == n:
        global res
        res = min(res, maxValue - minValue)
        return

    curIdx = bisect_left(arr[idx], pre)
    # 3개 다 가능
    if 1 <= curIdx < m - 1:
        left, mid, right = arr[idx][curIdx - 1], arr[idx][curIdx], arr[idx][curIdx + 1]
        minDiff = min(abs(pre - left), abs(pre - mid), abs(pre - right))
        if minDiff == abs(pre - left):
            dfs(idx + 1, min(minValue, left), max(maxValue, left), left)
        elif minDiff == abs(pre - mid):
            dfs(idx + 1, min(minValue, mid), max(maxValue, mid), mid)
        elif minDiff == abs(pre - right):
            dfs(idx + 1, min(minValue, right), max(maxValue, right), right)
    # 왼쪽, 중앙
    elif 1 <= curIdx < m:
        left, mid = arr[idx][curIdx - 1], arr[idx][curIdx]
        minDiff = min(abs(pre - left), abs(pre - mid))
        if minDiff == abs(pre - left):
            dfs(idx + 1, min(minValue, left), max(maxValue, left), left)
        elif minDiff == abs(pre - mid):
            dfs(idx + 1, min(minValue, mid), max(maxValue, mid), mid)
    # 중앙, 오른쪽
    elif 0 <= curIdx < m - 1:
        mid, right = arr[idx][curIdx], arr[idx][curIdx + 1]
        minDiff = min(abs(pre - mid), abs(pre - right))
        if minDiff == abs(pre - mid):
            dfs(idx + 1, min(minValue, mid), max(maxValue, mid), mid)
        elif minDiff == abs(pre - right):
            dfs(idx + 1, min(minValue, right), max(maxValue, right), right)
    # 중앙
    elif 0 <= curIdx < m:
        mid = arr[idx][curIdx]
        dfs(idx + 1, min(minValue, mid), max(maxValue, mid), mid)

for start in range(m):
    dfs(1, arr[0][start], arr[0][start], arr[0][start])

print(res)