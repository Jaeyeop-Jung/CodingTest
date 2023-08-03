import heapq

n = int(input())
cur = int(input())
arr = [-int(input()) for _ in range(n - 1)]

heapq.heapify(arr)
res = 0
while arr and cur <= -arr[0]:
    heapq.heappush(arr, heapq.heappop(arr) + 1)
    res += 1
    cur += 1
print(res)