import math
import sys

input = sys.stdin.readline

def dfs(arr, dp, idx, visited):
    if idx == 11:
        return 0
    if (idx, visited) in dp:
        return dp[(idx, visited)]

    dp[(idx, visited)] = 0
    for position, score in arr[idx]:
        if not (visited & 1 << position):
            dp[(idx, visited)] = max(dp[(idx, visited)], dfs(arr, dp, idx + 1, visited | 1 << position) + score)
    return dp[(idx, visited)]

t = int(input())
for _ in range(t):
    arr = []
    for i in range(11):
        arr.append([])
        temp = list(map(int, input().split()))
        for j in range(11):
            if 0 < temp[j]:
                arr[-1].append((j, temp[j]))

    print(dfs(arr, {}, 0, 0))