# import sys
#
# sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline
#
# def find_parent(parent, x):
#     if parent[x][0] != x:
#         parent[x][0] = find_parent(parent, parent[x][0])
#     return parent[x][0]
#
# def union_parent(parent, x, y):
#     a = find_parent(parent, x)
#     b = find_parent(parent, y)
#     if a < b:
#         parent[a] = [parent[a][0], parent[a][1] + parent[b][1], parent[a][2] + parent[b][2]]
#         parent[b] = [a, 0, 0]
#     else:
#         parent[b] = [parent[b][0], parent[b][1] + parent[a][1], parent[b][2] + parent[a][2]]
#         parent[a] = [b, 0, 0]
#
# n, m, k = map(int, input().split())
# arr = list(map(int, input().split()))
# parent = [[i, 1, arr[i]] for i in range(n)]
# for _ in range(m):
#     a, b = map(int, input().split())
#     union_parent(parent, a - 1, b - 1)
#
# temp = []
# for parentNum, memberCnt, total in parent:
#     if memberCnt != 0:
#         temp.append([memberCnt, total])
#
# def dfs(arr, dp, idx, cost):
#     if idx == len(arr):
#         return 0
#     if dp[idx][cost]:
#         return dp[idx][cost]
#
#     if cost + arr[idx][0] < k:
#         dp[idx][cost] = max(dp[idx][cost], dfs(arr, dp, idx + 1, cost + arr[idx][0]) + arr[idx][1])
#     dp[idx][cost] = max(dp[idx][cost], dfs(arr, dp, idx + 1, cost))
#
#     return dp[idx][cost]
#
# print(dfs(temp, [[0] * sum([i[0] for i in temp]) for _ in range(len(temp))], 0, 0))

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
parent = [i for i in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    union_parent(parent, a - 1, b - 1)

for i in range(n):
    find_parent(parent, i)

pparent = set([i for i in parent])
temp = {p: [0, 0] for p in pparent}
totalCost = 0
for i in range(n):
    temp[find_parent(parent, i)][0] += 1
    temp[find_parent(parent, i)][1] += arr[i]
temp = [temp[key] for key in temp]

# def dfs(arr, dp, idx, cost):
#     if idx == len(arr):
#         return 0
#     if dp[idx]:
#         return dp[idx]
#
#     if cost + arr[idx][0] < k:
#         dp[idx][cost] = max(dp[idx][cost], dfs(arr, dp, idx + 1, cost + arr[idx][0]) + arr[idx][1])
#     dp[idx][cost] = max(dp[idx][cost], dfs(arr, dp, idx + 1, cost))
#
#     return dp[idx][cost]
#
# print(dfs(temp, [[0] * sum([i[0] for i in temp]) for _ in range(len(temp))], 0, 0))

dp = [0] * k
for i in range(len(temp)):
    mCnt, cost, = temp[i]
    for j in range(k - 1, mCnt - 1, -1):
        dp[j] = max(dp[j], dp[j - mCnt] + cost)
print(max(dp))
