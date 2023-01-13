n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1
for r in range(len(dp)):
    for c in range(len(dp[r])):
        if r == n - 1 and c == n - 1:
            break
        movedR, movedC = r + arr[r][c], c
        if 0 <= movedR < n and 0 <= movedC < n:
            dp[movedR][movedC] += dp[r][c]
        movedR, movedC = r, c + arr[r][c]
        if 0 <= movedR < n and 0 <= movedC < n:
            dp[movedR][movedC] += dp[r][c]
print(dp[-1][-1])
