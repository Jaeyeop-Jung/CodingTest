import heapq
from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x: x[1])
arr = deque(arr)

h = []
while 2 <= len(arr):
    leftCnt, left = arr.popleft()
    rightCnt, right = arr.pop()

    if leftCnt == rightCnt:
        pass
    elif leftCnt < rightCnt:
        arr.append([rightCnt - leftCnt, right])
    else:
        arr.appendleft([leftCnt - rightCnt, left])
    heapq.heappush(h, -(left + right))

cnt, num = arr.pop()
if 2 <= cnt:
    heapq.heappush(h, -(num + num))

print(-heapq.heappop(h))