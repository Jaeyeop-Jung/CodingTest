# TODO 틀림

import sys
import heapq
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: x[0])

h = []
res = []
q = deque(arr)
while q:
    start, height, end = q.popleft()
    temp = [[-height, start, end]]
    while q and q[0][0] == temp[0][1] and q[0][1] == temp[0][2]:
        start, height, end = q.popleft()
        heapq.heappush(temp, [-height, start, end])
    preEnd = -1
    while h and h[0][2] < start:
        _, _, pop = heapq.heappop(h)
        if pop <= preEnd:
            continue
        preEnd = pop
    if h and preEnd != -1:
        res.append(preEnd)
        res.append(-h[0][0])
    elif not h and preEnd != -1:
        res.append(preEnd)
        res.append(0)
    heapq.heappush(h, [-height, start, end])
    if h[0] == [-height, start, end] and not (res and -h[0][0] == res[-1]):
        res.append(start)
        res.append(height)

preEnd = -1
while h:
    height, start, end, = heapq.heappop(h)
    if preEnd < end:
        while h and h[0][2] < end:
            heapq.heappop(h)
        if h and -h[0][0] == res[-1]:
            continue
        res.append(end)
        if h:
            res.append(-h[0][0])
        else:
            res.append(0)

print(*res)
