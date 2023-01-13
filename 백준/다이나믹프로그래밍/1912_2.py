import math

n = int(input())
arr = list(map(int, input().split()))

# dp = [-math.inf] * (n + 1)
# temp = 0
# for i in range(1, n + 1):
#     if temp + arr[i - 1] < 0:
#         dp[i] = temp + arr[i - 1]
#         temp = 0
#     else:
#         dp[i] = temp + arr[i - 1]
#         temp += arr[i - 1]

for i in range(1, n):
    arr[i] = max(arr[i], arr[i - 1] + arr[i])

print(max(arr))
