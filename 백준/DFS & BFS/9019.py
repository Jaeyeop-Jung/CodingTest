# TODO 틀림

import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b, = map(int, input().split())
    q = deque()
    q.append([str(a).rjust(4, '0'), ''])
    visited = [False] * 10000
    visited[a] = True
    while q:
        cur, route, = q.popleft()
        if int(cur) == b:
            print(route)
            break

        if not visited[int(cur) * 2 % 10000]:
            q.append([str(int(cur) * 2 % 10000), route + 'D'])
            visited[int(cur) * 2 % 10000] = True

        temp = int(cur) - 1 % 10000
        if not visited[temp]:
            visited[temp] = True
            q.append([str(temp), route + 'S'])

        s = str(cur)
        if not visited[int(s[1:] + s[0])]:
            q.append([s[1:] + s[0], route + 'L'])
            visited[int(s[1:] + s[0])] = True
        if not visited[int(s[-1] + s[:-1])]:
            q.append([s[-1] + s[:-1], route + 'R'])
            visited[int(s[-1] + s[:-1])] = True
