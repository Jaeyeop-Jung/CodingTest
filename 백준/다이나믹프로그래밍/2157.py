# TODO 틀림 거의 맞았다 예외만 잘 걸러봐

from collections import defaultdict

n, m, k = map(int, input().split())
graph = {i: defaultdict(int) for i in range(n + 1)}
for _ in range(k):
    u, v, w = map(int, input().split())
    if v <= u:
        continue
    graph[u][v] = max(graph[u][v], w)

dp = [[0] * (n + 1) for _ in range(m)]
# row는 지나간 간선의 갯수
# 1번에서 출발 가능한 곳 초기화
for key in graph[1]:
    dp[1][key] = graph[1][key]

# 간선을 지난 횟수
for r in range(2, m):
    # 도착 지점
    for c in range(r, n + 1):
        for k in range(c):
            # k -> c로 길이 있고, 현재 - 1개의 간선을 지났을 때 경우가 있으면
            dp[r][c] = max(dp[r - 1][c], dp[r][c])
            if graph[k][c] != 0 and dp[r - 1][k] != 0:
                dp[r][c] = max(dp[r][c], dp[r - 1][k] + graph[k][c])

print(dp[-1][-1])