from string import ascii_uppercase
import sys
sys.setrecursionlimit(10 ** 4)

arr = list(input())
z_ = [''] + list(ascii_uppercase)
dic = {str(i): v for i, v in enumerate(z_)}
def dfs(dp, idx):
    if idx == len(arr):
        return 1
    if dp[idx] != 0:
        return dp[idx]

    if arr[idx] != '0':
        dp[idx] += dfs(dp, idx + 1) % 1000000
    if idx + 1 < len(arr) and ''.join(arr[idx:idx + 2]) in dic:
        dp[idx] += dfs(dp, idx + 2) % 1000000
    dp[idx] %= 1000000
    return dp[idx]

dp = [0] * len(arr)
print(dfs(dp, 0))