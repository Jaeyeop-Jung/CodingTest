# TODO 틀림

import math
import sys

input = sys.stdin.readline
arr = [[], [], ['1'], ['7'], ['4'], ['2', '3', '5'], ['6', '9', '0'], ['8'], []]

def dfsMin(arr, dpMin, cur, depth):
    if cur <= 1:
        return math.inf
    if dpMin[cur] != math.inf:
        return dpMin[cur]

    ret = math.inf
    for i in range(min(cur, len(arr) - 1), 1, -1):
        for num in arr[i]:
            if cur - i == 1:
                continue
            temp = dfsMin(arr, dpMin, cur - i, depth + 1) * 10 + int(num)
            ret = min(ret, temp)
    dpMin[cur] = ret
    return dpMin[cur]

def dfsMax(arr, dpMax, cur, depth):
    if cur == 0:
        return ''
    if dpMax[cur] != -math.inf:
        return dpMax[cur]

    ret = '-1'
    for i in range(min(cur, len(arr) - 1), 1, -1):
        for num in arr[i]:
            if depth == 0 and num == '0':
                continue
            if cur - i == 1:
                continue
            temp = num + dfsMax(arr, dpMax, cur - i, depth + 1)
            if int(temp) > int(ret):
                ret = temp
    dpMax[cur] = ret
    return dpMax[cur]

cnt = int(input())

dpMin = [math.inf] * (101)
dpMax = [-math.inf] * (101)

dpMin[2] = 1
dpMin[3] = 7
dpMin[4] = 4
dpMin[5] = 2
dpMin[6] = 6
dpMin[7] = 8


dfsMin(arr, dpMin, cnt, 0)
dfsMax(arr, dpMax, cnt, 0)

print(dpMin[cnt], int(dpMax[cnt]))