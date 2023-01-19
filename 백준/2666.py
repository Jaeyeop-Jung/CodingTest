import math
import sys

input = sys.stdin.readline

n = int(input())
cur1, cur2, = map(int, input().split())
m = int(input())
arr = [int(input()) for _ in range(m)]

result = math.inf
def dfs(idx, cur1, cur2, cnt):
    if idx == len(arr):
        global result
        result = min(result, cnt)
        return
    dfs(idx + 1, arr[idx], cur2, cnt + abs(arr[idx] - cur1))
    dfs(idx + 1, cur1, arr[idx], cnt + abs(arr[idx] - cur2))

dfs(0, cur1, cur2, 0)
print(result)

