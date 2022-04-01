
n = int(input())
arr = list()
for i in range(n):
    arr.append(list(map(int, input().split())))

dp = [0] * (n + 1)

if arr[0][0] == 1:
    dp[0] += arr[0][1]
for i in range(n):
    if i + arr[i][0] <= n:
        dp[i] = arr[i][1]
        for j in range(i):
            if j + arr[j][0] <= i:
                dp[i] = max(dp[i], dp[j] + arr[i][1])

print(max(dp))
