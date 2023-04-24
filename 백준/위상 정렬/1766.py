# TODO 틀림

import heapq
from collections import defaultdict

n, m = map(int, input().split())
degree = defaultdict(int)
way = defaultdict(list)
for _ in range(m):
    a, b, = map(int, input().split())
    degree[b] += 1
    way[a].append(b)

h = []
for i in range(1, n + 1):
    if degree[i] == 0:
        heapq.heappush(h, i)

result = []
while h:
    pop = heapq.heappop(h)
    result.append(pop)
    for before in way[pop]:
        degree[before] -= 1
        if degree[before] == 0:
            heapq.heappush(h, before)

print(*result)