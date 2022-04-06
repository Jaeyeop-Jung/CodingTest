
n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n

dp[0] = arr[0]
for i in range(1, n):
    for j in range(i):
        dp[i] = max(dp[j] + arr[i-j-1], arr[i], dp[i])

print(max(dp))
