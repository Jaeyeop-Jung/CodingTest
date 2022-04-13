from collections import deque

t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    d.insert(0, 0)
    graph = [[] for i in range(n + 1)]
    indegree = [0] * (n + 1)
    for i in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1
    w = int(input())

    result = []
    dp = [0] * (n + 1)
    q = deque()
    for i in range(n + 1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] += d[i]

    while q:
        now = q.popleft()
        result.append(now)
        max_d = 0

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
                max_d = max(max_d, d[i])
        for i in graph[now]:
            dp[i] = dp[now] + max_d
    print(dp)





