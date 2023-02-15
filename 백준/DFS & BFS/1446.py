import math
import sys

input = sys.stdin.readline

n, d, = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def dfs(cur, cost):
    if cur == d:
        global result
        result = min(result, cost)
        return

    for i in range(len(arr)):
        start, end, dist, = arr[i]
        if cur <= start and end <= d:
            dfs(end, cost + start - cur + dist)
    dfs(d, cost + d - cur)

result = math.inf
dfs(0, 0)
print(result)