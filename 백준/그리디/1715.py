import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

heapq.heapify(arr)
result = 0
while arr:
    if len(arr) <= 1:
        break
    pop1 = heapq.heappop(arr)
    pop2 = heapq.heappop(arr)
    result += pop1 + pop2
    heapq.heappush(arr, pop1 + pop2)

print(result)