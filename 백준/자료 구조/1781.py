# TODO 틀림

import sys
import heapq

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()

h = []
for deadline, cup in arr:
    heapq.heappush(h, cup)
    if deadline < len(h):
        heapq.heappop(h)

print(sum(h))