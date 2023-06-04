# TODO 틀림 깊게 생각해봐라

import math
from collections import deque
from collections import defaultdict

n = int(input())
graph = defaultdict(list)
for _ in range(n):
    start, end, cost, = input().split()
    graph[start].append([end, cost])
    graph[end].append([start, cost])

price = defaultdict(int)
visited = defaultdict(bool)
def dfs(graph, visited, cur, before):
    if cur == 'Z':
        return before
    totalCost = 0
    for next, cost in graph[cur]:
        if not visited[next]:
            visited[next] = True
            totalCost += dfs(graph, visited, next, int(cost))
            visited[next] = False
    return min(totalCost, before)


visited['A'] = True
print(dfs(graph, visited, 'A', math.inf))