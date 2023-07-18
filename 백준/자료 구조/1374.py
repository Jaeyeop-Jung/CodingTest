import sys
import heapq

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x: (x[1], x[2]))
h = []
res = 0
for i in range(n):
    num, start, end, = arr[i]
    while h and h[0][0] <= start:
        heapq.heappop(h)
    heapq.heappush(h, [end, start])
    res = max(res, len(h))

print(res)
