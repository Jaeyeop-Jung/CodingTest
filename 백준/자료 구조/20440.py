import math
import sys
import heapq

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x: (x[0], x[1]))
h = []
res = 0
resStart = math.inf
resEnd = -math.inf
for i in range(n):
    while h and h[0] <= arr[i][0]:
        heapq.heappop(h)
    heapq.heappush(h, arr[i][1])
    if res < len(h):
        res = len(h)
        resStart = arr[i][0]
        resEnd = h[0]
    if res == len(h) and resEnd == arr[i][0]:
        resEnd = arr[i][1]

print(res)
print(resStart, resEnd)