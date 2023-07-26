import sys
from collections import deque
import heapq

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x: (x[0], x[1]))
arr = deque(arr)
h = []
res = 0
while arr:
    start, end = arr.popleft()
    while h and h[0][0] <= start:
        heapq.heappop(h)
    heapq.heappush(h, [end, start])
    res = max(res, len(h))

print(res)