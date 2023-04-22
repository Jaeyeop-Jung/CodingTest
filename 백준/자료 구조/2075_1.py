import heapq
import sys

input = sys.stdin.readline

n = int(input())
h = []
for _ in range(n):
    temp = list(map(int, input().split()))
    for i in temp:
        if len(h) < n:
            heapq.heappush(h, i)
        else:
            heapq.heappush(h, i)
            heapq.heappop(h)

# for _ in range(n - 1):
#     heapq.heappop(h)
print(heapq.heappop(h))