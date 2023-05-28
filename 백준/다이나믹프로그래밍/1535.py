
n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

dp = [0] * 100
for i in range(n):
    for j in range(99, arr1[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - arr1[i]] + arr2[i])

print(dp[-1])
