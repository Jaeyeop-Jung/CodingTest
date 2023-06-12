import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def dfs(r, c, milk):
    if r == n or c == n:
        return 0
    if dp[r][c][milk] != 0:
        return dp[r][c][milk]

    nextMilk = (milk + 1) % 3
    if arr[r][c] == milk:
        # 먹을 때
        dp[r][c][milk] = max(
            dp[r][c][milk],
            dfs(r + 1, c, nextMilk) + 1,
            dfs(r, c + 1, nextMilk) + 1,
            dfs(r + 1, c, nextMilk) + 1,
            dfs(r, c + 1, nextMilk) + 1
        )
    else:
        dp[r][c][milk] = max(
            dp[r][c][milk],
            dfs(r + 1, c, milk),
            dfs(r, c + 1, milk)
        )
    return dp[r][c][milk]


dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
print(dfs(0, 0, 0))