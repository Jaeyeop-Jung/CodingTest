import sys
sys.setrecursionlimit(10 ** 8)

def dfs(dp, arr, cur):
    if len(arr) <= cur:
        return 0
    if dp[cur] != 0:
        return dp[cur]

    # 노선택
    dp[cur] = max(dp[cur], dfs(dp, arr, cur + 1))

    # 선택
    dp[cur] = max(dp[cur], dfs(dp, arr, cur + 2) + arr[cur])

    return dp[cur]

def solution(money):
    dp0 = [0] * len(money)
    dp1 = [0] * len(money)
    return max(dfs(dp0, money[2:-1], 0) + money[0], dfs(dp1, money[1:-2], 0) + money[-1])


# print(solution([1, 2, 3, 1]))
print(solution([1, 2, 3, 4, 5, 6]))