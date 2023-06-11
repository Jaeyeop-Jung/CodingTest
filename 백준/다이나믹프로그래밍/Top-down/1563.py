# TODO 틀림

import sys
sys.setrecursionlimit(10 ** 8)

n = int(input())

def dfs(n, dp, day, late, absent):
    if late == 2 or absent == 3:
        return 0
    if n == day:
        return 1
    if (day, late, absent) in dp:
        return dp[(day, late, absent)]

    a = dfs(n, dp, day + 1, late, 0)
    b = dfs(n, dp, day + 1, late + 1, 0)
    c = dfs(n, dp, day + 1, late, absent + 1)
    dp[(day, late, absent)] = a + b + c % 1_000_000
    return dp[(day, late, absent)]



dp = {}
print(dfs(n, dp, 0, 0, 0) % 1_000_000)