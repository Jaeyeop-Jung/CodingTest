import heapq
import sys

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

h = []
res = [0] * n
for i in range(n):
    while h and h[0][0] <= arr[i]:
        _, idx, = heapq.heappop(h)
        res[idx] = i - idx - 1
    heapq.heappush(h, [arr[i], i])

while h:
    _, idx = heapq.heappop(h)
    res[idx] = n - idx - 1

print(sum(res))