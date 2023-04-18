import heapq
from collections import deque

n = int(input())
arr = []
for i in range(n):
    startTime, spendTime = map(int, input().split())
    arr.append([i, startTime, spendTime])
arr.sort(key=lambda x: (x[1], x[0]))
arr = deque(arr)

cur = arr.popleft()
cur = cur[1] + cur[2]
wait = []
result = 0
while True:
    while arr and arr[0][1] <= cur:
        idx, startTime, spendTime = arr.popleft()
        heapq.heappush(wait, [idx, startTime, spendTime])

    if not wait:
        if not arr:
            break
        wait.append(arr.popleft())
        cur = wait[0][1]

    idx, startTime, spendTime, = heapq.heappop(wait)
    result = max(result, cur - startTime)
    cur += spendTime

print(result)