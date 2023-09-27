import heapq
import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()

res = 0
h = []
for start, end in arr:
    if not h:
        heapq.heappush(h, end)
    else:
        if h[0] <= start:
            heapq.heappop(h)
        heapq.heappush(h, end)
    res = max(res, len(h))

print(res)