import heapq
from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: (x[1], x[2], x[0]))

res = 0
h = []
for num, start, end in arr:
    while h and h[0] <= start:
        heapq.heappop(h)
    heapq.heappush(h, end)
    res = max(res, len(h))

q = deque([i for i in range(1, res + 1)])
h = []
print(res)
resArr = []
for num, start, end in arr:
    while h and h[0][0] <= start:
        _, popNum, = heapq.heappop(h)
        q.append(popNum)
    new = q.popleft()
    heapq.heappush(h, [end, new])
    resArr.append([num, new])

resArr.sort(key=lambda x: x[0])
for _, num in resArr:
    print(num)