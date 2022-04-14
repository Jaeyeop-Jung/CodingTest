import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    d.insert(0, 0)
    graph = [[] for j in range(n + 1)]
    indegree = [0] * (n + 1)
    for j in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1
    w = int(input())

    dp = [0] * (n + 1)
    q = deque()
    for j in range(1, n + 1):
        if indegree[j] == 0:
            q.append(j)
            dp[j] += d[j]

    while q:
        now = q.popleft()

        for j in graph[now]:
            indegree[j] -= 1
            dp[j] = max(dp[j], dp[now] + d[j])
            if indegree[j] == 0:
                q.append(j)

    print(dp[w])
