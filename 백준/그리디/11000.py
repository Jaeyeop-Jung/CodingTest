import sys
import heapq

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x: x[0])

h = []
result = 0
for start, end in arr:
    # if not h:
    #     result = max(result, 1)
    #     heapq.heappush(h, end)
    #     continue
    #
    # if start < h[0]:
    #     heapq.heappush(h, end)
    #     result = max(result, len(h))
    # elif start == h[0]:
    #     heapq.heappop(h)
    #     heapq.heappush(h, end)
    # else:
    #     heapq.heappush(h, end)

    while h and h[0] <= start:
        heapq.heappop(h)
    heapq.heappush(h, end)
    result = max(result, len(h))

print(result)