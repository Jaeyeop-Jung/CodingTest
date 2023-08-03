import sys
import heapq
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dist, cur = map(int, input().split())

arr.sort()
arr = deque(arr)
res = 0
h = []
while cur < dist:
    while arr and arr[0][0] <= cur:
        pop = arr.popleft()
        heapq.heappush(h, [-pop[1], pop[0]])
    if not h:
        break
    pop = heapq.heappop(h)
    res += 1
    cur -= pop[0]

print(res if dist <= cur else -1)