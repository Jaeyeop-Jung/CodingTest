import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n + 2)]

    visited = [False] * (n + 2)
    visited[0] = True
    q = deque()
    q.append(arr[0])
    while q:
        r, c, = q.popleft()
        for i in range(n + 2):
            if visited[i]:
                continue
            nextR, nextC, = arr[i]
            if abs(r - nextR) + abs(c - nextC) <= 1000:
                visited[i] = True
                q.append([nextR, nextC])

    print('happy' if visited[-1] else 'sad')
