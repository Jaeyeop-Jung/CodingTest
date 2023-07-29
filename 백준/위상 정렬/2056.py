# TODO 틀림 잘 생각해라 뇌 빼지말고

# import random
# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# def sol1(n, arr):
#     pre = [0] + [arr[i][1] for i in range(len(arr))]
#     next = {i: [] for i in range(1, n + 1)}
#     res = [0] + [0] * n
#
#     q = deque()
#     for i in range(len(arr)):
#         if 0 < arr[i][1]:
#             for j in range(2, 2 + arr[i][1]):
#                 next[arr[i][j]].append(i + 1)
#         else:
#             q.append([arr[i][0], 0, i + 1])
#
#     while q:
#         spendTime, preTime, cur = q.popleft()
#         res[cur] = max(res[cur], spendTime + preTime)
#         for nextTask in next[cur]:
#             pre[nextTask] -= 1
#             res[nextTask] = max(res[nextTask], spendTime + preTime + arr[nextTask - 1][0])
#             if pre[nextTask] == 0:
#                 q.append([arr[nextTask - 1][0], spendTime + preTime, nextTask])
#                 res[nextTask] = max(res[nextTask], res[cur] + arr[nextTask - 1][0])
#
#     return max(res)
#
# def sol2(n, array):
#     indegree = [0] * (n+1)
#     graph = [[] for _ in range(n+1)]
#     dp = [0] * (n+1)
#     t = [0]
#
#     cnt = 0
#     for i in range(1, n+1):
#         temp = array[cnt]
#         t.append(temp[0])
#         if temp[1] != 0:
#             for j in range(2, len(temp)):
#                 graph[temp[j]].append(i)
#                 indegree[i] += 1
#         cnt += 1
#
#     q = deque()
#     for i in range(1, n+1):
#         if indegree[i] == 0:
#             q.append(i)
#             dp[i] = t[i]
#     while q:
#         now = q.popleft()
#         for i in graph[now]:
#             indegree[i] -= 1
#             dp[i] = max(dp[now] + t[i], dp[i])
#             if indegree[i] == 0:
#                 q.append(i)
#     return max(dp)
#
# n = 7
# for _ in range(1000000):
#     arr = [[5, 0]]
#     for i in range(1, n):
#         cost = random.randrange(1, 10)
#         preNum = random.randrange(0, i)
#         pre = []
#         for _ in range(preNum):
#             while True:
#                 randomNum = random.randrange(1, i)
#                 if randomNum not in pre:
#                     pre.append(randomNum)
#                     break
#         arr.append([cost, preNum] + pre)
#
#     a = sol1(n, arr)
#     b = sol2(n, arr)
#     if a != b:
#         print(n)
#         print(arr)
#         print(a, b)
#         break

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
pre = [0] + [arr[i][1] for i in range(len(arr))]
next = {i: [] for i in range(1, n + 1)}
res = [0] + [0] * n

q = deque()
for i in range(len(arr)):
    if 0 < arr[i][1]:
        for j in range(2, 2 + arr[i][1]):
            next[arr[i][j]].append(i + 1)
    else:
        q.append([arr[i][0], 0, i + 1])


while q:
    spendTime, preTime, cur = q.popleft()
    res[cur] = max(res[cur], spendTime + preTime)
    for nextTask in next[cur]:
        pre[nextTask] -= 1
        # res[nextTask] = max(res[nextTask], spendTime + preTime + arr[nextTask - 1][0])
        res[nextTask] = max(res[nextTask], res[cur] + arr[nextTask - 1][0])
        if pre[nextTask] == 0:
            q.append([arr[nextTask - 1][0], spendTime + preTime, nextTask])

print(max(res))