# TODO 틀림 잘 생각해봐 이건 맞아야지..

import math

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def dfs(arr, dp, idx, before, start):
    if idx == n - 1:
        for cur in range(n):
            if before == cur or cur == start:
                continue
            if dp[idx - 1][before] + arr[idx][cur] < dp[idx][cur]:
                dp[idx][cur] = dp[idx - 1][before] + arr[idx][cur]
        return

    for cur in range(n):
        if cur == before:
            continue
        if dp[idx - 1][before] + arr[idx][cur] < dp[idx][cur]:
            dp[idx][cur] = dp[idx - 1][before] + arr[idx][cur]
            dfs(arr, dp, idx + 1, cur, start)


dp = [[math.inf] * 3 for _ in range(n)]
dp[0] = arr[0][:]
for start in range(3):
    dfs(arr, dp, 1, start, start)

print(min(dp[-1]))