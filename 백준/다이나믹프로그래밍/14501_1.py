
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = [0] * (n + 1)
for i in range(len(arr)):
    if i + arr[i][0] <= len(arr):
        dp[i + arr[i][0]] = max(max(dp[:i + 1]) + arr[i][1], dp[i] + arr[i][1], dp[i + arr[i][0]])

print(max(dp))
