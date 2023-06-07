import math

def getScore(cur, next):
    if cur == 0:
        return 2
    elif cur == next:
        return 1
    elif cur % 2 == next % 2:
        return 4
    else:
        return 3

arr = list(map(int, input().split()))
arr.pop()
arr = [0] + arr

dp = [[[math.inf] * 5 for _ in range(5)] for _ in range(len(arr) + 1)]
dp[0][0][0] = 0
for i in range(1, len(arr)):
    move = arr[i]
    for left in range(5):
        for right in range(5):
            dp[i][move][right] = min(dp[i][move][right], dp[i - 1][left][right] + getScore(left, move))
            dp[i][left][move] = min(dp[i][left][move], dp[i - 1][left][right] + getScore(right, move))

print(min(map(min, dp[-2])))
