# TODO 틀림 https://whatryando.tistory.com/85

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = map(int, input().split())

words = []
for i in range(n):
    words.append(int(input()))

dp = [[-1 for i in range(m)]for j in range(n)]

def dfs(dp, idx, length):
    if dp[idx][length] != -1:
        pass
    else:
        if idx == n-1:
            dp[idx][length] = 0
        else:
            if length + 1 + words[idx + 1] < m :
                dp[idx][length] = min(dfs(dp, idx + 1, length + 1 + words[idx + 1]), dfs(dp, idx + 1, words[idx + 1] - 1) + (m - length - 1) * (m - length - 1))
            else:
                dp[idx][length] = dfs(dp, idx + 1, words[idx + 1] - 1) + (m - length - 1) * (m - length - 1)
    return dp[idx][length]

print(dfs(dp, 0, words[0]-1))