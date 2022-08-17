import math
import sys

input = sys.stdin.readline

n = int(input())
arr = []
arr.append(0)
arr += list(map(int, input().split()))

if n == 1:
    print(arr[1])
else:
    dp = [-math.inf] * (n + 1)
    dp[1] = arr[1]
    for i in range(2, n + 1):
        if arr[i] < 0:
            dp[i] = max(dp[i - 1] + arr[i], arr[i])
        else:
            dp[i] = max(dp[i - 1] + arr[i], arr[i])
    print(max(dp))

# if n == 1:
#     print(arr[1])
# else:
#     dp = [-math.inf] * (n + 1)
#     for i in range(1, n + 1):
#         dp[i] = max(dp[i - 1] + arr[i], arr[i])
#         # result = max(result, dp[i])
#     print(max(dp))