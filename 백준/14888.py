# TODO 틀림 개념은 맞는데 구현에 좀 더 신경써라

import math
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
plus, minus, multi, div = map(int, input().split())
op_cnt = plus + minus + multi + div

resMax = -math.inf
resMin = math.inf

def dfs(total, cnt, next):
    global plus
    global minus
    global multi
    global div
    if cnt == op_cnt:
        global resMax
        global resMin
        resMax = max(resMax, total)
        resMin = min(resMin, total)
        return
    for i in range(4):
        if i == 0 and 0 < plus:
            plus -= 1
            dfs(total + arr[next], cnt + 1, next + 1)
            plus += 1
        elif i == 1 and 0 < minus:
            minus -= 1
            dfs(total - arr[next], cnt + 1, next + 1)
            minus += 1
        elif i == 2 and 0 < multi:
            multi -= 1
            dfs(total * arr[next], cnt + 1, next + 1)
            multi += 1
        elif i == 3 and 0 < div:
            div -= 1
            dfs(int(total / arr[next]), cnt + 1, next + 1)
            div += 1

for i in range(4):
    if i == 0 and 0 < plus:
        plus -= 1
        dfs(arr[0] + arr[1], 1, 2)
        plus += 1
    elif i == 1 and 0 < minus:
        minus -= 1
        dfs(arr[0] - arr[1], 1, 2)
        minus += 1
    elif i == 2 and 0 < multi:
        multi -= 1
        dfs(arr[0] * arr[1], 1, 2)
        multi += 1
    elif i == 3 and 0 < div:
        div -= 1
        dfs(int(arr[0] / arr[1]), 1, 2)
        div += 1

print(resMax)
print(resMin)