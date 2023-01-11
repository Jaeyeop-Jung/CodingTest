r, c, w, = map(int, input().split())

dp = [[1]]
for curR in range(1, r + w - 1):
    temp = []
    for curC in range(curR + 1):
        left = 0
        if 0 <= curC - 1 < curR + 1:
            left = dp[curR - 1][curC - 1]
        right = 0
        if 0 <= curC < curR:
            right = dp[curR - 1][curC]
        temp.append(left + right)
    dp.append(temp)

result = 0
cnt = 1
for curR in range(r - 1, len(dp)):
    for curC in range(c - 1, c - 1 + cnt):
        result += dp[curR][curC]
    cnt += 1

print(result)