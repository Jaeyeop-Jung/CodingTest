import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    arr.append(list(map(int, input().split())))
    arr.append(list(map(int, input().split())))

    dp = [[0] * n for i in range(2)]
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    if n == 1:
        print(max(map(max, dp)))
        continue

    dp[0][1] = dp[1][0] + arr[0][1]
    dp[1][1] = dp[0][0] + arr[1][1]
    if n == 2:
        print(max(map(max, dp)))
        continue

    for column in range(2, n):
        for row in range(2):
            if row == 0:
                # 1 2 3     dp[0][2]의 값을 알고 싶다면 dp[1][1] + arr[0][2] or dp[0][:]들의 큰 값 + dp[0][2]를 하면 된다.
                # 4 5 6
                dp[row][column] = max(dp[1][column - 1] + arr[row][column], max(dp[0][column - 2], dp[1][column - 2]) + arr[row][column])
            else:
                dp[row][column] = max(dp[0][column - 1] + arr[row][column], max(dp[0][column - 2], dp[1][column - 2]) + arr[row][column])
    print(max(map(max, dp)))
