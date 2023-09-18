import heapq

n, m, = map(int, input().split())
h = list(map(int, input().split()))
heapq.heapify(h)

for _ in range(m):
    total = 0
    for _ in range(2):
        total += heapq.heappop(h)
    heapq.heappush(h, total)
    heapq.heappush(h, total)

print(sum(h))
