# TODO 틀림 어렵지만 잘 생각해봐 할 수 있다. 트리를 그려봐

import sys

input = sys.stdin.readline

def dfs(me, arr, dp, left, right):
    if right < left:
        return 0
    if dp[left][right] != -1:
        return dp[left][right]

    # 나
    if me:
        dp[left][right] = max(
            dfs(False, arr, dp, left + 1, right) + arr[left],
            dfs(False, arr, dp, left, right - 1) + arr[right]
        )
    # 상대방
    else:
        dp[left][right] = min(
            dfs(True, arr, dp, left + 1, right),
            dfs(True, arr, dp, left, right - 1)
        )

    return dp[left][right]

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    dp = [[-1] * n for _ in range(n)]
    dfs(True, arr, dp, 0, n - 1)
    print(dp[0][-1])