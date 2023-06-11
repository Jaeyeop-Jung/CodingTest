import math
import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

def dfs(left, right):
    if n == left or n == right:
        return 0
    if dp[left][right] != -1:
        return dp[left][right]

    cur = -1
    if arr1[left] > arr2[right]:
        cur = max(cur, dfs(left, right + 1) + arr2[right])
    else:
        cur = max(cur, dfs(left + 1, right))
        cur = max(cur, dfs(left + 1, right + 1))
    dp[left][right] = cur
    return cur

dp = [[-1] * (n) for _ in range(n)]
print(dfs(0, 0))