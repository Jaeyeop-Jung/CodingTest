
n, m, c = map(int, input().split())
arr = list(map(int, input().split()))

def recur(arr, dp, visit, cnt, rest):
    if (visit, cnt, rest) in dp:
        return dp[(visit, cnt, rest)]

    dp[(visit, cnt, rest)] = 0
    for i in range(n):
        if not visit & (1 << i) and arr[i] <= c:
            next = visit | (1 << i)
            if rest < arr[i]:
                if cnt < m:
                    dp[(visit, cnt, rest)] = max(dp[(visit, cnt, rest)], recur(arr, dp, next, cnt + 1, c - arr[i]) + 1)
            else:
                dp[(visit, cnt, rest)] = max(dp[(visit, cnt, rest)], recur(arr, dp, next, cnt, rest - arr[i]) + 1)

    return dp[(visit, cnt, rest)]

dp = {}
print(recur(arr, dp, 0, 1, c))