import sys
input = sys.stdin.readline
from bisect import bisect_left

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x: x[0])
dp = []
for i in range(len(arr)):
    if not dp or dp[-1] < arr[i][1]:
        dp.append(arr[i][1])
    else:
        idx = bisect_left(dp, arr[i][1])
        dp[idx] = arr[i][1]

print(n - len(dp))
