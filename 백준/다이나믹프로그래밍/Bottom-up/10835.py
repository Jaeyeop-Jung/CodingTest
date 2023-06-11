import math

n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

dp = [[-math.inf] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 0
for left in range(n):
    for right in range(n):
        dp[left + 1][right] = max(dp[left + 1][right], dp[left][right])
        dp[left + 1][right + 1] = max(dp[left + 1][right + 1], dp[left][right])
        if arr1[left] > arr2[right]:
            dp[left][right + 1] = max(dp[left][right + 1], dp[left][right] + arr2[right])

res = max(max(dp[-1]), max([dp[i][-1] for i in range(n)]))
print(res if res != -math.inf else 0)