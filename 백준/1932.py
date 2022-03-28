
n = int(input())
arr = list()
for i in range(n):
    arr.append(list(map(int, input().split())))

dp = list()
for i in range(len(arr)):
    dp.append([0] * len(arr[i]))

dp[0][0] = arr[0][0]
if n == 1:
    print(arr[0][0])
else:
    dp[1][0] = dp[0][0] + arr[1][0]
    dp[1][1] = dp[0][0] + arr[1][1]
    for i in range(1, len(dp) - 1):
        for j in range(len(dp[i])):
            for k in range(j, j+2):
                dp[i+1][k] = max(dp[i+1][k], dp[i][j] + arr[i+1][k])


    print(max(dp[n-1]))