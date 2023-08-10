import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.readline

t = int(input())
for testCase in range(t):
    k, m, p = map(int, input().split())
    degree = [0] * (m + 1)
    graph = defaultdict(list)
    for _ in range(p):
        a, b = map(int, input().split())
        graph[a].append(b)
        degree[b] += 1
    strahlerCnt = [defaultdict(int) for _ in range(m + 1)]
    strahler = [-1] * (m + 1)

    q = deque()
    for i in range(1, len(degree)):
        if degree[i] == 0:
            q.append(i)
            strahlerCnt[i][1] += 1
            strahler[i] = 1
    while q:
        cur = q.popleft()
        for next in graph[cur]:
            degree[next] -= 1
            strahlerCnt[next][strahler[cur]] += 1
            if degree[next] == 0:
                q.append(next)
                maxKey = max(strahlerCnt[next].keys())
                if 2 <= strahlerCnt[next][maxKey]:
                    strahler[next] = maxKey + 1
                else:
                    strahler[next] = maxKey
    print(k, max(strahler))
