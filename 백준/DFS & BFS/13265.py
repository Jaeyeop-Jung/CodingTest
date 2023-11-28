import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, = map(int, input().split())
    visited = [False] * n
    graph = [[] for _ in range(n)]
    dic = {}
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    flag = False
    for num in range(n):
        if visited[num]:
            continue
        q = deque([num])
        visited[num] = True
        dic[num] = 1
        while q:
            cur = q.popleft()
            for next in graph[cur]:
                if next in dic and dic[next] == dic[cur]:
                    flag = True
                    break
                if not visited[next]:
                    dic[next] = dic[cur] ^ 1
                    q.append(next)
                    visited[next] = True
            if flag:
                break
        if flag:
            break

    print('impossible' if flag else 'possible')
