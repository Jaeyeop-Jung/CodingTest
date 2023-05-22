
t = int(input())
for test_case in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    dp = [0] * n
    for i in range(n):
        if arr[i][0] == 1:
            for j in range(i + 1, n):
                if arr[i][1] == arr[j][1] and arr[j][0] == -1:
                    dp[j] = max(dp[j], max(dp[:i + 1]) + arr[i][1])
                    break
            else:
                dp[-1] = max(dp[-1], dp[i])

    print(f'#{test_case} {max(dp)}')