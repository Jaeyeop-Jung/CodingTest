# TODO 틀림 잘 생각해봐라;;


import sys
from collections import deque
import heapq

input = sys.stdin.readline

n = int(input())
arr = [sorted(list(map(int, input().split()))) for _ in range(n)]
k = int(input())

temp = []
for start, end in arr:
    if end - start <= k:
        temp.append([start, end])

temp.sort(key=lambda x: x[1])
q = deque(temp)
res = 0
h = []
while q:
    start, end = q.popleft()
    while h and h[0][0] < end - k:
        heapq.heappop(h)
    heapq.heappush(h, [start, end])
    res = max(res, len(h))

print(res)