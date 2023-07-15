# TODO 틀림 조금만 더 생각해봐 맞출 수 있다

n = int(input())

def dfs(dp, cur):
    if cur == 0:
        return 0
    if dp[cur]:
        return dp[cur]

    dp[cur] = max(dp[cur], dfs(dp, cur - 1) + 1)
    cnt = 2
    for i in range(3, cur + 1):
        dp[cur] = max(dp[cur], dp[cur - i] * cnt)
        cnt += 1

    return dp[cur]


dp = [0] * (n + 1)
print(dfs(dp, n))