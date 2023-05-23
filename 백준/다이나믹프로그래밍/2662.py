
n, m = map(int, input().split())
arr = [[0] * (m + 1)] + [list(map(int, input().split())) for _ in range(n)]

res = [[0] * m for _ in range(n + 1)]
dp = [0] * (n + 1)
for c in range(1, m + 1):
    for i in range(n, -1, -1):
        for sep in range(i, -1, -1):
            if dp[i] < dp[sep] + arr[i - sep][c]:
                dp[i] = max(dp[i], dp[sep] + arr[i - sep][c])
                temp = res[sep][:]
                temp[c - 1] += i - sep
                res[i] = temp

print(dp[-1])
print(*res[-1])