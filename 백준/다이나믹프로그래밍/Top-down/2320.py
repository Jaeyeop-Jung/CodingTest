# TODO 틀림

n = int(input())
arr = [input() for _ in range(n)]

def recur(arr, dp, visit, start):
    if visit in dp:
        return dp[visit]

    dp[visit] = 0
    if visit == 0:
        for i in range(n):
            next = visit | (1 << i)
            dp[visit] = max(dp[visit], recur(arr, dp, next, arr[i][-1]) + len(arr[i]))
    else:
        for i in range(n):
            if start != arr[i][0] or visit & (1 << i):
                continue
            next = visit | (1 << i)
            dp[visit] = max(dp[visit], recur(arr, dp, next, arr[i][-1]) + len(arr[i]))

    return dp[visit]


dp = {}
print(recur(arr, dp, 0, ''))