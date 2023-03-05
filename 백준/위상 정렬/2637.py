# TODO 틀림 할 수 있다 아이디어는 잘 맞춤

# from collections import defaultdict
#
# n = int(input())
# m = int(input())
# graph = [[] for _ in range(n + 1)]
# for _ in range(m):
#     next, prev, cost = map(int, input().split())
#     graph[next].append([prev, cost])
#
# result = defaultdict(int)
#
# def dfs(graph, cur, cost):
#     if not graph[cur]:
#         global result
#         result[cur] += cost
#         return
#     for next, next_cost in graph[cur]:
#         dfs(graph, next, cost * next_cost)
#
# dfs(graph, n, 1)
#
# for key in sorted(result.keys()):
#     print(f'{key} {result[key]}')

from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
degree = [0] * (n + 1)
for _ in range(m):
    next, prev, cost = map(int, input().split())
    graph[prev].append([next, cost])
    degree[next] += 1

q = deque()
for i in range(1, n + 1):
    if degree[i] == 0:
        q.append(i)

dp = [[0] * (n + 1) for _ in range(n + 1)]
for i in q:
    dp[i][i] += 1

while q:
    cur = q.popleft()
    for next, cost in graph[cur]:
        for i in range(len(dp)):
            dp[next][i] += (dp[cur][i] * cost)
        degree[next] -= 1
        if degree[next] == 0:
            q.append(next)

for i in range(len(dp[-1])):
    if dp[-1][i] != 0:
        print(f'{i} {dp[-1][i]}')