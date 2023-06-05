import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.readline

n, m, = map(int, input().split())
graph = defaultdict(list)
degree = [0] * (n + 1)
for _ in range(m):
    arr = list(map(int, input().split()))
    for i in range(1, arr[0]):
        graph[arr[i + 1]].append(arr[i])
        degree[arr[i]] += 1

q = deque()
res = []
for i in range(1, n + 1):
    if degree[i] == 0:
        q.append(i)
        res.append(i)

while q:
    cur = q.popleft()
    for next in graph[cur]:
        degree[next] -= 1
        if degree[next] == 0:
            q.append(next)
            res.append(next)

if len(res) == n:
    for i in reversed(res):
        print(i)
else:
    print(0)