from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))

dp = []
for i in range(len(arr)):
    if not dp or dp[-1] < arr[i]:
        dp.append(arr[i])
    else:
        idx = bisect_left(dp, arr[i])
        dp[idx] = arr[i]

print(len(dp))
