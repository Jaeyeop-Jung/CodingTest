# TODO 틀림 어렵지만 잘 생각해봐 맞을 수 있다

import sys

input = sys.stdin.readline

garo, sero, height, = map(int, input().split())
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()

def dfs(arr, l, w, h, cnt):
    global res
    if l == 0 or w == 0 or h == 0:
        return

    for i in range(len(arr) - 1, -1, -1):
        length, num, = arr[i]
        if num == 0:
            continue
        length = 2 ** length
        if min(l, w, h) < length:
            continue

        arr[i][1] -= 1
        res += 1
        dfs(arr, l, w - length, h, cnt + 1)
        dfs(arr, length, length, h - length, cnt + 1)
        dfs(arr, length, w - length, h, cnt + 1)



res = 0
dfs(arr, garo, sero, height, 0)
print(res)