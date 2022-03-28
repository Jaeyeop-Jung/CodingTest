
n = int(input())
arr = list()
for i in range(n):
    arr.append(list(map(int, input().split())))

dp = list()
for i in range(n):
    dp.append([1000000, 1000000, 1000000])

dp[0] = arr[0]

for i in range(1, n):
    for j in range(3):
        for k in range(3):
            if j != k:
                dp[i][j] = min(dp[i][j], dp[i-1][k] + arr[i][j])

print(min(dp[n - 1]))
