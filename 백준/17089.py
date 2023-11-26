import math
import sys
from collections import defaultdict

input = sys.stdin.readline

n, m, = map(int, input().split())
graph = defaultdict(set)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].add(b - 1)
    graph[b - 1].add(a - 1)

def dfs(graph, cur):
    if len(cur) == 3:
        if cur[0] in graph[cur[-1]]:
            global res
            res = min(res, len(graph[cur[0]]) + len(graph[cur[1]]) + len(graph[cur[2]]) - 6)
        return

    for next in graph[cur[-1]]:
        if next not in cur:
            dfs(graph, cur + [next])


res = math.inf
for start in range(n):
    dfs(graph, [start])

if res == math.inf:
    print(-1)
else:
    print(res)