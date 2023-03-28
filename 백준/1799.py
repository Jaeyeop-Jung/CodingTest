# TODO 틀림

import sys
sys.setrecursionlimit(10 ** 8)

dR = [1, 1, -1, -1]
dC = [1, -1, -1, 1]

def can(arr, r, c):
    for i in range(4):
        curR, curC = r, c
        while True:
            curR, curC = curR + dR[i], curC + dC[i]
            if not 0 <= curR < n or not 0 <= curC < n:
                break
            if arr[curR][curC] == 2:
                return False
    return True


def dfs(arr, curR, curC, cnt):
    global result
    result = max(result, cnt)
    for r in range(curR, n):
        for c in range(curC, n):
            if arr[r][c] == 1 and can(arr, r, c):
                arr[r][c] = 2
                dfs(arr, r, c, cnt + 1)
                arr[r][c] = 1

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = 0
dfs(arr, 0, -1, 0)
print(result)