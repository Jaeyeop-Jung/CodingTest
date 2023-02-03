# TODO 틀림

n = int(input())
arr = list(map(int, input().split()))

# dp = [0] * n
# dp[1] = max(arr[:2]) - min(arr[:2])
# dp[2] = max(arr[:3]) - min(arr[:3])
# for i in range(3, n):
#     l = dp[i - 2] + max(arr[i - 1:i + 1]) - min(arr[i - 1:i + 1])
#     r = dp[i - 3] + max(arr[i - 2:i + 1]) - min(arr[i - 2:i + 1])
#     dp[i] = max(l, r)

dp = [0] * n
for i in range(1, n):
    for j in range(0, i + 1):
        ma = max(arr[i - j:i + 1])
        mi = min(arr[i - j:i + 1])
        if i - j - 1 == -1:
            j = i - 1
        dp[i] = max(dp[i], dp[i - j - 1] + abs(ma - mi))

print(dp[-1])
