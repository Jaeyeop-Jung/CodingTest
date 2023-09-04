import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
arr = [input().strip() for _ in range(n)]
start, end, = map(int, input().split())

graph = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            continue

        cnt = 0
        for cur in range(k):
            if arr[i][cur] != arr[j][cur]:
                cnt += 1
                if 2 <= cnt:
                    break
        else:
            graph[i].append(j)
            graph[j].append(i)

q = deque()
q.append([start - 1, [start - 1]])
visited = [False] * n
visited[start - 1] = True
while q:
    cur, path, = q.popleft()
    if cur == end - 1:
        for route in path:
            print(route + 1, end=' ')
        exit()
    for next in graph[cur]:
        if not visited[next]:
            q.append([next, path + [next]])
            visited[next] = True

print(-1)